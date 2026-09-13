import { useMemo, useState } from "react";
import { looksEnglish } from "../lib/speech";
import { formatMatchAnswer, parseMatchSides, shuffleList, type QuizOptions } from "../lib/match";
import { SpeakButton } from "./SpeakButton";

export function MatchQuestion({
  options,
  value,
  onChange,
  disabled = false,
}: {
  options: QuizOptions;
  value: string;
  onChange: (answer: string) => void;
  disabled?: boolean;
}) {
  const sides = useMemo(() => parseMatchSides(options), [options]);
  const left = sides?.left || [];
  const right = useMemo(() => shuffleList(sides?.right || []), [sides?.right?.join("\0")]);
  const [activeLeft, setActiveLeft] = useState<string | null>(null);

  const pairs = useMemo(() => {
    const map: Record<string, string> = {};
    for (const part of (value || "").split(";")) {
      const trimmed = part.trim();
      if (!trimmed.includes("=")) continue;
      const [l, r] = trimmed.split("=", 2);
      if (l.trim() && r.trim()) map[l.trim()] = r.trim();
    }
    return map;
  }, [value]);

  if (!sides || !left.length || !right.length) {
    return (
      <p className="rounded-xl border border-rose/40 bg-[#fff5f3] px-4 py-3 text-sm text-rose">
        Не удалось загрузить пары для соотнесения. Обновите страницу или перезапустите seed.
      </p>
    );
  }

  const setPair = (leftItem: string, rightItem: string) => {
    const next = { ...pairs, [leftItem]: rightItem };
    onChange(formatMatchAnswer(next));
    setActiveLeft(null);
  };

  const clearPair = (leftItem: string) => {
    const next = { ...pairs };
    delete next[leftItem];
    onChange(formatMatchAnswer(next));
  };

  return (
    <div className="grid gap-3">
      <p className="text-sm text-ink-soft">Соедините: слева маркер / элемент, справа категория. Сначала нажмите слева, затем справа.</p>
      <div className="grid gap-4 md:grid-cols-2">
        <div className="grid gap-2">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-ink-soft">Маркер</p>
          {left.map((item) => (
            <div key={item} className="flex items-center gap-2">
              <button
                type="button"
                disabled={disabled}
                onClick={() => {
                  if (pairs[item]) clearPair(item);
                  setActiveLeft(item);
                }}
                className={`min-w-0 flex-1 rounded-xl border px-4 py-3 text-left transition ${
                  activeLeft === item ? "border-terra bg-[#fff1eb]" : "border-line bg-white hover:border-terra/50"
                }`}
              >
                <span className="font-medium">{item}</span>
                {pairs[item] && <span className="mt-1 block text-sm text-ink-soft">→ {pairs[item]}</span>}
              </button>
              {looksEnglish(item) && <SpeakButton text={item} />}
            </div>
          ))}
        </div>
        <div className="grid gap-2">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-ink-soft">Время / категория</p>
          {right.map((item) => (
            <div key={item} className="flex items-center gap-2">
              <button
                type="button"
                disabled={disabled || !activeLeft}
                onClick={() => activeLeft && setPair(activeLeft, item)}
                className={`min-w-0 flex-1 rounded-xl border px-4 py-3 text-left transition ${
                  Object.values(pairs).includes(item) ? "border-sage/50 bg-sage-soft/40" : "border-line bg-white hover:border-terra/50"
                } ${!activeLeft ? "opacity-70" : ""}`}
              >
                {item}
              </button>
              {looksEnglish(item) && <SpeakButton text={item} />}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export function matchAnswerComplete(options: QuizOptions, value: string): boolean {
  const sides = parseMatchSides(options);
  if (!sides) return false;
  const paired = new Set(
    (value || "")
      .split(";")
      .map((part) => part.trim().split("=", 1)[0]?.trim())
      .filter(Boolean),
  );
  return sides.left.every((item) => paired.has(item));
}
