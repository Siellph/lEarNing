import { BookOpenText, GraduationCap, Home, LogOut, Shield, Sparkles, UserRound, Volume2 } from "lucide-react";
import { NavLink, Outlet } from "react-router-dom";
import { BrandMark } from "./BrandMark";
import { useAuth } from "../context/AuthContext";

const links = [
  { to: "/app", label: "Обзор", icon: Home, end: true },
  { to: "/app/grammar", label: "Грамматика", icon: BookOpenText },
  { to: "/app/sounds", label: "Звуки", icon: Volume2 },
  { to: "/app/vocab", label: "Словарь", icon: Sparkles },
  { to: "/app/exams", label: "Экзамены", icon: GraduationCap },
  { to: "/app/profile", label: "Профиль", icon: UserRound },
];

export function Layout() {
  const { user, logout } = useAuth();

  return (
    <div className="surface-grid flex h-full flex-col">
      <div className="mx-auto flex min-h-0 w-full max-w-7xl flex-1">
        <aside className="hide-sm flex h-full w-64 shrink-0 flex-col border-r border-line/70 px-5 py-6">
          <BrandMark size="md" />
          <p className="mt-1 text-sm text-ink-soft">учим EN</p>
          <nav className="mt-8 grid gap-1">
            {links.map((link) => (
              <NavLink
                key={link.to}
                to={link.to}
                end={link.end}
                className={({ isActive }) =>
                  `flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium ${
                    isActive ? "bg-card text-terra shadow-sm" : "text-ink-soft hover:bg-card/70"
                  }`
                }
              >
                <link.icon size={18} />
                {link.label}
              </NavLink>
            ))}
            {user?.role === "admin" && (
              <NavLink
                to="/admin"
                className="mt-2 flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium text-dusk hover:bg-card/70"
              >
                <Shield size={18} />
                Админ-панель
              </NavLink>
            )}
          </nav>
          <div className="mt-auto rounded-2xl bg-card p-4">
            <p className="font-semibold">{user?.name}</p>
            <p className="text-xs text-ink-soft">{user?.xp} XP · серия {user?.streak}</p>
            <button className="btn btn-ghost mt-3 w-full text-sm" onClick={logout}>
              <LogOut size={16} /> Выйти
            </button>
          </div>
        </aside>
        <div className="flex min-h-0 min-w-0 flex-1 flex-col">
          <header className="flex shrink-0 items-center justify-between border-b border-line/70 px-4 py-3 sm:px-8">
            <BrandMark size="sm" className="sm:hidden" />
            <div className="ml-auto flex items-center gap-3 text-sm text-ink-soft">
              <span className="rounded-full bg-card px-3 py-1">{user?.xp ?? 0} XP</span>
              <span className="rounded-full bg-card px-3 py-1">🔥 {user?.streak ?? 0}</span>
            </div>
          </header>
          <main className="min-h-0 flex-1 overflow-y-auto px-4 py-[clamp(0.45rem,1.2vh,1.25rem)] sm:px-8">
            <Outlet />
          </main>
          <nav className="sticky bottom-0 grid shrink-0 grid-cols-6 border-t border-line bg-paper/95 px-1 py-2 backdrop-blur sm:hidden">
            {links.map((link) => (
              <NavLink
                key={link.to}
                to={link.to}
                end={link.end}
                className={({ isActive }) =>
                  `flex flex-col items-center gap-1 py-1 text-[11px] ${isActive ? "text-terra" : "text-ink-soft"}`
                }
              >
                <link.icon size={18} />
                {link.label}
              </NavLink>
            ))}
          </nav>
        </div>
      </div>
    </div>
  );
}
