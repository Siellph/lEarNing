import { useEffect, useRef } from "react";
import { useSearchParams } from "react-router-dom";
import { getAppScrollEl, clearAppScroll } from "../lib/scrollRestore";

export const SEARCH_HIGHLIGHT_PARAM = "highlight";
const HIGHLIGHT_MS = 2800;
const HIGHLIGHT_CLASS = "search-highlight-pulse";

function escapeAttr(value: string) {
  if (typeof CSS !== "undefined" && typeof CSS.escape === "function") {
    return CSS.escape(value);
  }
  return value.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
}

/** Scroll to `[data-search-id]` and pulse border for ~2–3s. */
export function applySearchHighlight(id: string): () => void {
  const el = document.querySelector<HTMLElement>(`[data-search-id="${escapeAttr(id)}"]`);
  if (!el) return () => {};

  el.scrollIntoView({ behavior: "smooth", block: "center" });
  el.classList.add(HIGHLIGHT_CLASS);

  const timer = window.setTimeout(() => {
    el.classList.remove(HIGHLIGHT_CLASS);
  }, HIGHLIGHT_MS);

  return () => {
    window.clearTimeout(timer);
    el.classList.remove(HIGHLIGHT_CLASS);
  };
}

/**
 * When `ready`, read `?highlight=` from the URL, scroll/pulse the matching card,
 * then strip the param (keeps other query keys like `batch`).
 */
export function useSearchHighlight(ready = true) {
  const [params, setParams] = useSearchParams();
  const highlight = params.get(SEARCH_HIGHLIGHT_PARAM);
  const applied = useRef<string | null>(null);

  useEffect(() => {
    if (!ready || !highlight) {
      if (!highlight) applied.current = null;
      return;
    }
    if (applied.current === highlight) return;

    let attempts = 0;
    let cancelled = false;
    const retryTimers: number[] = [];

    const tick = () => {
      if (cancelled) return;

      const targetEl = document.querySelector<HTMLElement>(
        `[data-search-id="${escapeAttr(highlight)}"]`
      );
      const container = getAppScrollEl() || document.documentElement;

      if (targetEl && container) {
        applied.current = highlight;

        clearAppScroll(window.location.pathname);

        // 1. Временно добавляем padding снизу, чтобы элементы на самом дне могли встать строго в центр
        const originalPaddingBottom = container.style.paddingBottom;
        container.style.paddingBottom = `${container.clientHeight / 2}px`;

        const scrollStep = () => {
          if (cancelled) return;

          const containerRect = container.getBoundingClientRect();
          const targetRect = targetEl.getBoundingClientRect();

          // Формула точной прокрутки элемента в центр контейнера
          const targetTop =
            targetRect.top -
            containerRect.top +
            container.scrollTop -
            (containerRect.height / 2 - targetRect.height / 2);

          container.scrollTo({
            top: Math.max(0, targetTop),
            behavior: "smooth",
          });

          targetEl.classList.add(HIGHLIGHT_CLASS);
        };

        // 2. Делаем два захода скролла:
        // Первичный - сразу
        requestAnimationFrame(scrollStep);
        // Корректирующий - через 120мс (когда layout точно полностью посчитан)
        const adjustTimer = window.setTimeout(scrollStep, 120);
        retryTimers.push(adjustTimer);

        // 3. Через 1 секунду (когда плавный скролл гарантированно закончился) — аккуратно возвращаем всё назад
        const cleanupTimer = window.setTimeout(() => {
          container.style.paddingBottom = originalPaddingBottom;
        }, 1000);
        retryTimers.push(cleanupTimer);

        // 4. Снимаем класс подсветки
        const highlightTimer = window.setTimeout(() => {
          targetEl.classList.remove(HIGHLIGHT_CLASS);
        }, HIGHLIGHT_MS);
        retryTimers.push(highlightTimer);

        // 5. Очищаем URL
        const urlTimer = window.setTimeout(() => {
          setParams(
            (prev) => {
              const next = new URLSearchParams(prev);
              next.delete(SEARCH_HIGHLIGHT_PARAM);
              return next;
            },
            { replace: true }
          );
        }, 600);
        retryTimers.push(urlTimer);

        return;
      }

      attempts += 1;
      if (attempts < 40) {
        retryTimers.push(window.setTimeout(tick, 50));
      }
    };

    const initialTimer = window.setTimeout(tick, 100);

    return () => {
      cancelled = true;
      window.clearTimeout(initialTimer);
      for (const id of retryTimers) window.clearTimeout(id);
    };
  }, [ready, highlight, setParams]);
}

// export function useSearchHighlight(ready = true) {
//   const [params, setParams] = useSearchParams();
//   const highlight = params.get(SEARCH_HIGHLIGHT_PARAM);
//   const applied = useRef<string | null>(null);

//   useEffect(() => {
//     if (!ready || !highlight) {
//       if (!highlight) applied.current = null;
//       return;
//     }
//     if (applied.current === highlight) return;

//     let attempts = 0;
//     let cancelled = false;
//     const retryTimers: number[] = [];

//     const tick = () => {
//       if (cancelled) return;
//       const el = document.querySelector<HTMLElement>(`[data-search-id="${escapeAttr(highlight)}"]`);
//       if (el) {
//         applied.current = highlight;
//         el.scrollIntoView({ behavior: "smooth", block: "center" });
//         el.classList.add(HIGHLIGHT_CLASS);
//         // Keep pulse alive after URL cleanup re-runs this effect.
//         window.setTimeout(() => {
//           el.classList.remove(HIGHLIGHT_CLASS);
//         }, HIGHLIGHT_MS);

//         setParams(
//           (prev) => {
//             const next = new URLSearchParams(prev);
//             next.delete(SEARCH_HIGHLIGHT_PARAM);
//             return next;
//           },
//           { replace: true },
//         );
//         return;
//       }
//       attempts += 1;
//       if (attempts < 24) {
//         retryTimers.push(window.setTimeout(tick, 40));
//       }
//     };

//     const frame = window.requestAnimationFrame(tick);
//     return () => {
//       cancelled = true;
//       window.cancelAnimationFrame(frame);
//       for (const id of retryTimers) window.clearTimeout(id);
//     };
//   }, [ready, highlight, setParams]);
// }