import { useLayoutEffect, useRef, useState } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { VoiceControls } from "./SpeakButton";

type BatchPracticeBarProps = {
  batchCount: number;
  activeBatch: number | null;
  onSelectBatch: (batch: number) => void;
  onPractice: () => void;
  practiceActive?: boolean;
  busy?: boolean;
  className?: string;
};

const CHIP_STEP = 40; // ~chip width + gap

/**
 * One row: scrollable batch chips (left) + voice/practice (right).
 * Overflow uses hidden scrollbar + edge chevrons.
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
  const practiceLabel = busy ? "…" : practiceActive ? "Ещё раз" : "Практика";

  const scrollRef = useRef<HTMLDivElement>(null);
  const [canScrollLeft, setCanScrollLeft] = useState(false);
  const [canScrollRight, setCanScrollRight] = useState(false);

  function updateScrollState() {
    const el = scrollRef.current;
    if (!el) return;
    const { scrollLeft, scrollWidth, clientWidth } = el;
    setCanScrollLeft(scrollLeft > 1);
    setCanScrollRight(scrollLeft + clientWidth < scrollWidth - 1);
  }

  useLayoutEffect(() => {
    const el = scrollRef.current;
    if (!el) return;
    updateScrollState();
    const ro = new ResizeObserver(() => updateScrollState());
    ro.observe(el);
    el.addEventListener("scroll", updateScrollState, { passive: true });
    window.addEventListener("resize", updateScrollState);
    return () => {
      ro.disconnect();
      el.removeEventListener("scroll", updateScrollState);
      window.removeEventListener("resize", updateScrollState);
    };
  }, [batchCount]);

  useLayoutEffect(() => {
    const el = scrollRef.current;
    if (!el || activeBatch == null) return;
    const chip = el.querySelector<HTMLElement>(`[data-batch="${activeBatch}"]`);
    chip?.scrollIntoView({ inline: "nearest", block: "nearest", behavior: "smooth" });
    updateScrollState();
  }, [activeBatch, batchCount]);

  function scrollChips(dir: -1 | 1) {
    const el = scrollRef.current;
    if (!el) return;
    const amount = Math.max(CHIP_STEP * 2, Math.round(el.clientWidth * 0.45));
    el.scrollBy({ left: dir * amount, behavior: "smooth" });
  }

  return (
    <div className={`flex items-center gap-3 ${className}`}>
      <div className="relative min-w-0 flex-1">
        {canScrollLeft && (
          <>
            <div
              aria-hidden
              className="pointer-events-none absolute inset-y-0 left-0 z-10 w-9 bg-gradient-to-r from-paper via-paper/90 to-transparent"
            />
            <button
              type="button"
              aria-label="Прокрутить партии влево"
              className="absolute left-0 top-1/2 z-20 flex h-7 w-7 -translate-y-1/2 items-center justify-center rounded-full bg-card/95 text-ink-soft shadow-sm ring-1 ring-line transition-colors hover:text-ink"
              onClick={() => scrollChips(-1)}
            >
              <ChevronLeft size={16} strokeWidth={2.25} />
            </button>
          </>
        )}

        <div
          ref={scrollRef}
          className="flex min-w-0 gap-1.5 overflow-x-auto [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden"
          role="group"
          aria-label="Партии"
        >
          {batches.map((n) => {
            const active = activeBatch === n;
            return (
              <button
                key={n}
                type="button"
                data-batch={n}
                aria-current={active ? "true" : undefined}
                className={`inline-flex h-8 min-w-8 shrink-0 items-center justify-center rounded-full px-2.5 text-sm font-semibold transition-colors ${
                  active ? "bg-ink text-paper" : "bg-card text-ink-soft hover:text-ink"
                }`}
                onClick={() => onSelectBatch(n)}
              >
                {n}
              </button>
            );
          })}
        </div>

        {canScrollRight && (
          <>
            <div
              aria-hidden
              className="pointer-events-none absolute inset-y-0 right-0 z-10 w-9 bg-gradient-to-l from-paper via-paper/90 to-transparent"
            />
            <button
              type="button"
              aria-label="Прокрутить партии вправо"
              className="absolute right-0 top-1/2 z-20 flex h-7 w-7 -translate-y-1/2 items-center justify-center rounded-full bg-card/95 text-ink-soft shadow-sm ring-1 ring-line transition-colors hover:text-ink"
              onClick={() => scrollChips(1)}
            >
              <ChevronRight size={16} strokeWidth={2.25} />
            </button>
          </>
        )}
      </div>

      <div className="flex shrink-0 items-center justify-end gap-2">
        <VoiceControls className="!flex-nowrap" />
        <button
          type="button"
          className="btn btn-primary h-8 shrink-0 px-4 py-0 text-sm shadow-none"
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
