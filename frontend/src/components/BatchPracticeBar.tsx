import { useLayoutEffect, useRef } from "react";

type BatchPracticeBarProps = {
  batchCount: number;
  activeBatch: number | null;
  onSelectBatch: (batch: number) => void;
  onPractice: () => void;
  practiceActive?: boolean;
  busy?: boolean;
  className?: string;
};

/**
 * Batch chips + practice.
 * Mobile: chips centered (scroll if needed), practice full-width below.
 * Desktop: chips left, practice right.
 * Horizontal scroll only — no arrow buttons, scrollbar hidden.
 */
export function BatchPracticeBar({
  batchCount,
  activeBatch,
  onSelectBatch,
  onPractice,
  practiceActive = false,
  busy = false,
  className = "",
}: BatchPracticeBarProps) {
  const batches = Array.from({ length: batchCount }, (_, i) => i + 1);
  const practiceLabel = busy ? "…" : practiceActive ? "Повторить" : "Практика";
  const scrollRef = useRef<HTMLDivElement>(null);

  useLayoutEffect(() => {
    const el = scrollRef.current;
    if (!el || activeBatch == null) return;
    const chip = el.querySelector<HTMLElement>(`[data-batch="${activeBatch}"]`);
    chip?.scrollIntoView({ inline: "nearest", block: "nearest", behavior: "smooth" });
  }, [activeBatch, batchCount]);

  return (
    <div className={`flex min-w-0 flex-col gap-3 sm:flex-row sm:items-center sm:gap-3 ${className}`}>
      <div
        ref={scrollRef}
        className="h-scroll-x min-w-0 w-full flex-1"
        role="group"
        aria-label="Партии"
      >
        <div className="flex w-max min-w-full justify-center gap-1.5 sm:justify-start">
          {batches.map((n) => {
            const active = activeBatch === n;
            return (
              <button
                key={n}
                type="button"
                data-batch={n}
                aria-current={active ? "true" : undefined}
                className={`inline-flex h-8 min-w-8 shrink-0 items-center justify-center rounded-full px-2 text-sm font-semibold transition-colors ${
                  active ? "bg-ink text-paper" : "bg-card text-ink-soft hover:text-ink"
                }`}
                onClick={() => onSelectBatch(n)}
              >
                {n}
              </button>
            );
          })}
        </div>
      </div>

      <div className="flex w-full min-w-0 sm:w-auto sm:shrink-0 sm:justify-end">
        <button
          type="button"
          className="btn btn-primary h-10 w-full px-4 py-0 text-sm shadow-none sm:h-8 sm:w-auto"
          onClick={onPractice}
          disabled={busy}
          title="Тренировать текущую партию"
        >
          {practiceLabel}
        </button>
      </div>
    </div>
  );
}
