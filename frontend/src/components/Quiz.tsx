import { useMemo, useState, type CSSProperties } from "react";
import { CheckCircle2, CircleAlert } from "lucide-react";
import { fullSentenceInstruction, kindLabel } from "../lib/kindLabels";
import { extractEnglish, looksEnglish, speakableEnglish } from "../lib/speech";
import { type QuizOptions } from "../lib/match";
import { MatchQuestion, matchAnswerComplete } from "./MatchQuestion";
import { PromptWithBlanks, countBlanks, joinGapAnswers } from "./PromptWithBlanks";
import { SpeakButton } from "./SpeakButton";

export type QuizItem = {
  id: number;
  kind: string;
  prompt: string;
  options?: QuizOptions;
  solved?: boolean;
};

type Result = {
  correct: boolean;
  explanation: string;
  expected?: string | null;
};

export function Quiz({
  items,
  onCheck,
  submitLabel = "Проверить",
}: {
  items: QuizItem[];
  onCheck: (id: number, answer: string) => Promise<Result>;
  submitLabel?: string;
}) {
  return (
    <div className="grid gap-5">
      {items.map((item, index) => (
        <QuizCard key={`${item.id}-${item.kind}-${index}`} item={item} index={index} onCheck={onCheck} submitLabel={submitLabel} />
      ))}
    </div>
  );
}

function QuizCard({
  item,
  index,
  onCheck,
  submitLabel,
}: {
  item: QuizItem;
  index: number;
  onCheck: (id: number, answer: string) => Promise<Result>;
  submitLabel: string;
}) {
  const blankCount = countBlanks(item.prompt);
  const [value, setValue] = useState("");
  const [blanks, setBlanks] = useState<string[]>(() => Array.from({ length: blankCount }, () => ""));
  const [result, setResult] = useState<Result | null>(null);
  const [busy, setBusy] = useState(false);
  const isMatch = item.kind === "match";
  const choiceOptions = useMemo(() => {
    if (isMatch || !item.options || !Array.isArray(item.options)) return null;
    return [...item.options].sort(() => Math.random() - 0.5);
  }, [item.id, item.prompt, item.options, isMatch]);

  const useInlineGaps = blankCount > 0 && !isMatch && !choiceOptions;
  const answerText = useInlineGaps ? joinGapAnswers(blanks) : value.trim();
  const canSubmit = isMatch ? matchAnswerComplete(item.options, value) : !!answerText.trim();
  const speakText = speakableEnglish(item.prompt);
  const showSpeak = Boolean(extractEnglish(item.prompt) || speakText);
  const rewriteHint = fullSentenceInstruction(item.kind, blankCount > 0);
  const done = Boolean(item.solved || result?.correct);

  const submit = async () => {
    if (!canSubmit) return;
    setBusy(true);
    try {
      const res = await onCheck(item.id, answerText.trim());
      setResult(res);
    } finally {
      setBusy(false);
    }
  };

  return (
    <article
      className={`quiz-card motion-enter ${result ? (result.correct ? "quiz-card-ok" : "quiz-card-bad") : ""}`}
      style={{ "--motion-i": Math.min(index, 8) } as CSSProperties}
    >
      <header className="quiz-card-head">
        <span className="quiz-kind">
          {index + 1}. {kindLabel(item.kind)}
        </span>
        {done && (
          <span className="quiz-status-ok">
            <CheckCircle2 size={14} /> Верно
          </span>
        )}
      </header>

      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-[1.05rem] leading-relaxed sm:text-lg">
            <PromptWithBlanks
              text={item.prompt}
              values={useInlineGaps ? blanks : undefined}
              onChange={
                useInlineGaps
                  ? (next) => {
                      setBlanks(next);
                      setResult(null);
                    }
                  : undefined
              }
              onSubmit={useInlineGaps ? submit : undefined}
              disabled={!!result?.correct}
            />
          </p>
          {showSpeak && <SpeakButton text={item.prompt} speak={speakText} />}
        </div>

        {rewriteHint && !choiceOptions && !isMatch && <p className="quiz-hint">{rewriteHint}</p>}

        {isMatch ? (
          <MatchQuestion
            options={item.options}
            value={value}
            onChange={(next) => {
              setValue(next);
              setResult(null);
            }}
            disabled={!!result?.correct}
            checked={!!result}
            correct={!!result?.correct}
            expected={result?.expected}
          />
        ) : choiceOptions ? (
          <div className="grid gap-2">
            {choiceOptions.map((opt) => (
              <div key={opt} className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => {
                    setValue(opt);
                    setResult(null);
                  }}
                  className={`quiz-choice ${value === opt ? "is-selected" : ""}`}
                >
                  {opt}
                </button>
                {looksEnglish(opt) && <SpeakButton text={opt} />}
              </div>
            ))}
          </div>
        ) : useInlineGaps ? null : (
          <input
            className="field"
            value={value}
            onChange={(e) => {
              setValue(e.target.value);
              setResult(null);
            }}
            placeholder={
              item.kind === "order"
                ? "Соберите фразу"
                : rewriteHint
                  ? "Введите предложение целиком"
                  : "Введите ответ"
            }
            onKeyDown={(e) => e.key === "Enter" && submit()}
          />
        )}

        <div className="flex flex-wrap items-center gap-3 pt-1">
          <button className="btn btn-primary" disabled={busy || !canSubmit || !!result?.correct} onClick={submit}>
            {busy ? "Проверяем…" : result?.correct ? "Готово" : submitLabel}
          </button>
        </div>

        {result && (
          <div className={`quiz-feedback ${result.correct ? "is-ok" : "is-bad"}`} aria-live="polite">
            <div className="quiz-feedback-title">
              {result.correct ? (
                <>
                  <CheckCircle2 size={18} /> Отлично
                </>
              ) : (
                <>
                  <CircleAlert size={18} /> Нужно иначе
                </>
              )}
            </div>
            {!result.correct && result.expected && (
              <p className="quiz-feedback-expected">
                Верный ответ: <strong>{result.expected}</strong>
              </p>
            )}
            {!result.correct && result.explanation && (
              <p className="quiz-feedback-note">{result.explanation}</p>
            )}
            {result.correct && result.explanation && (
              <p className="quiz-feedback-note">{result.explanation}</p>
            )}
          </div>
        )}
      </div>
    </article>
  );
}
