import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api, ApiError } from "../api/client";
import { BrandMark } from "../components/BrandMark";
import { useAuth } from "../context/AuthContext";

export function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [unverified, setUnverified] = useState(false);
  const [info, setInfo] = useState("");
  const [busy, setBusy] = useState(false);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setBusy(true);
    setError("");
    setInfo("");
    setUnverified(false);
    try {
      const user = await login(email, password);
      navigate(user.role === "admin" ? "/admin" : "/app");
    } catch (err) {
      const message = err instanceof Error ? err.message : "Ошибка входа";
      setError(message);
      setUnverified(err instanceof ApiError && err.status === 403 && message.toLowerCase().includes("email"));
    } finally {
      setBusy(false);
    }
  };

  const resend = async () => {
    setBusy(true);
    setError("");
    try {
      const data = await api<{ message: string }>("/auth/resend-verification", {
        method: "POST",
        body: JSON.stringify({ email }),
      });
      setInfo(data.message);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Не удалось отправить письмо");
    } finally {
      setBusy(false);
    }
  };

  return (
    <AuthShell title="Вход в lEarNing" subtitle="Продолжите путь по грамматике">
      <form className="grid gap-4" onSubmit={submit}>
        <label className="grid gap-1 text-sm">
          Email
          <input className="field" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <label className="grid gap-1 text-sm">
          Пароль
          <input className="field" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </label>
        {error && <p className="text-sm text-rose">{error}</p>}
        {info && <p className="text-sm">{info}</p>}
        {unverified && (
          <button className="btn" type="button" disabled={busy} onClick={resend}>
            Отправить письмо ещё раз
          </button>
        )}
        <button className="btn btn-primary" disabled={busy}>
          {busy ? "Входим…" : "Войти"}
        </button>
        <p className="text-sm text-ink-soft">
          Нет аккаунта? <Link to="/register" className="text-terra">Зарегистрироваться</Link>
        </p>
      </form>
    </AuthShell>
  );
}

export function AuthShell({ title, subtitle, children }: { title: string; subtitle: string; children: React.ReactNode }) {
  return (
    <div className="surface-grid grid min-h-screen place-items-center px-4 py-10">
      <div className="w-full max-w-md">
        <Link to="/" className="inline-block">
          <BrandMark size="md" />
          <p className="mt-1 text-sm text-ink-soft">учим EN</p>
        </Link>
        <div className="card mt-6 p-6 sm:p-8">
          <h1 className="font-display text-3xl">{title}</h1>
          <p className="mb-6 mt-2 text-ink-soft">{subtitle}</p>
          {children}
        </div>
      </div>
    </div>
  );
}
