/** Persist / restore scroll for the app main scroller (not window). */

const STORAGE_PREFIX = "learning_scroll:";
const memory = new Map<string, number>();

let restoreGuardUntil = 0;

export function getAppScrollEl(): HTMLElement | null {
  return document.querySelector<HTMLElement>("[data-app-scroll]");
}

export function beginScrollRestoreGuard(ms = 2000): void {
  restoreGuardUntil = Date.now() + ms;
}

export function saveAppScroll(pathname: string, y?: number): void {
  const el = getAppScrollEl();
  if (!pathname) return;
  const next = y ?? el?.scrollTop;
  if (next == null || !Number.isFinite(next)) return;

  // While restoring, the browser may clamp scrollTop on short loading content.
  // Don't let that wipe a taller saved position for this path.
  const prev = memory.get(pathname);
  if (Date.now() < restoreGuardUntil && prev != null && prev > next + 8) {
    return;
  }

  memory.set(pathname, next);
  try {
    sessionStorage.setItem(STORAGE_PREFIX + pathname, String(next));
  } catch {
    /* private mode / quota */
  }
}

export function readAppScroll(pathname: string): number | null {
  if (memory.has(pathname)) return memory.get(pathname)!;
  try {
    const raw = sessionStorage.getItem(STORAGE_PREFIX + pathname);
    if (raw == null) return null;
    const y = Number(raw);
    return Number.isFinite(y) ? y : null;
  } catch {
    return null;
  }
}

export function restoreAppScroll(y: number): void {
  const el = getAppScrollEl();
  if (!el) return;
  el.scrollTop = y;
}

export function scrollAppToTop(): void {
  const el = getAppScrollEl();
  if (el) el.scrollTop = 0;
}
