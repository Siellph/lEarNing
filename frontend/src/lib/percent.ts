/** Whole-number percent for progress UI (avoids float artifacts like 56.00000000000001). */
export function percent(done: number, total: number): number {
  return total > 0 ? Math.round((done / total) * 100) : 0;
}
