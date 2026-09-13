import { useMemo, useState, type CSSProperties } from "react";
import { CheckCircle2, CircleAlert } from "lucide-react";
import { fullSentenceInstruction, kindLabel } from "../lib/kindLabels";
import { extractEnglish, looksEnglish, speakableEnglish } from "../lib/speech";
import { type QuizOptions } from "../lib/match";
import { MatchQuestion, matchAnswerComplete } from "./MatchQuestion";
import { PromptWithBlanks, countBlanks, joinGapAnswers } from "./PromptWithBlanks";
import { SpeakButton } from "./SpeakButton";

export type QuizLastResult = {
  correct: boolean;
  explanation: string;
  expected?: string | null;
  answer?: string | null;
};

export type QuizItem = {
  id: number;
  kind: string;
  prompt: string;
  options?: QuizOptions;
  solved?: boolean;
  last_result?: QuizLastResult | null;
};

type Result = {
  correct: boolean;
  explanation: string;
  expected?: string | null;
};

function splitGapValue(value: string, blankCount: number): string[] {
  if (blankCount <= 0) return [];
  if (blankCount <= 1) return [value || ""];
  const parts = value.split(" / ");
  if (parts.length === blankCount) return parts;
  return Array.from({ length: blankCount }, (_, i) => parts[i] || "");
}

function initialResult(item: QuizItem): Result | null {
  if (item.last_result) {
    return {
      correct: item.last_result.correct,
      explanation: item.last_result.explanation || "",
      expected: item.last_result.expected ?? null,
    };
  }
  if (item.solved) return { correct: true, explanation: "" };
  return null;
}

function initialAnswer(item: QuizItem): string {
  return item.last_result?.answer?.trim() || "";
}

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
  const restoredAnswer = initialAnswer(item);
  const [value, setValue] = useState(restoredAnswer);
  const [blanks, setBlanks] = useState<string[]>(() =>
    blankCount > 0 ? splitGapValue(restoredAnswer, blankCount) : [],
  );
  const [result, setResult] = useState<Result | null>(() => initialResult(item));
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
  const locked = !!result?.correct;
  const cardTone = result ? (result.correct ? "quiz-card-ok" : "quiz-card-bad") : "";

  const clearResult = () => {
    if (!locked) setResult(null);
  };

  const submit = async () => {
    if (!canSubmit || locked) return;
    setBusy(true);
    try {
      const res = await onCheck(item.id, answerText.trim());
      setResult(res);
    } finally {
      setBusy(false);
    }
  };

  return (
    <article className={`quiz-card motion-enter ${cardTone}`} style={{ "--motion-i": Math.min(index, 8) } as CSSProperties}>
      <header className="quiz-card-head">
        <span className="quiz-kind">
          {index + 1}. {kindLabel(item.kind)}
        </span>
        {result?.correct && (
          <span className="quiz-status-ok">
            <CheckCircle2 size={14} aria-hidden /> Верно
          </span>
        )}
        {result && !result.correct && (
          <span className="quiz-status-bad">
            <CircleAlert size={14} aria-hidden /> Неверно
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
                      clearResult();
                    }
                  : undefined
              }
              onSubmit={useInlineGaps ? submit : undefined}
              disabled={locked}
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
              clearResult();
            }}
            disabled={locked}
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
                  disabled={locked}
                  onClick={() => {
                    setValue(opt);
                    clearResult();
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
            disabled={locked}
            onChange={(e) => {
              setValue(e.target.value);
              clearResult();
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
          <button className="btn btn-primary" disabled={busy || !canSubmit || locked} onClick={submit}>
            {busy ? "Проверяем…" : locked ? "Готово" : submitLabel}
          </button>
        </div>

        {result && !result.correct && (result.expected || result.explanation) && (
          <div className="quiz-feedback is-bad" aria-live="polite">
            {result.expected && (
              <p className="quiz-feedback-expected">
                Верный ответ: <strong>{result.expected}</strong>
              </p>
            )}
            {result.explanation && <p className="quiz-feedback-note">{result.explanation}</p>}
          </div>
        )}
      </div>
    </article>
  );
}
