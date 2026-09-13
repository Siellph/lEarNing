import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { AuthShell } from "./Login";

export function Register() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [accepted, setAccepted] = useState(false);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!accepted) {
      setError("Чтобы создать аккаунт, примите Пользовательское соглашение и Политику конфиденциальности");
      return;
    }
    setBusy(true);
    setError("");
    try {
      const result = await register(name, email, password, true);
      if (result.user) {
        navigate(result.user.role === "admin" ? "/admin" : "/app");
        return;
      }
      if (result.message && result.message.includes("без подтверждения")) {
        navigate("/login", { state: { email: result.email || email, notice: result.message } });
        return;
      }
      navigate("/check-email", { state: { email: result.email || email } });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Ошибка регистрации");
    } finally {
      setBusy(false);
    }
  };

  return (
    <AuthShell title="Регистрация" subtitle="Начните с уровня A1 и двигайтесь вверх">
      <form className="grid gap-4" onSubmit={submit}>
        <label className="grid gap-1 text-sm">
          Имя
          <input className="field" value={name} onChange={(e) => setName(e.target.value)} required minLength={2} />
        </label>
        <label className="grid gap-1 text-sm">
          Email
          <input className="field" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <label className="grid gap-1 text-sm">
          Пароль
          <input className="field" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required minLength={6} />
        </label>
        <label className="flex items-start gap-3 text-sm leading-6 text-ink-soft">
          <input
            type="checkbox"
            className="mt-1 h-4 w-4 shrink-0 accent-terra"
            checked={accepted}
            onChange={(e) => {
              setAccepted(e.target.checked);
              if (e.target.checked) setError("");
            }}
          />
          <span>
            Я принимаю{" "}
            <Link to="/terms" className="text-terra" target="_blank" rel="noreferrer">
              Пользовательское соглашение
            </Link>{" "}
            и{" "}
            <Link to="/privacy" className="text-terra" target="_blank" rel="noreferrer">
              Политику конфиденциальности
            </Link>
          </span>
        </label>
        {error && <p className="text-sm text-rose">{error}</p>}
        <button className="btn btn-primary" disabled={busy || !accepted}>
          {busy ? "Создаём…" : "Создать аккаунт"}
        </button>
        <p className="text-sm text-ink-soft">
          Уже есть аккаунт? <Link to="/login" className="text-terra">Войти</Link>
        </p>
      </form>
    </AuthShell>
  );
}
