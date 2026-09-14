/** Persist / restore scroll for the app main scroller (not window). */

const STORAGE_PREFIX = "learning_scroll:";
const memory = new Map<string, number>();

export function getAppScrollEl(): HTMLElement | null {
  return document.querySelector<HTMLElement>("[data-app-scroll]");
}

export function saveAppScroll(pathname: string): void {
  const el = getAppScrollEl();
  if (!el || !pathname) return;
  const y = el.scrollTop;
  memory.set(pathname, y);
  try {
    sessionStorage.setItem(STORAGE_PREFIX + pathname, String(y));
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

export function restoreAppScroll(pathname: string, y: number): void {
  const el = getAppScrollEl();
  if (!el) return;
  el.scrollTop = y;
}

export function scrollAppToTop(): void {
  const el = getAppScrollEl();
  if (el) el.scrollTop = 0;
}
