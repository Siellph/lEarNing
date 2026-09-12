import { useEffect, useRef, useState } from "react";
import { Link } from "react-router-dom";
import { getConsent, setConsent, type ConsentChoice } from "../lib/consent";

export function ConsentBanner() {
  const [open, setOpen] = useState(() => getConsent() === null);
  const dialogRef = useRef<HTMLDivElement>(null);
  const acceptRef = useRef<HTMLButtonElement>(null);
  const previousFocus = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (!open) return;
    previousFocus.current = document.activeElement instanceof HTMLElement ? document.activeElement : null;
    const id = window.requestAnimationFrame(() => acceptRef.current?.focus());
    return () => window.cancelAnimationFrame(id);
  }, [open]);

  useEffect(() => {
    if (!open) return;
    const onKey = (event: KeyboardEvent) => {
      if (event.key !== "Tab" || !dialogRef.current) return;
      const focusable = dialogRef.current.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])',
      );
      if (!focusable.length) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [open]);

  const choose = (choice: ConsentChoice) => {
    setConsent(choice);
    setOpen(false);
    previousFocus.current?.focus();
  };

  if (!open) return null;

  return (
    <div className="consent-sheet">
      <div
        ref={dialogRef}
        className="consent-sheet-panel"
        role="dialog"
        aria-modal="true"
        aria-labelledby="consent-title"
        aria-describedby="consent-text"
      >
        <p id="consent-title" className="font-display text-xl text-ink">
          Данные в браузере
        </p>
        <p id="consent-text" className="mt-2 text-sm leading-6 text-ink-soft">
          Рекламных cookie и аналитики нет. Чтобы оставаться в кабинете, в local storage хранится
          токен входа — это нужно для работы сайта. Если примете, запомним ещё темп и акцент
          озвучки.
        </p>
        <div className="mt-4 flex flex-wrap items-center gap-2">
          <button ref={acceptRef} type="button" className="btn btn-primary text-sm" onClick={() => choose("accepted")}>
            Принять
          </button>
          <button type="button" className="btn btn-ghost text-sm" onClick={() => choose("rejected")}>
            Отклонить
          </button>
          <Link to="/privacy" className="px-2 text-sm font-semibold text-terra hover:underline">
            Подробнее
          </Link>
          <Link to="/terms" className="text-sm text-ink-soft hover:text-terra">
            Соглашение
          </Link>
        </div>
      </div>
    </div>
  );
}
