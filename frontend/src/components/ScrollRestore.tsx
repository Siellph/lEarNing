import { useLayoutEffect, useRef } from "react";
import { useLocation, useSearchParams } from "react-router-dom";
import { SEARCH_HIGHLIGHT_PARAM } from "../lib/searchHighlight";
import {
  readAppScroll,
  restoreAppScroll,
  saveAppScroll,
  scrollAppToTop,
} from "../lib/scrollRestore";

/**
 * Keeps scroll position per pathname in the app main scroller so «Назад»
 * returns to the same place on the list/hub page.
 */
export function ScrollRestore() {
  const { pathname } = useLocation();
  const [params] = useSearchParams();
  const prevPath = useRef(pathname);
  const skipHighlight = Boolean(params.get(SEARCH_HIGHLIGHT_PARAM));

  useLayoutEffect(() => {
    const prev = prevPath.current;
    if (prev !== pathname) {
      saveAppScroll(prev);
      prevPath.current = pathname;
    }

    // Deep-link highlight owns scroll when present.
    if (skipHighlight) return;

    const saved = readAppScroll(pathname);
    if (saved == null) {
      scrollAppToTop();
      return;
    }

    const apply = () => restoreAppScroll(pathname, saved);
    apply();
    const raf = requestAnimationFrame(apply);
    const t1 = window.setTimeout(apply, 50);
    const t2 = window.setTimeout(apply, 200);
    const t3 = window.setTimeout(apply, 450);
    return () => {
      cancelAnimationFrame(raf);
      window.clearTimeout(t1);
      window.clearTimeout(t2);
      window.clearTimeout(t3);
    };
  }, [pathname, skipHighlight]);

  return null;
}
