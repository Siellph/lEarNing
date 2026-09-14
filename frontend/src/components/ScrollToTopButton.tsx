import { useEffect, useState } from "react";
import { ArrowUp } from "lucide-react";
import { getAppScrollEl } from "../lib/scrollRestore";

const SHOW_AFTER_PX = 320;

/** Floating control: scroll the app main pane back to top. */
export function ScrollToTopButton() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const el = getAppScrollEl();
    if (!el) return;

    const sync = () => setVisible(el.scrollTop > SHOW_AFTER_PX);
    sync();
    el.addEventListener("scroll", sync, { passive: true });
    return () => el.removeEventListener("scroll", sync);
  }, []);

  if (!visible) return null;

  return (
    <button
      type="button"
      className="fixed bottom-5 right-4 z-30 flex size-11 items-center justify-center rounded-full border border-line/80 bg-card text-ink shadow-[0_10px_28px_-12px_rgba(18,32,51,0.45)] transition-colors hover:border-terra hover:text-terra sm:bottom-8 sm:right-8"
      aria-label="Наверх"
      title="Наверх"
      onClick={() => {
        const el = getAppScrollEl();
        el?.scrollTo({ top: 0, behavior: "smooth" });
      }}
    >
      <ArrowUp size={20} strokeWidth={2.25} aria-hidden />
    </button>
  );
}
