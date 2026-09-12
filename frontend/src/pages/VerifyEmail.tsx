import { useEffect, useState } from "react";
import { Link, useLocation, useSearchParams } from "react-router-dom";
import { api, ApiError } from "../api/client";
import { AuthShell } from "./Login";

async function resendVerification(email: string) {
  return api<{ message: string }>("/auth/resend-verification", {
    method: "POST",
    body: JSON.stringify({ email }),
  });
}

export function CheckEmail() {
  const location = useLocation();
  const preset = (location.state as { email?: string } | null)?.email ?? "";
  const [email, setEmail] = useState(preset);
  const [info, setInfo] = useState(preset ? "Проверьте почту — мы отправили ссылку для подтверждения." : "");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  const resend = async () => {
    if (!email) {
      setError("Укажите email");
      return;
    }
    setBusy(true);
    setError("");
    try {
      const data = await resendVerification(email);
      setInfo(data.message);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Не удалось отправить письмо");
    } finally {
      setBusy(false);
    }
  };

  return (
    <AuthShell title="Проверьте почту" subtitle="Аккаунт создан, но вход откроется после подтверждения email">
      <div className="grid gap-4">
        <p className="text-sm text-ink-soft">
          Если письма нет во входящих, загляните в спам. В локальной разработке ссылка печатается в логах backend.
        </p>
        <label className="grid gap-1 text-sm">
          Email
          <input className="field" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        {info && <p className="text-sm">{info}</p>}
        {error && <p className="text-sm text-rose">{error}</p>}
        <button className="btn btn-primary" type="button" disabled={busy} onClick={resend}>
          {busy ? "Отправляем…" : "Отправить письмо ещё раз"}
        </button>
        <p className="text-sm text-ink-soft">
          Уже подтвердили? <Link to="/login" className="text-terra">Войти</Link>
        </p>
      </div>
    </AuthShell>
  );
}

export function VerifyEmail() {
  const [params] = useSearchParams();
  const token = params.get("token") ?? "";
  const [status, setStatus] = useState<"pending" | "ok" | "error">(token ? "pending" : "error");
  const [message, setMessage] = useState(token ? "Проверяем ссылку…" : "В ссылке нет токена.");

  useEffect(() => {
    if (!token) return;
    api<{ message: string }>("/auth/verify", {
      method: "POST",
      body: JSON.stringify({ token }),
    })
      .then((data) => {
        setStatus("ok");
        setMessage(data.message);
      })
      .catch((err) => {
        setStatus("error");
        setMessage(err instanceof ApiError || err instanceof Error ? err.message : "Ссылка не сработала");
      });
  }, [token]);

  return (
    <AuthShell title="Подтверждение email" subtitle="Последний шаг перед входом">
      <div className="grid gap-4">
        <p className={status === "error" ? "text-sm text-rose" : "text-sm"}>{message}</p>
        {status === "ok" && (
          <Link to="/login" className="btn btn-primary text-center">
            Войти
          </Link>
        )}
        {status === "error" && (
          <Link to="/check-email" className="btn btn-primary text-center">
            Запросить письмо ещё раз
          </Link>
        )}
      </div>
    </AuthShell>
  );
}
