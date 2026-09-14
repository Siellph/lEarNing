import { useEffect, useLayoutEffect, useRef } from "react";
import { useLocation, useSearchParams } from "react-router-dom";
import { SEARCH_HIGHLIGHT_PARAM } from "../lib/searchHighlight";
import {
  beginScrollRestoreGuard,
  getAppScrollEl,
  readAppScroll,
  restoreAppScroll,
  saveAppScroll,
  scrollAppToTop,
} from "../lib/scrollRestore";

/**
 * Keeps scroll position per pathname in the app main scroller.
 *
 * Saves on scroll events (not on route change) so a short next page cannot
 * clamp scrollTop to 0 and wipe the previous page's position.
 */
export function ScrollRestore() {
  const { pathname } = useLocation();
  const [params] = useSearchParams();
  const skipHighlight = Boolean(params.get(SEARCH_HIGHLIGHT_PARAM));
  const pathRef = useRef(pathname);
  pathRef.current = pathname;

  useEffect(() => {
    const el = getAppScrollEl();
    if (!el) return;

    let ticking = false;
    const onScroll = () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        ticking = false;
        saveAppScroll(pathRef.current, el.scrollTop);
      });
    };

    // Save before navigation: route change can clamp scrollTop before we leave.
    const onPointerDown = () => {
      saveAppScroll(pathRef.current, el.scrollTop);
    };

    el.addEventListener("scroll", onScroll, { passive: true });
    el.addEventListener("pointerdown", onPointerDown, true);
    return () => {
      el.removeEventListener("scroll", onScroll);
      el.removeEventListener("pointerdown", onPointerDown, true);
    };
  }, [pathname]);

  useLayoutEffect(() => {
    if (skipHighlight) return;

    const saved = readAppScroll(pathname);
    if (saved == null || saved <= 0) {
      scrollAppToTop();
      return;
    }

    const el = getAppScrollEl();
    if (!el) return;

    beginScrollRestoreGuard(2500);

    let cancelled = false;
    const apply = () => {
      if (cancelled) return;
      restoreAppScroll(saved);
    };

    apply();
    const raf = requestAnimationFrame(apply);
    const ro = new ResizeObserver(() => apply());
    ro.observe(el);

    const stopAt = window.setTimeout(() => ro.disconnect(), 2500);
    const timers = [50, 150, 400, 800, 1500].map((ms) => window.setTimeout(apply, ms));

    return () => {
      cancelled = true;
      cancelAnimationFrame(raf);
      ro.disconnect();
      window.clearTimeout(stopAt);
      timers.forEach((id) => window.clearTimeout(id));
    };
  }, [pathname, skipHighlight]);

  return null;
}
