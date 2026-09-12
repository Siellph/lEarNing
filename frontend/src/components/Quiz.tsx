import { useMemo, useState } from "react";
import { extractEnglish, looksEnglish } from "../lib/speech";
import { SpeakButton } from "./SpeakButton";

export type QuizItem = {
  id: number;
  kind: string;
  prompt: string;
  options?: string[] | null;
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
    <div className="grid gap-4">
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
  const [value, setValue] = useState("");
  const [result, setResult] = useState<Result | null>(null);
  const [busy, setBusy] = useState(false);
  const options = useMemo(() => {
    if (!item.options) return null;
    return [...item.options].sort(() => Math.random() - 0.5);
  }, [item.id, item.prompt]);

  const submit = async () => {
    if (!value.trim()) return;
    setBusy(true);
    try {
      const res = await onCheck(item.id, value.trim());
      setResult(res);
    } finally {
      setBusy(false);
    }
  };

  const kindLabel: Record<string, string> = {
    multiple_choice: "Выбор",
    fill_blank: "Пропуск",
    transform: "Преобразование",
    error_correction: "Исправление",
  };

  return (
    <article className="card p-5 sm:p-6">
      <div className="mb-3 flex flex-wrap items-center gap-2 text-xs">
        <span className="rounded-full bg-paper-2 px-2.5 py-1 font-semibold text-ink-soft">
          {index + 1}. {kindLabel[item.kind] || "Задание"}
        </span>
        {(item.solved || result?.correct) && (
          <span className="rounded-full bg-sage-soft px-2.5 py-1 font-semibold text-sage">Верно</span>
        )}
      </div>
      <div className="mb-4 flex items-start justify-between gap-3">
        <p className="text-lg leading-relaxed">{item.prompt}</p>
        {extractEnglish(item.prompt) && <SpeakButton text={extractEnglish(item.prompt) || item.prompt} />}
      </div>
      {options ? (
        <div className="grid gap-2">
          {options.map((opt) => (
            <div key={opt} className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => {
                  setValue(opt);
                  setResult(null);
                }}
                className={`min-w-0 flex-1 rounded-xl border px-4 py-3 text-left transition ${
                  value === opt ? "border-terra bg-[#fff1eb]" : "border-line bg-white hover:border-terra/50"
                }`}
              >
                {opt}
              </button>
              {looksEnglish(opt) && <SpeakButton text={opt} />}
            </div>
          ))}
        </div>
      ) : (
        <input
          className="field"
          value={value}
          onChange={(e) => {
            setValue(e.target.value);
            setResult(null);
          }}
          placeholder="Введите ответ"
          onKeyDown={(e) => e.key === "Enter" && submit()}
        />
      )}
      <div className="mt-4 flex flex-wrap items-center gap-3">
        <button className="btn btn-primary" disabled={busy || !value.trim()} onClick={submit}>
          {busy ? "Проверяем…" : submitLabel}
        </button>
        {result && (
          <span className={`text-sm font-semibold ${result.correct ? "text-sage" : "text-rose"}`}>
            {result.correct ? "Отлично" : `Правильный ответ: ${result.expected}`}
          </span>
        )}
      </div>
      {result && <p className="mt-3 text-sm leading-relaxed text-ink-soft">{result.explanation}</p>}
    </article>
  );
}
