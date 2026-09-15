import {
  AlertTriangle,
  BookOpen,
  BookOpenText,
  CircleHelp,
  GraduationCap,
  Headphones,
  Home,
  LogOut,
  Menu,
  MessagesSquare,
  MessageSquareQuote,
  Shield,
  Sparkles,
  UserRound,
  Volume2,
  WholeWord,
  X,
} from "lucide-react";
import { useEffect, useId, useRef, useState } from "react";
import { NavLink } from "react-router-dom";
import { BrandMark } from "./BrandMark";
import { DonationBanner } from "./DonationBanner";
import { GlobalSearch } from "./GlobalSearch";
import { PageEnter } from "./PageEnter";
import { ScrollRestore } from "./ScrollRestore";
import { ScrollToTopButton } from "./ScrollToTopButton";
import { VoiceSettingsMenu } from "./SpeakButton";
import { useAuth } from "../context/AuthContext";

const desktopLinks = [
  { to: "/app", label: "Обзор", icon: Home, end: true },
  { to: "/app/grammar", label: "Грамматика", icon: BookOpenText },
  { to: "/app/sounds", label: "Звуки", icon: Volume2 },
  { to: "/app/vocab", label: "Словарь", icon: Sparkles },
  { to: "/app/verbs", label: "Глаголы", icon: WholeWord },
  { to: "/app/idioms", label: "Идиомы", icon: MessageSquareQuote },
  { to: "/app/exceptions", label: "Исключения", icon: AlertTriangle },
  { to: "/app/reading", label: "Чтение", icon: BookOpen },
  { to: "/app/listening", label: "Аудирование", icon: Headphones },
  { to: "/app/dialogues", label: "Диалоги", icon: MessagesSquare },
  { to: "/app/exams", label: "Экзамены", icon: GraduationCap },
  { to: "/app/help", label: "Справка", icon: CircleHelp },
  { to: "/app/profile", label: "Профиль", icon: UserRound },
];

function navClass({ isActive }: { isActive: boolean }) {
  return `nav-item flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium ${
    isActive ? "bg-card text-terra shadow-sm" : "text-ink-soft hover:bg-card/70"
  }`;
}

export function Layout() {
  const { user, logout } = useAuth();
  const isAdmin = user?.role === "admin";
  const [drawerOpen, setDrawerOpen] = useState(false);
  const drawerTitleId = useId();
  const openBtnRef = useRef<HTMLButtonElement>(null);
  const closeBtnRef = useRef<HTMLButtonElement>(null);

  const closeDrawer = () => setDrawerOpen(false);

  useEffect(() => {
    if (!drawerOpen) return;

    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    closeBtnRef.current?.focus();

    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") closeDrawer();
    };
    window.addEventListener("keydown", onKeyDown);

    return () => {
      document.body.style.overflow = prevOverflow;
      window.removeEventListener("keydown", onKeyDown);
      openBtnRef.current?.focus();
    };
  }, [drawerOpen]);

  useEffect(() => {
    const mq = window.matchMedia("(min-width: 721px)");
    const onChange = () => {
      if (mq.matches) setDrawerOpen(false);
    };
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, []);

  const renderNav = (onNavigate?: () => void) => (
    <>
      {desktopLinks.map((link) => (
        <NavLink
          key={link.to}
          to={link.to}
          end={link.end}
          className={navClass}
          onClick={onNavigate}
        >
          <link.icon size={18} />
          {link.label}
        </NavLink>
      ))}
      {isAdmin && (
        <NavLink
          to="/admin"
          className="mt-2 flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium text-dusk hover:bg-card/70"
          onClick={onNavigate}
        >
          <Shield size={18} />
          Админ-панель
        </NavLink>
      )}
    </>
  );

  return (
    <div className="surface-grid flex h-dvh flex-col">
      <DonationBanner />
      <div className="mx-auto flex min-h-0 w-full max-w-7xl flex-1">
        <aside className="hide-sm flex h-full w-64 shrink-0 flex-col border-r border-line/70 px-5 py-6">
          <BrandMark size="md" />
          <p className="mt-1 text-sm text-ink-soft">учим ENG</p>
          <nav className="mt-8 grid gap-1 overflow-y-auto">{renderNav()}</nav>
          <div className="mt-auto rounded-2xl bg-card p-4">
            <p className="font-semibold">{user?.name}</p>
            <p className="text-xs text-ink-soft">
              {user?.xp} XP · серия {user?.streak}
            </p>
            <button className="btn btn-ghost mt-3 w-full text-sm" onClick={logout}>
              <LogOut size={16} /> Выйти
            </button>
          </div>
        </aside>

        <div className="flex min-h-0 min-w-0 flex-1 flex-col">
          <header className="flex shrink-0 items-center justify-between gap-3 border-b border-line/70 px-4 py-3 sm:px-8">
            <div className="flex min-w-0 items-center gap-2">
              <button
                ref={openBtnRef}
                type="button"
                className="hidden size-10 shrink-0 items-center justify-center rounded-xl border border-line/80 bg-card text-ink shadow-sm hover:bg-paper-2 max-[720px]:inline-flex"
                aria-label="Открыть меню"
                aria-expanded={drawerOpen}
                aria-controls="mobile-nav-drawer"
                onClick={() => setDrawerOpen(true)}
              >
                <Menu size={20} />
              </button>
              <BrandMark size="sm" className="sm:hidden" />
            </div>
            <div className="ml-auto flex items-center gap-2 text-sm text-ink-soft sm:gap-3">
              <GlobalSearch />
              <VoiceSettingsMenu />
              <span className="inline-flex items-center justify-center rounded-full bg-card px-3 py-1">
                {user?.xp ?? 0} XP
              </span>
              <span className="inline-flex items-center justify-center rounded-full bg-card px-3 py-1">
                🔥 {user?.streak ?? 0}
              </span>
            </div>
          </header>
          <main
            data-app-scroll
            className="min-h-0 min-w-0 flex-1 overflow-x-hidden overflow-y-auto px-4 py-[clamp(0.45rem,1.2vh,1.25rem)] sm:px-8"
          >
            <ScrollRestore />
            <PageEnter />
          </main>
          <ScrollToTopButton />
        </div>
      </div>

      {/* Mobile drawer — only relevant below hide-sm breakpoint */}
      <div
        className={`drawer-backdrop fixed inset-0 z-40 hidden bg-ink/35 max-[720px]:block ${
          drawerOpen ? "opacity-100" : "pointer-events-none opacity-0"
        }`}
        aria-hidden={!drawerOpen}
        onClick={closeDrawer}
      />
      <div
        id="mobile-nav-drawer"
        role="dialog"
        aria-modal="true"
        aria-labelledby={drawerTitleId}
        aria-hidden={!drawerOpen}
        inert={!drawerOpen ? true : undefined}
        className={`drawer-panel fixed inset-y-0 left-0 z-50 hidden w-[min(17.5rem,88vw)] flex-col border-r border-line/70 bg-paper shadow-[4px_0_24px_rgba(18,32,51,0.12)] max-[720px]:flex ${
          drawerOpen ? "translate-x-0" : "pointer-events-none -translate-x-full"
        }`}
      >
        <div className="flex items-start justify-between gap-3 border-b border-line/70 px-5 py-4">
          <div>
            <BrandMark size="md" />
            <p id={drawerTitleId} className="mt-1 text-sm text-ink-soft">
              учим ENG
            </p>
          </div>
          <button
            ref={closeBtnRef}
            type="button"
            className="inline-flex size-10 shrink-0 items-center justify-center rounded-xl border border-line/80 bg-card text-ink hover:bg-paper-2"
            aria-label="Закрыть меню"
            onClick={closeDrawer}
          >
            <X size={18} />
          </button>
        </div>
        <nav className="grid flex-1 gap-1 overflow-y-auto px-3 py-4">{renderNav(closeDrawer)}</nav>
        <div className="border-t border-line/70 p-4">
          <div className="rounded-2xl bg-card p-4">
            <p className="font-semibold">{user?.name}</p>
            <p className="text-xs text-ink-soft">
              {user?.xp} XP · серия {user?.streak}
            </p>
            <button
              className="btn btn-ghost mt-3 w-full text-sm"
              onClick={() => {
                closeDrawer();
                logout();
              }}
            >
              <LogOut size={16} /> Выйти
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
