import { useMemo, useState } from "react";
import { looksEnglish } from "../lib/speech";
import {
  formatMatchAnswer,
  parseMatchAnswer,
  parseMatchSides,
  shuffleList,
  type QuizOptions,
} from "../lib/match";
import { SpeakButton } from "./SpeakButton";

type Chip = { id: string; label: string };

export function MatchQuestion({
  options,
  value,
  onChange,
  disabled = false,
  checked = false,
  correct = false,
  expected = null,
}: {
  options: QuizOptions;
  value: string;
  onChange: (answer: string) => void;
  disabled?: boolean;
  /** After «Проверить»: highlight correct/incorrect slots */
  checked?: boolean;
  correct?: boolean;
  expected?: string | null;
}) {
  const sides = useMemo(() => parseMatchSides(options), [options]);
  const left = sides?.left || [];
  const chips = useMemo<Chip[]>(() => {
    const right = sides?.right || [];
    return shuffleList(right.map((label, i) => ({ id: `chip-${i}-${label}`, label })));
  }, [sides?.right?.join("\0")]);

  const [selectedChipId, setSelectedChipId] = useState<string | null>(null);
  const [selectedSlot, setSelectedSlot] = useState<string | null>(null);

  const pairs = useMemo(() => parseMatchAnswer(value), [value]);
  const expectedPairs = useMemo(() => (checked ? parseMatchAnswer(expected || "") : {}), [checked, expected]);

  const chipInSlot = useMemo(() => {
    const used = new Set<string>();
    const map: Record<string, Chip> = {};
    for (const [slot, label] of Object.entries(pairs)) {
      const chip = chips.find((c) => c.label === label && !used.has(c.id));
      if (chip) {
        used.add(chip.id);
        map[slot] = chip;
      }
    }
    return map;
  }, [chips, pairs]);

  const poolChips = chips.filter((c) => !Object.values(chipInSlot).some((x) => x.id === c.id));

  if (!sides || !left.length || !chips.length) {
    return (
      <p className="rounded-xl border border-rose/40 bg-[#fff5f3] px-4 py-3 text-sm text-rose">
        Не удалось загрузить пары для соотнесения. Обновите страницу или перезапустите seed.
      </p>
    );
  }

  const commitPairs = (next: Record<string, string>) => {
    onChange(formatMatchAnswer(next));
    setSelectedChipId(null);
    setSelectedSlot(null);
  };

  const assign = (slot: string, chip: Chip) => {
    const next = { ...pairs };
    // Clear only this chip's current slot (by id), not every slot with the same label —
    // duplicate labels (e.g. two «Perfect») are valid.
    for (const [s, occupied] of Object.entries(chipInSlot)) {
      if (occupied.id === chip.id) delete next[s];
    }
    delete next[slot];
    next[slot] = chip.label;
    commitPairs(next);
  };

  const clearSlot = (slot: string) => {
    if (disabled) return;
    const next = { ...pairs };
    delete next[slot];
    commitPairs(next);
  };

  const onChipClick = (chip: Chip) => {
    if (disabled) return;
    if (selectedSlot) {
      assign(selectedSlot, chip);
      return;
    }
    setSelectedChipId((prev) => (prev === chip.id ? null : chip.id));
    setSelectedSlot(null);
  };

  const onSlotClick = (slot: string) => {
    if (disabled) return;
    const occupied = chipInSlot[slot];
    if (selectedChipId) {
      const chip = chips.find((c) => c.id === selectedChipId);
      if (chip) {
        assign(slot, chip);
        return;
      }
    }
    if (occupied) {
      clearSlot(slot);
      return;
    }
    setSelectedSlot((prev) => (prev === slot ? null : slot));
    setSelectedChipId(null);
  };

  const slotTone = (slot: string) => {
    if (!checked) {
      if (selectedSlot === slot) return "border-terra bg-[#fff1eb]";
      if (chipInSlot[slot]) return "border-line bg-white";
      return "border-dashed border-line bg-paper-2/40";
    }
    if (correct) return "border-sage/60 bg-sage-soft/50";
    const given = pairs[slot];
    const want = expectedPairs[slot];
    if (want && given && given.trim().toLowerCase() === want.trim().toLowerCase()) {
      return "border-sage/60 bg-sage-soft/50";
    }
    return "border-rose/50 bg-[#fff5f3]";
  };

  return (
    <div className="grid gap-4">
      <p className="text-sm text-ink-soft">
        Перетащите / назначьте форму справа в слот слева: нажмите чип, затем пустой слот (или сначала слот, затем чип).
        Нажмите назначенный чип в слоте, чтобы вернуть его. Результат — только после «Проверить».
      </p>

      <div className="grid gap-4 lg:grid-cols-[minmax(0,1.2fr)_minmax(0,1fr)] lg:items-start">
        <div className="grid gap-2">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-ink-soft">Слоты</p>
          {left.map((item) => {
            const chip = chipInSlot[item];
            return (
              <div key={item} className="grid grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)] items-stretch gap-2">
                <div className="flex min-h-[3.25rem] items-center gap-2 rounded-xl border border-line bg-paper-2 px-3 py-2">
                  <span className="min-w-0 flex-1 text-sm font-medium leading-snug sm:text-base">{item}</span>
                  {looksEnglish(item) && <SpeakButton text={item} />}
                </div>
                <button
                  type="button"
                  disabled={disabled}
                  onClick={() => onSlotClick(item)}
                  aria-label={
                    chip
                      ? `Слот для «${item}»: ${chip.label}. Нажмите, чтобы убрать.`
                      : `Пустой слот для «${item}»`
                  }
                  className={`flex min-h-[3.25rem] items-center justify-center rounded-xl border px-2 py-2 text-center text-sm font-semibold leading-snug transition ${slotTone(item)} ${
                    disabled ? "cursor-default opacity-80" : "hover:border-terra/50"
                  }`}
                >
                  {chip ? (
                    <span className="line-clamp-3 break-words">{chip.label}</span>
                  ) : (
                    <span className="text-xs font-medium text-ink-soft/70">слот</span>
                  )}
                </button>
              </div>
            );
          })}
        </div>

        <div className="grid gap-2">
          <p className="text-xs font-semibold uppercase tracking-[0.14em] text-ink-soft">Формы</p>
          <div className="flex min-h-[3.25rem] flex-wrap content-start gap-2 rounded-xl border border-dashed border-line bg-paper-2/60 p-3">
            {poolChips.length === 0 ? (
              <p className="self-center text-sm text-ink-soft">
                {left.some((slot) => !chipInSlot[slot])
                  ? "Не хватает форм для всех слотов — обновите страницу или перезапустите seed."
                  : "Все формы назначены"}
              </p>
            ) : (
              poolChips.map((chip) => (
                <div key={chip.id} className="inline-flex max-w-full items-center gap-1">
                  <button
                    type="button"
                    disabled={disabled}
                    onClick={() => onChipClick(chip)}
                    className={`inline-flex min-h-[2.5rem] max-w-full items-center rounded-lg border px-3 py-1.5 text-sm font-semibold transition ${
                      selectedChipId === chip.id
                        ? "border-terra bg-[#fff1eb]"
                        : "border-line bg-white hover:border-terra/50"
                    } ${disabled ? "cursor-default opacity-80" : ""}`}
                  >
                    <span className="truncate">{chip.label}</span>
                  </button>
                  {looksEnglish(chip.label) && <SpeakButton text={chip.label} />}
                </div>
              ))
            )}
          </div>
          {selectedChipId && !selectedSlot && (
            <p className="text-xs text-ink-soft">Выбрана форма — нажмите пустой слот слева.</p>
          )}
          {selectedSlot && !selectedChipId && (
            <p className="text-xs text-ink-soft">Выбран слот — нажмите форму справа.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export function matchAnswerComplete(options: QuizOptions, value: string): boolean {
  const sides = parseMatchSides(options);
  if (!sides) return false;
  const paired = parseMatchAnswer(value);
  return sides.left.every((item) => Boolean(paired[item]));
}
