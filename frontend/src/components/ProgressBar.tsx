export function ProgressBar({ value, label }: { value: number; label?: string }) {
  const safe = Math.max(0, Math.min(100, Math.round(value)));
  return (
    <div className="w-full">
      {label && (
        <div className="mb-1 flex justify-between text-xs text-ink-soft">
          <span>{label}</span>
          <span>{safe}%</span>
        </div>
      )}
      <div className="h-2 overflow-hidden rounded-full bg-paper-2">
        <div
          className="h-full rounded-full bg-sage transition-all duration-500"
          style={{ width: `${safe}%` }}
        />
      </div>
    </div>
  );
}
