import { Heart } from "lucide-react";
import { useEffect, useLayoutEffect, useRef, useState } from "react";

type Banner = {
  enabled: boolean;
  title?: string;
  message?: string;
  url?: string;
  button?: string;
};

export function DonationBanner() {
  const [banner, setBanner] = useState<Banner | null>(null);
  const [height, setHeight] = useState(0);
  const barRef = useRef<HTMLElement>(null);

  useEffect(() => {
    fetch("/api/public/donation")
      .then((res) => (res.ok ? res.json() : { enabled: false }))
      .then((data) => setBanner(data))
      .catch(() => setBanner({ enabled: false }));
  }, []);

  const visible = Boolean(banner?.enabled && banner.url);

  useLayoutEffect(() => {
    if (!visible) {
      setHeight(0);
      return;
    }
    const el = barRef.current;
    if (!el) return;
    const update = () => setHeight(el.getBoundingClientRect().height);
    update();
    const ro = new ResizeObserver(update);
    ro.observe(el);
    return () => ro.disconnect();
  }, [visible, banner?.title, banner?.message, banner?.button]);

  if (!visible || !banner) return null;

  return (
    <>
      <div className="donate-bar-spacer" style={{ height }} aria-hidden />
      <aside className="donate-bar" ref={barRef}>
        <Heart size={18} className="shrink-0" />
        <div className="min-w-0 flex-1">
          <p className="font-semibold">{banner.title}</p>
          <p className="text-sm opacity-90">{banner.message}</p>
        </div>
        <a className="btn btn-primary shrink-0 text-sm" href={banner.url} target="_blank" rel="noreferrer">
          {banner.button || "Оставить чаевые"}
        </a>
      </aside>
    </>
  );
}
