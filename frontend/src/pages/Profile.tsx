import { useState } from "react";
import { api } from "../api/client";
import { useAuth } from "../context/AuthContext";

export function Profile() {
  const { user, refresh } = useAuth();
  const [name, setName] = useState(user?.name || "");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const save = async (e: React.FormEvent) => {
    e.preventDefault();
    await api("/auth/me", {
      method: "PATCH",
      body: JSON.stringify({ name, password: password || undefined }),
    });
    setPassword("");
    setMsg("Сохранено");
    refresh();
  };

  return (
    <div className="mx-auto grid max-w-xl gap-6">
      <div>
        <h1 className="font-display text-4xl">Профиль</h1>
        <p className="mt-2 text-ink-soft">Имя, пароль и текущий прогресс аккаунта.</p>
      </div>
      <div className="card grid gap-2 p-5">
        <p>Email: {user?.email}</p>
        <p>Роль: {user?.role === "admin" ? "администратор" : "ученик"}</p>
        <p>Опыт: {user?.xp} XP · серия {user?.streak} дн.</p>
      </div>
      <form className="card grid gap-4 p-5" onSubmit={save}>
        <label className="grid gap-1 text-sm">
          Имя
          <input className="field" value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <label className="grid gap-1 text-sm">
          Новый пароль
          <input className="field" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <button className="btn btn-primary justify-self-start">Сохранить</button>
        {msg && <p className="text-sm text-sage">{msg}</p>}
      </form>
    </div>
  );
}
