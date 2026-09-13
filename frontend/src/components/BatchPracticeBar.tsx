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

/**
 * Stable toolbar: batch chips wrap only in the left zone;
 * Practice stays pinned (top-right on desktop, full-width row on mobile).
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

  return (
    <div
      className={`grid grid-cols-1 items-start gap-3 sm:grid-cols-[minmax(0,1fr)_auto] ${className}`}
    >
      <div className="flex min-w-0 flex-wrap gap-1.5" role="group" aria-label="Партии">
        {batches.map((n) => {
          const active = activeBatch === n;
          return (
            <button
              key={n}
              type="button"
              aria-current={active ? "true" : undefined}
              className={`inline-flex h-8 min-w-8 items-center justify-center rounded-full px-2.5 text-sm font-semibold transition-colors ${
                active ? "bg-ink text-paper" : "bg-card text-ink-soft hover:text-ink"
              }`}
              onClick={() => onSelectBatch(n)}
            >
              {n}
            </button>
          );
        })}
      </div>

      <div className="flex shrink-0 flex-col gap-2 sm:flex-row sm:items-center sm:justify-end">
        <VoiceControls />
        <button
          type="button"
          className="btn btn-primary h-9 w-full shrink-0 px-4 py-0 text-sm shadow-none sm:h-8 sm:w-auto"
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
