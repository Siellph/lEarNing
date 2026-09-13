import { useMemo, useRef, useState, type DragEvent } from "react";
import { looksEnglish } from "../lib/speech";
import {
  alignMatchPairs,
  formatMatchAnswer,
  parseMatchAnswer,
  parseMatchSides,
  resolveMatchPairs,
  shuffleList,
  type QuizOptions,
} from "../lib/match";
import { SpeakButton } from "./SpeakButton";

type Chip = { id: string; label: string };

const POOL_TARGET = "__pool__";

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
  const [draggingId, setDraggingId] = useState<string | null>(null);
  const [dropTarget, setDropTarget] = useState<string | null>(null);
  const draggingIdRef = useRef<string | null>(null);
  const skipClickRef = useRef(false);
  const skipClickTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const pairs = useMemo(() => {
    // When correct (incl. restore) and value is empty / mis-keyed, use expected.
    if (correct) return resolveMatchPairs(left, value, expected);
    return alignMatchPairs(left, parseMatchAnswer(value));
  }, [left, value, expected, correct]);
  const expectedPairs = useMemo(
    () => (checked ? alignMatchPairs(left, parseMatchAnswer(expected || "")) : {}),
    [checked, expected, left],
  );

  const chipInSlot = useMemo(() => {
    const used = new Set<string>();
    const map: Record<string, Chip> = {};
    // Only bind chips to real left slots — stray keys must not empty the pool.
    for (const slot of left) {
      const label = pairs[slot];
      if (!label) continue;
      const chip = chips.find((c) => c.label === label && !used.has(c.id));
      if (chip) {
        used.add(chip.id);
        map[slot] = chip;
      }
    }
    return map;
  }, [chips, pairs, left]);

  const poolChips = chips.filter((c) => !Object.values(chipInSlot).some((x) => x.id === c.id));

  if (!sides || !left.length || !chips.length) {
    return (
      <p className="rounded-xl border border-rose/40 bg-[#fff5f3] px-4 py-3 text-sm text-rose">
        Не удалось загрузить пары для соотнесения. Обновите страницу.
      </p>
    );
  }

  const allSlotsFilled = left.every((slot) => Boolean(chipInSlot[slot]));
  const formsShortage =
    poolChips.length === 0 && !allSlotsFilled && !disabled && !checked && !correct;

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

  const clearChipById = (chipId: string) => {
    for (const [s, occupied] of Object.entries(chipInSlot)) {
      if (occupied.id === chipId) {
        clearSlot(s);
        return;
      }
    }
  };

  const armSkipClick = () => {
    skipClickRef.current = true;
    if (skipClickTimerRef.current) clearTimeout(skipClickTimerRef.current);
    skipClickTimerRef.current = setTimeout(() => {
      skipClickRef.current = false;
      skipClickTimerRef.current = null;
    }, 80);
  };

  const consumeSkipClick = () => {
    if (!skipClickRef.current) return false;
    skipClickRef.current = false;
    if (skipClickTimerRef.current) {
      clearTimeout(skipClickTimerRef.current);
      skipClickTimerRef.current = null;
    }
    return true;
  };

  const readDragChipId = (e: DragEvent) =>
    e.dataTransfer.getData("text/plain") || draggingIdRef.current || "";

  const onChipDragStart = (e: DragEvent, chip: Chip) => {
    if (disabled) {
      e.preventDefault();
      return;
    }
    e.dataTransfer.setData("text/plain", chip.id);
    e.dataTransfer.effectAllowed = "move";
    draggingIdRef.current = chip.id;
    setDraggingId(chip.id);
    setSelectedChipId(null);
    setSelectedSlot(null);
  };

  const onChipDragEnd = () => {
    draggingIdRef.current = null;
    setDraggingId(null);
    setDropTarget(null);
    armSkipClick();
  };

  const onDragOverTarget = (e: DragEvent, target: string) => {
    if (disabled || !draggingIdRef.current) return;
    e.preventDefault();
    e.dataTransfer.dropEffect = "move";
    if (dropTarget !== target) setDropTarget(target);
  };

  const onDragLeaveTarget = (e: DragEvent, target: string) => {
    const related = e.relatedTarget as Node | null;
    if (related && e.currentTarget.contains(related)) return;
    if (dropTarget === target) setDropTarget(null);
  };

  const onDropSlot = (e: DragEvent, slot: string) => {
    e.preventDefault();
    e.stopPropagation();
    if (disabled) return;
    const chipId = readDragChipId(e);
    const chip = chips.find((c) => c.id === chipId);
    draggingIdRef.current = null;
    setDropTarget(null);
    setDraggingId(null);
    if (chip) assign(slot, chip);
  };

  const onDropPool = (e: DragEvent) => {
    e.preventDefault();
    if (disabled) return;
    const chipId = readDragChipId(e);
    draggingIdRef.current = null;
    setDropTarget(null);
    setDraggingId(null);
    if (chipId) clearChipById(chipId);
  };

  const onChipClick = (chip: Chip) => {
    if (disabled || consumeSkipClick()) return;
    if (selectedSlot) {
      assign(selectedSlot, chip);
      return;
    }
    setSelectedChipId((prev) => (prev === chip.id ? null : chip.id));
    setSelectedSlot(null);
  };

  const onSlotClick = (slot: string) => {
    if (disabled || consumeSkipClick()) return;
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
      if (dropTarget === slot) return "border-terra bg-[#fff1eb] match-drop-target";
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
                  draggable={!disabled && Boolean(chip)}
                  onDragStart={(e) => {
                    if (!chip) {
                      e.preventDefault();
                      return;
                    }
                    onChipDragStart(e, chip);
                  }}
                  onDragEnd={onChipDragEnd}
                  onClick={() => onSlotClick(item)}
                  onDragOver={(e) => onDragOverTarget(e, item)}
                  onDragLeave={(e) => onDragLeaveTarget(e, item)}
                  onDrop={(e) => onDropSlot(e, item)}
                  aria-label={
                    chip
                      ? `Слот для «${item}»: ${chip.label}. Нажмите, чтобы убрать.`
                      : `Пустой слот для «${item}»`
                  }
                  className={`match-slot flex min-h-[3.25rem] items-center justify-center rounded-xl border px-2 py-2 text-center text-sm font-semibold leading-snug transition ${slotTone(item)} ${
                    chip && !disabled ? "match-chip is-draggable" : ""
                  } ${draggingId && chip && draggingId === chip.id ? "is-dragging" : ""} ${
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
          <div
            className={`match-pool flex min-h-[3.25rem] flex-wrap content-start gap-2 rounded-xl border border-dashed border-line bg-paper-2/60 p-3 ${
              dropTarget === POOL_TARGET ? "is-drop-target" : ""
            }`}
            onDragOver={(e) => onDragOverTarget(e, POOL_TARGET)}
            onDragLeave={(e) => onDragLeaveTarget(e, POOL_TARGET)}
            onDrop={onDropPool}
          >
            {poolChips.length === 0 ? (
              <p
                className={`self-center text-sm ${
                  formsShortage ? "text-terra" : "text-ink-soft"
                }`}
              >
                {formsShortage
                  ? "Не хватает форм для всех слотов. Обновите страницу."
                  : draggingId
                    ? "Отпустите, чтобы вернуть форму"
                    : "Все формы назначены"}
              </p>
            ) : (
              poolChips.map((chip) => (
                <div key={chip.id} className="inline-flex max-w-full items-center gap-1">
                  <button
                    type="button"
                    disabled={disabled}
                    draggable={!disabled}
                    onDragStart={(e) => onChipDragStart(e, chip)}
                    onDragEnd={onChipDragEnd}
                    onDragOver={(e) => onDragOverTarget(e, POOL_TARGET)}
                    onDrop={onDropPool}
                    onClick={() => onChipClick(chip)}
                    className={`match-chip inline-flex min-h-[2.5rem] max-w-full items-center rounded-lg border px-3 py-1.5 text-sm font-semibold transition ${
                      selectedChipId === chip.id
                        ? "border-terra bg-[#fff1eb]"
                        : "border-line bg-white hover:border-terra/50"
                    } ${draggingId === chip.id ? "is-dragging" : ""} ${
                      disabled ? "cursor-default opacity-80" : "is-draggable"
                    }`}
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
  const paired = alignMatchPairs(sides.left, parseMatchAnswer(value));
  return sides.left.every((item) => Boolean(paired[item]));
}
