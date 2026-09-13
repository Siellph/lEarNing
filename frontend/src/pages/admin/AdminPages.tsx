import { useEffect, useRef, useState } from "react";
import { Link, NavLink, Outlet, useParams } from "react-router-dom";
import { api } from "../../api/client";
import { BrandMark } from "../../components/BrandMark";
import { useAuth } from "../../context/AuthContext";

export function AdminLayout() {
  const { user, logout } = useAuth();
  const tabs = [
    ["/admin", "Сводка", true],
    ["/admin/users", "Пользователи", false],
    ["/admin/modules", "Модули", false],
    ["/admin/vocab", "Словарь", false],
    ["/admin/study", "Колоды", false],
    ["/admin/skills", "Навыки", false],
    ["/admin/exams", "Экзамены", false],
    ["/admin/donation", "Настройки", false],
  ] as const;

  return (
    <div className="surface-grid min-h-screen">
      <header className="border-b border-line/70 px-4 py-4 sm:px-8">
        <div className="mx-auto flex max-w-6xl flex-wrap items-center justify-between gap-3">
          <div>
            <BrandMark size="md" />
            <p className="text-sm text-ink-soft">админ · {user?.email}</p>
          </div>
          <div className="flex gap-2">
            <Link to="/app" className="btn btn-ghost text-sm">
              Кабинет ученика
            </Link>
            <button className="btn btn-ghost text-sm" onClick={logout}>
              Выйти
            </button>
          </div>
        </div>
        <nav className="mx-auto mt-4 flex max-w-6xl gap-2 overflow-x-auto pb-1">
          {tabs.map(([to, label, end]) => (
            <NavLink
              key={to}
              to={to}
              end={end}
              className={({ isActive }) =>
                `whitespace-nowrap rounded-full px-4 py-2 text-sm ${isActive ? "bg-ink text-paper" : "bg-card text-ink-soft"}`
              }
            >
              {label}
            </NavLink>
          ))}
        </nav>
      </header>
      <main className="mx-auto max-w-6xl px-4 py-8 sm:px-8">
        <Outlet />
      </main>
    </div>
  );
}

export function AdminDashboard() {
  const [stats, setStats] = useState<Record<string, number> | null>(null);
  useEffect(() => {
    api("/admin/stats").then(setStats);
  }, []);
  if (!stats) return <p>Загружаем сводку…</p>;
  const items = [
    ["Пользователи", stats.users],
    ["Ученики", stats.students],
    ["Модули", stats.modules],
    ["Упражнения", stats.exercises],
    ["Экзамены", stats.exams],
    ["Слова", stats.vocab_words],
    ["Карточки колод", stats.study_cards],
    ["Материалы навыков", stats.skill_items],
    ["Попытки практики", stats.practice_attempts],
    ["Попытки тестов", stats.test_attempts],
  ];
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {items.map(([title, value]) => (
        <div key={title} className="card p-5">
          <p className="text-sm text-ink-soft">{title}</p>
          <p className="font-display mt-2 text-3xl">{value}</p>
        </div>
      ))}
    </div>
  );
}

export function AdminUsers() {
  const [users, setUsers] = useState<
    {
      id: number;
      email: string;
      name: string;
      role: string;
      is_active: boolean;
      email_verified: boolean;
      xp: number;
      streak: number;
    }[]
  >([]);
  useEffect(() => {
    api("/admin/users").then(setUsers);
  }, []);

  const patch = async (id: number, body: object) => {
    await api(`/admin/users/${id}`, { method: "PATCH", body: JSON.stringify(body) });
    api("/admin/users").then(setUsers);
  };

  const activate = async (id: number) => {
    await api(`/admin/users/${id}/activate`, { method: "POST" });
    api("/admin/users").then(setUsers);
  };

  return (
    <div className="grid gap-4">
      <div>
        <h1 className="font-display text-3xl">Пользователи</h1>
        <p className="mt-1 text-sm text-ink-soft">
          «Активировать» подтверждает email без письма — удобно, если SMTP на VPS недоступен.
        </p>
      </div>
      <div className="grid gap-3">
        {users.map((u) => (
          <article key={u.id} className="card grid gap-3 p-4 sm:grid-cols-[1fr_auto] sm:items-center">
            <div className="min-w-0">
              <div className="flex flex-wrap items-center gap-2">
                <p className="font-semibold">{u.name}</p>
                <span className="rounded-full bg-paper-2 px-2 py-0.5 text-xs text-ink-soft">{u.role}</span>
                {!u.is_active && <span className="rounded-full bg-rose/15 px-2 py-0.5 text-xs text-rose">отключён</span>}
                <span
                  className={`rounded-full px-2 py-0.5 text-xs ${
                    u.email_verified ? "bg-sage-soft text-sage" : "bg-[#fff1eb] text-terra"
                  }`}
                >
                  {u.email_verified ? "email подтверждён" : "email не подтверждён"}
                </span>
              </div>
              <p className="mt-1 truncate text-sm text-ink-soft">{u.email}</p>
              <p className="mt-2 text-sm">
                <span className="font-semibold text-terra">{u.xp} XP</span>
                <span className="text-ink-soft"> · серия {u.streak}</span>
              </p>
            </div>
            <div className="flex flex-wrap items-center gap-2">
              <select className="field !w-auto !py-1.5 text-sm" value={u.role} onChange={(e) => patch(u.id, { role: e.target.value })}>
                <option value="student">ученик</option>
                <option value="admin">админ</option>
              </select>
              <button className="btn btn-ghost text-xs" onClick={() => patch(u.id, { is_active: !u.is_active })}>
                {u.is_active ? "Отключить" : "Включить"}
              </button>
              {!u.email_verified && (
                <button className="btn btn-sage text-xs" onClick={() => activate(u.id)}>
                  Активировать
                </button>
              )}
            </div>
          </article>
        ))}
      </div>
    </div>
  );
}

export function AdminModules() {
  const [modules, setModules] = useState<
    { id: number; slug: string; title: string; description: string; level_code: string; exercise_count: number; lesson_count: number }[]
  >([]);
  const [levels, setLevels] = useState<{ id: number; code: string; title: string }[]>([]);
  const [form, setForm] = useState({ level_id: 1, slug: "", title: "", description: "", sort_order: 99, estimated_minutes: 20 });

  const load = () => api("/admin/modules").then(setModules);
  useEffect(() => {
    load();
    api("/admin/levels").then(setLevels);
  }, []);

  const create = async (e: React.FormEvent) => {
    e.preventDefault();
    await api("/admin/modules", { method: "POST", body: JSON.stringify({ ...form, sources: [] }) });
    setForm({ ...form, slug: "", title: "", description: "" });
    load();
  };

  return (
    <div className="grid gap-6">
      <form className="card grid gap-3 p-5 md:grid-cols-2" onSubmit={create}>
        <h2 className="font-display text-2xl md:col-span-2">Новый модуль</h2>
        <select className="field" value={form.level_id} onChange={(e) => setForm({ ...form, level_id: Number(e.target.value) })}>
          {levels.map((l) => (
            <option key={l.id} value={l.id}>
              {l.code}
            </option>
          ))}
        </select>
        <input className="field" placeholder="slug" value={form.slug} onChange={(e) => setForm({ ...form, slug: e.target.value })} required />
        <input className="field" placeholder="Название" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} required />
        <input className="field" placeholder="Описание" value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} required />
        <button className="btn btn-primary justify-self-start">Добавить</button>
      </form>
      <div className="grid gap-3">
        {modules.map((m) => (
          <div key={m.id} className="card flex flex-wrap items-center justify-between gap-3 p-4">
            <div>
              <p className="text-xs text-terra">{m.level_code}</p>
              <p className="font-semibold">{m.title}</p>
              <p className="text-sm text-ink-soft">
                {m.slug} · уроков {m.lesson_count} · упражнений {m.exercise_count}
              </p>
            </div>
            <div className="flex gap-2">
              <Link to={`/admin/modules/${m.id}`} className="btn btn-ghost text-sm">
                Содержание
              </Link>
              <button
                className="btn btn-ghost text-sm"
                onClick={async () => {
                  if (confirm("Удалить модуль?")) {
                    await api(`/admin/modules/${m.id}`, { method: "DELETE" });
                    load();
                  }
                }}
              >
                Удалить
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

type ContentItem = {
  id: number;
  kind: string;
  prompt: string;
  answer: string;
  options?: string[] | { left: string[]; right: string[] } | null;
  accepted?: string[] | null;
  explanation?: string;
};

function optionsEditValue(options: ContentItem["options"]): string {
  if (!options) return "";
  if (Array.isArray(options)) return options.join(" | ");
  const left = options.left || [];
  const right = options.right || [];
  return [...left, "=>", ...right].join(" | ");
}

function parseOptionsEdit(value: string): string[] | { left: string[]; right: string[] } | null {
  const parts = value
    .split("|")
    .map((s) => s.trim())
    .filter(Boolean);
  if (!parts.length) return null;
  const sep = parts.indexOf("=>");
  if (sep >= 0) {
    return { left: parts.slice(0, sep), right: parts.slice(sep + 1) };
  }
  return parts;
}

export function AdminModuleContent() {
  const { moduleId } = useParams();
  const id = Number(moduleId);
  const [data, setData] = useState<{
    module: { id: number; title: string; slug: string };
    lessons: { id: number; title: string }[];
    exercises: ContentItem[];
    test: { id: number; title: string; questions: ContentItem[] } | null;
  } | null>(null);
  const [ex, setEx] = useState({ kind: "fill_blank", prompt: "", answer: "", explanation: "Проверьте форму.", options: "" });
  const [tq, setTq] = useState({ kind: "fill_blank", prompt: "", answer: "", explanation: "Проверьте форму.", options: "" });
  const [editEx, setEditEx] = useState<ContentItem | null>(null);
  const [editTq, setEditTq] = useState<ContentItem | null>(null);

  const load = () => api(`/admin/modules/${id}/content`).then(setData);
  useEffect(() => {
    load();
  }, [id]);

  if (!data) return <p>Загружаем…</p>;

  const kindSelect = (value: string, onChange: (v: string) => void) => (
    <select className="field" value={value} onChange={(e) => onChange(e.target.value)}>
      <option value="multiple_choice">Выбор</option>
      <option value="fill_blank">Пропуск</option>
      <option value="transform">Преобразование</option>
      <option value="error_correction">Исправление</option>
      <option value="order">Порядок слов</option>
      <option value="match">Соотнесение</option>
    </select>
  );

  return (
    <div className="grid gap-6">
      <div>
        <Link to="/admin/modules" className="text-sm text-terra">
          ← Модули
        </Link>
        <h1 className="font-display mt-2 text-3xl">{data.module.title}</h1>
      </div>
      <section className="card p-5">
        <h2 className="font-semibold">Уроки</h2>
        <ul className="mt-3 grid gap-2 text-sm">
          {data.lessons.map((l) => (
            <li key={l.id} className="flex justify-between gap-3">
              {l.title}
              <button
                className="text-rose"
                onClick={async () => {
                  await api(`/admin/lessons/${l.id}`, { method: "DELETE" });
                  load();
                }}
              >
                удалить
              </button>
            </li>
          ))}
        </ul>
      </section>
      <form
        className="card grid gap-3 p-5"
        onSubmit={async (e) => {
          e.preventDefault();
          await api(`/admin/modules/${id}/exercises`, {
            method: "POST",
            body: JSON.stringify({
              ...ex,
              options: ex.options ? ex.options.split("|").map((item) => item.trim()).filter(Boolean) : null,
            }),
          });
          setEx({ ...ex, prompt: "", answer: "", options: "" });
          load();
        }}
      >
        <h2 className="font-semibold">Добавить упражнение</h2>
        {kindSelect(ex.kind, (kind) => setEx({ ...ex, kind }))}
        <input className="field" placeholder="Задание" value={ex.prompt} onChange={(e) => setEx({ ...ex, prompt: e.target.value })} required />
        <input className="field" placeholder="Варианты через | (для выбора)" value={ex.options} onChange={(e) => setEx({ ...ex, options: e.target.value })} />
        <input className="field" placeholder="Ответ" value={ex.answer} onChange={(e) => setEx({ ...ex, answer: e.target.value })} required />
        <button className="btn btn-primary justify-self-start">Добавить в практику</button>
      </form>
      <div className="grid gap-2">
        {data.exercises.map((item) => (
          <div key={item.id} className="card grid gap-2 p-4 text-sm">
            {editEx?.id === item.id ? (
              <form
                className="grid gap-2"
                onSubmit={async (e) => {
                  e.preventDefault();
                  await api(`/admin/exercises/${item.id}`, {
                    method: "PATCH",
                    body: JSON.stringify({
                      kind: editEx.kind,
                      prompt: editEx.prompt,
                      answer: editEx.answer,
                      explanation: editEx.explanation,
                      options: editEx.options,
                      accepted: editEx.accepted,
                    }),
                  });
                  setEditEx(null);
                  load();
                }}
              >
                {kindSelect(editEx.kind, (kind) => setEditEx({ ...editEx, kind }))}
                <input className="field" value={editEx.prompt} onChange={(e) => setEditEx({ ...editEx, prompt: e.target.value })} />
                <input
                  className="field"
                  placeholder="Варианты через | (для match: left | => | right)"
                  value={optionsEditValue(editEx.options)}
                  onChange={(e) =>
                    setEditEx({
                      ...editEx,
                      options: parseOptionsEdit(e.target.value),
                    })
                  }
                />
                <input className="field" value={editEx.answer} onChange={(e) => setEditEx({ ...editEx, answer: e.target.value })} />
                <input
                  className="field"
                  placeholder="Пояснение"
                  value={editEx.explanation || ""}
                  onChange={(e) => setEditEx({ ...editEx, explanation: e.target.value })}
                />
                <div className="flex gap-2">
                  <button className="btn btn-primary text-xs">Сохранить</button>
                  <button type="button" className="btn btn-ghost text-xs" onClick={() => setEditEx(null)}>
                    Отмена
                  </button>
                </div>
              </form>
            ) : (
              <div className="flex flex-wrap items-start justify-between gap-3">
                <span>
                  <b>{item.kind}</b>: {item.prompt} → {item.answer}
                </span>
                <div className="flex gap-2">
                  <button className="text-terra" onClick={() => setEditEx(item)}>
                    изменить
                  </button>
                  <button
                    className="text-rose"
                    onClick={async () => {
                      await api(`/admin/exercises/${item.id}`, { method: "DELETE" });
                      load();
                    }}
                  >
                    удалить
                  </button>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>
      {data.test && (
        <section className="grid gap-3">
          <h2 className="font-display text-2xl">Вопросы теста модуля</h2>
          <p className="text-sm text-ink-soft">Банк теста отделён от практики; в попытке ученик получает выборку 8–12 вопросов.</p>
          <form
            className="card grid gap-3 p-5"
            onSubmit={async (e) => {
              e.preventDefault();
              await api(`/admin/tests/${data.test!.id}/questions`, {
                method: "POST",
                body: JSON.stringify({
                  ...tq,
                  options: tq.options ? tq.options.split("|").map((item) => item.trim()).filter(Boolean) : null,
                }),
              });
              setTq({ ...tq, prompt: "", answer: "", options: "" });
              load();
            }}
          >
            {kindSelect(tq.kind, (kind) => setTq({ ...tq, kind }))}
            <input className="field" placeholder="Вопрос теста" value={tq.prompt} onChange={(e) => setTq({ ...tq, prompt: e.target.value })} required />
            <input className="field" placeholder="Варианты через |" value={tq.options} onChange={(e) => setTq({ ...tq, options: e.target.value })} />
            <input className="field" placeholder="Ответ" value={tq.answer} onChange={(e) => setTq({ ...tq, answer: e.target.value })} required />
            <button className="btn btn-sage justify-self-start">Добавить в тест</button>
          </form>
          {data.test.questions.map((item) => (
            <div key={item.id} className="card grid gap-2 p-4 text-sm">
              {editTq?.id === item.id ? (
                <form
                  className="grid gap-2"
                  onSubmit={async (e) => {
                    e.preventDefault();
                    await api(`/admin/test-questions/${item.id}`, {
                      method: "PATCH",
                      body: JSON.stringify({
                        kind: editTq.kind,
                        prompt: editTq.prompt,
                        answer: editTq.answer,
                        explanation: editTq.explanation,
                        options: editTq.options,
                        accepted: editTq.accepted,
                      }),
                    });
                    setEditTq(null);
                    load();
                  }}
                >
                  {kindSelect(editTq.kind, (kind) => setEditTq({ ...editTq, kind }))}
                  <input className="field" value={editTq.prompt} onChange={(e) => setEditTq({ ...editTq, prompt: e.target.value })} />
                  <input className="field" value={editTq.answer} onChange={(e) => setEditTq({ ...editTq, answer: e.target.value })} />
                  <div className="flex gap-2">
                    <button className="btn btn-primary text-xs">Сохранить</button>
                    <button type="button" className="btn btn-ghost text-xs" onClick={() => setEditTq(null)}>
                      Отмена
                    </button>
                  </div>
                </form>
              ) : (
                <div className="flex flex-wrap items-start justify-between gap-3">
                  <span>
                    <b>{item.kind}</b>: {item.prompt} → {item.answer}
                  </span>
                  <div className="flex gap-2">
                    <button className="text-terra" onClick={() => setEditTq(item)}>
                      изменить
                    </button>
                    <button
                      className="text-rose"
                      onClick={async () => {
                        await api(`/admin/test-questions/${item.id}`, { method: "DELETE" });
                        load();
                      }}
                    >
                      удалить
                    </button>
                  </div>
                </div>
              )}
            </div>
          ))}
        </section>
      )}
    </div>
  );
}

type VocabTopicRow = {
  id: number;
  slug: string;
  title: string;
  description: string;
  level_code: string;
  sort_order: number;
  word_count: number;
};

type VocabWordRow = {
  id: number;
  topic_id: number;
  word: string;
  transcription: string;
  translation: string;
  part_of_speech: string;
  example: string;
  example_translation: string;
};

const PARTS_OF_SPEECH = [
  { value: "noun", ru: "существительное" },
  { value: "verb", ru: "глагол" },
  { value: "adjective", ru: "прилагательное" },
  { value: "adverb", ru: "наречие" },
  { value: "preposition", ru: "предлог" },
  { value: "conjunction", ru: "союз" },
  { value: "pronoun", ru: "местоимение" },
  { value: "determiner", ru: "определитель" },
  { value: "interjection", ru: "междометие" },
  { value: "phrase", ru: "фраза" },
  { value: "other", ru: "другое" },
] as const;

function PartOfSpeechSelect({ value, onChange }: { value: string; onChange: (value: string) => void }) {
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const rootRef = useRef<HTMLDivElement>(null);
  const known = PARTS_OF_SPEECH.find((opt) => opt.value === value);
  const options = [
    { value: "", label: "Не указано" },
    ...(!known && value ? [{ value, label: value }] : []),
    ...PARTS_OF_SPEECH.map((opt) => ({ value: opt.value, label: `${opt.value} — ${opt.ru}` })),
  ];
  const display = known ? `${known.value} — ${known.ru}` : value;

  useEffect(() => {
    if (!open) return;
    const close = (event: MouseEvent) => {
      if (!rootRef.current?.contains(event.target as Node)) setOpen(false);
    };
    document.addEventListener("mousedown", close);
    return () => document.removeEventListener("mousedown", close);
  }, [open]);

  const pick = (next: string) => {
    onChange(next);
    setOpen(false);
  };

  const move = (delta: number) => {
    setActive((current) => (current + delta + options.length) % options.length);
  };

  const onKeyDown = (event: React.KeyboardEvent) => {
    if (!open) {
      if (event.key === "Enter" || event.key === " " || event.key === "ArrowDown" || event.key === "ArrowUp") {
        event.preventDefault();
        const index = Math.max(0, options.findIndex((opt) => opt.value === value));
        setActive(index);
        setOpen(true);
      }
      return;
    }
    if (event.key === "Escape") {
      event.preventDefault();
      setOpen(false);
    } else if (event.key === "ArrowDown") {
      event.preventDefault();
      move(1);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      move(-1);
    } else if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      pick(options[active]?.value ?? "");
    }
  };

  return (
    <div className="choice" ref={rootRef} onKeyDown={onKeyDown}>
      <button
        type="button"
        className={`field choice-trigger${display ? "" : " is-empty"}`}
        aria-haspopup="listbox"
        aria-expanded={open}
        onClick={() => {
          const index = Math.max(0, options.findIndex((opt) => opt.value === value));
          setActive(index);
          setOpen((wasOpen) => !wasOpen);
        }}
      >
        {display || "Часть речи"}
      </button>
      {open ? (
        <div className="choice-panel" role="listbox">
          {options.map((opt, index) => (
            <button
              key={opt.value || "empty"}
              type="button"
              role="option"
              aria-selected={opt.value === value}
              className={`choice-option${opt.value === value ? " is-selected" : ""}${index === active ? " is-active" : ""}`}
              onMouseEnter={() => setActive(index)}
              onClick={() => pick(opt.value)}
            >
              {opt.label}
            </button>
          ))}
        </div>
      ) : null}
    </div>
  );
}

const emptyWordForm = {
  word: "",
  transcription: "",
  translation: "",
  part_of_speech: "",
  example: "",
  example_translation: "",
};

export function AdminVocab() {
  const [topics, setTopics] = useState<VocabTopicRow[]>([]);
  const [form, setForm] = useState({ slug: "", title: "", description: "Новая тема", level_code: "A1", sort_order: 99 });
  const [error, setError] = useState("");
  const load = () => api<VocabTopicRow[]>("/admin/vocab/topics").then(setTopics);
  useEffect(() => {
    load();
  }, []);

  return (
    <div className="grid gap-6">
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          try {
            await api("/admin/vocab/topics", { method: "POST", body: JSON.stringify(form) });
            setForm({ slug: "", title: "", description: "Новая тема", level_code: form.level_code, sort_order: 99 });
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось создать тему");
          }
        }}
      >
        <h2 className="font-display text-2xl md:col-span-2">Новая тема</h2>
        <input className="field" placeholder="slug" value={form.slug} onChange={(e) => setForm({ ...form, slug: e.target.value })} required />
        <input className="field" placeholder="Название" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} required />
        <input
          className="field md:col-span-2"
          placeholder="Описание"
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
          required
        />
        <select className="field" value={form.level_code} onChange={(e) => setForm({ ...form, level_code: e.target.value })}>
          {["A1", "A2", "B1", "B2", "C1", "C2"].map((c) => (
            <option key={c}>{c}</option>
          ))}
        </select>
        <input
          className="field"
          type="number"
          placeholder="Порядок"
          value={form.sort_order}
          onChange={(e) => setForm({ ...form, sort_order: Number(e.target.value) })}
        />
        <button className="btn btn-primary justify-self-start">Добавить тему</button>
        {error && <p className="text-sm text-rose md:col-span-2">{error}</p>}
      </form>
      <div className="grid gap-3">
        {topics.map((t) => (
          <div key={t.id} className="card flex flex-wrap items-center justify-between gap-3 p-4">
            <div>
              <p className="text-xs text-terra">{t.level_code}</p>
              <p className="font-semibold">{t.title}</p>
              <p className="text-sm text-ink-soft">
                {t.slug} · слов {t.word_count} · порядок {t.sort_order}
              </p>
            </div>
            <div className="flex gap-2">
              <Link to={`/admin/vocab/${t.id}`} className="btn btn-ghost text-sm">
                Редактировать
              </Link>
              <button
                className="btn btn-ghost text-sm"
                onClick={async () => {
                  if (confirm(`Удалить тему «${t.title}» и все её слова?`)) {
                    await api(`/admin/vocab/topics/${t.id}`, { method: "DELETE" });
                    load();
                  }
                }}
              >
                Удалить
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export function AdminVocabTopic() {
  const { topicId } = useParams();
  const id = Number(topicId);
  const [data, setData] = useState<(VocabTopicRow & { words: VocabWordRow[] }) | null>(null);
  const [topics, setTopics] = useState<VocabTopicRow[]>([]);
  const [meta, setMeta] = useState({ slug: "", title: "", description: "", level_code: "A1", sort_order: 99 });
  const [wordForm, setWordForm] = useState(emptyWordForm);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [draft, setDraft] = useState<VocabWordRow | null>(null);
  const [error, setError] = useState("");
  const [saved, setSaved] = useState("");

  const load = () =>
    api<VocabTopicRow & { words: VocabWordRow[] }>(`/admin/vocab/topics/${id}`).then((row) => {
      setData(row);
      setMeta({
        slug: row.slug,
        title: row.title,
        description: row.description,
        level_code: row.level_code,
        sort_order: row.sort_order,
      });
    });

  useEffect(() => {
    load();
    api<VocabTopicRow[]>("/admin/vocab/topics").then(setTopics);
  }, [id]);

  if (!data) return <p>Загружаем тему…</p>;

  return (
    <div className="grid gap-6">
      <div>
        <Link to="/admin/vocab" className="text-sm text-terra">
          ← Словарь
        </Link>
        <h1 className="font-display mt-2 text-3xl">{data.title}</h1>
        <p className="text-sm text-ink-soft">
          {data.word_count} слов · ученики открывают тему по адресу /app/vocab/{data.slug}
        </p>
      </div>
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          setSaved("");
          try {
            await api(`/admin/vocab/topics/${id}`, { method: "PATCH", body: JSON.stringify(meta) });
            setSaved("Тема сохранена.");
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось сохранить тему");
          }
        }}
      >
        <h2 className="font-semibold md:col-span-2">Параметры темы</h2>
        <label className="grid gap-1 text-sm">
          Название
          <input className="field" value={meta.title} onChange={(e) => setMeta({ ...meta, title: e.target.value })} required />
        </label>
        <label className="grid gap-1 text-sm">
          Slug
          <input className="field" value={meta.slug} onChange={(e) => setMeta({ ...meta, slug: e.target.value })} required />
        </label>
        <label className="grid gap-1 text-sm md:col-span-2">
          Описание
          <textarea className="field min-h-24" value={meta.description} onChange={(e) => setMeta({ ...meta, description: e.target.value })} />
        </label>
        <label className="grid gap-1 text-sm">
          Уровень CEFR
          <select className="field" value={meta.level_code} onChange={(e) => setMeta({ ...meta, level_code: e.target.value })}>
            {["A1", "A2", "B1", "B2", "C1", "C2"].map((c) => (
              <option key={c}>{c}</option>
            ))}
          </select>
        </label>
        <label className="grid gap-1 text-sm">
          Порядок
          <input
            className="field"
            type="number"
            value={meta.sort_order}
            onChange={(e) => setMeta({ ...meta, sort_order: Number(e.target.value) })}
          />
        </label>
        <p className="text-sm text-ink-soft md:col-span-2">
          Slug входит в ссылку ученика. Если смените его, старый адрес /app/vocab/{data.slug} перестанет открываться.
        </p>
        <button className="btn btn-primary justify-self-start">Сохранить тему</button>
        {saved && <p className="text-sm text-sage md:col-span-2">{saved}</p>}
        {error && <p className="text-sm text-rose md:col-span-2">{error}</p>}
      </form>
      <form
        className="card grid gap-3 p-5"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          try {
            await api("/admin/vocab/words", { method: "POST", body: JSON.stringify({ ...wordForm, topic_id: id }) });
            setWordForm(emptyWordForm);
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось добавить слово");
          }
        }}
      >
        <h2 className="font-semibold">Добавить слово</h2>
        <input className="field" placeholder="English word" value={wordForm.word} onChange={(e) => setWordForm({ ...wordForm, word: e.target.value })} required />
        <input
          className="field"
          placeholder="IPA, например /ˈteɪ.bəl/"
          value={wordForm.transcription}
          onChange={(e) => setWordForm({ ...wordForm, transcription: e.target.value })}
        />
        <input
          className="field"
          placeholder="Перевод"
          value={wordForm.translation}
          onChange={(e) => setWordForm({ ...wordForm, translation: e.target.value })}
          required
        />
        <PartOfSpeechSelect
          value={wordForm.part_of_speech}
          onChange={(part_of_speech) => setWordForm({ ...wordForm, part_of_speech })}
        />
        <input className="field" placeholder="Пример на английском" value={wordForm.example} onChange={(e) => setWordForm({ ...wordForm, example: e.target.value })} required />
        <input
          className="field"
          placeholder="Перевод примера"
          value={wordForm.example_translation}
          onChange={(e) => setWordForm({ ...wordForm, example_translation: e.target.value })}
          required
        />
        <button className="btn btn-sage justify-self-start">Добавить в тему</button>
      </form>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl">Слова в теме</h2>
        {data.words.map((item) => (
          <div key={item.id} className="card grid gap-3 p-4 text-sm">
            {editingId === item.id && draft ? (
              <form
                className="grid gap-2"
                onSubmit={async (e) => {
                  e.preventDefault();
                  setError("");
                  try {
                    await api(`/admin/vocab/words/${item.id}`, {
                      method: "PATCH",
                      body: JSON.stringify({
                        topic_id: draft.topic_id,
                        word: draft.word,
                        transcription: draft.transcription,
                        translation: draft.translation,
                        part_of_speech: draft.part_of_speech,
                        example: draft.example,
                        example_translation: draft.example_translation,
                      }),
                    });
                    setEditingId(null);
                    setDraft(null);
                    load();
                  } catch (err) {
                    setError(err instanceof Error ? err.message : "Не удалось сохранить слово");
                  }
                }}
              >
                <input className="field" value={draft.word} onChange={(e) => setDraft({ ...draft, word: e.target.value })} required />
                <input className="field" placeholder="IPA" value={draft.transcription} onChange={(e) => setDraft({ ...draft, transcription: e.target.value })} />
                <input className="field" placeholder="Перевод" value={draft.translation} onChange={(e) => setDraft({ ...draft, translation: e.target.value })} required />
                <PartOfSpeechSelect
                  value={draft.part_of_speech}
                  onChange={(part_of_speech) => setDraft({ ...draft, part_of_speech })}
                />
                <input className="field" placeholder="Пример" value={draft.example} onChange={(e) => setDraft({ ...draft, example: e.target.value })} required />
                <input
                  className="field"
                  placeholder="Перевод примера"
                  value={draft.example_translation}
                  onChange={(e) => setDraft({ ...draft, example_translation: e.target.value })}
                  required
                />
                <label className="grid gap-1 text-sm">
                  Перенести в другую тему
                  <select className="field" value={draft.topic_id} onChange={(e) => setDraft({ ...draft, topic_id: Number(e.target.value) })}>
                    {topics.map((topic) => (
                      <option key={topic.id} value={topic.id}>
                        {topic.level_code} · {topic.title}
                      </option>
                    ))}
                  </select>
                </label>
                <div className="flex gap-2">
                  <button className="btn btn-primary text-sm">Сохранить слово</button>
                  <button type="button" className="btn btn-ghost text-sm" onClick={() => { setEditingId(null); setDraft(null); }}>
                    Отмена
                  </button>
                </div>
              </form>
            ) : (
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <p className="font-semibold">
                    {item.word} {item.transcription && <span className="font-normal text-ink-soft">{item.transcription}</span>}
                  </p>
                  <p>
                    {item.translation} · {item.part_of_speech}
                  </p>
                  <p className="mt-1 text-ink-soft">
                    {item.example} — {item.example_translation}
                  </p>
                </div>
                <div className="flex gap-2">
                  <button className="btn btn-ghost text-xs" onClick={() => { setEditingId(item.id); setDraft({ ...item }); }}>
                    изменить
                  </button>
                  <button
                    className="text-rose"
                    onClick={async () => {
                      if (confirm(`Удалить «${item.word}»?`)) {
                        await api(`/admin/vocab/words/${item.id}`, { method: "DELETE" });
                        load();
                      }
                    }}
                  >
                    удалить
                  </button>
                </div>
              </div>
            )}
          </div>
        ))}
      </section>
    </div>
  );
}

export function AdminExams() {
  const [exams, setExams] = useState<{ id: number; title: string; level_code: string; question_count: number; passing_score: number }[]>([]);
  const [tests, setTests] = useState<{ id: number; title: string; module_title: string; question_count: number }[]>([]);
  useEffect(() => {
    api("/admin/exams").then(setExams);
    api("/admin/tests").then(setTests);
  }, []);
  return (
    <div className="grid gap-6">
      <p className="text-ink-soft">
        Вопросы тестов и экзаменов хранятся в PostgreSQL. Новые можно добавить здесь или в карточке модуля — после сохранения они сразу видны ученикам.
      </p>
      <section>
        <h2 className="font-display mb-3 text-2xl">Экзамены уровней</h2>
        <div className="grid gap-3">
          {exams.map((e) => (
            <Link key={e.id} to={`/admin/exams/${e.id}`} className="card p-4 hover:border-terra/40">
              <p className="font-semibold">
                {e.level_code} · {e.title}
              </p>
              <p className="text-sm text-ink-soft">
                {e.question_count} вопросов · порог {e.passing_score}%
              </p>
            </Link>
          ))}
        </div>
      </section>
      <section>
        <h2 className="font-display mb-3 text-2xl">Тесты модулей</h2>
        <p className="mb-3 text-sm text-ink-soft">Всего {tests.length}. Вопросы каждого теста редактируются в «Модули → Содержание».</p>
        <div className="grid gap-2">
          {tests.slice(0, 12).map((t) => (
            <div key={t.id} className="rounded-xl bg-paper px-4 py-3 text-sm">
              {t.module_title}: {t.question_count} вопросов
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export function AdminExamDetail() {
  const { examId } = useParams();
  const [data, setData] = useState<{
    id: number;
    title: string;
    level_code: string;
    questions: ContentItem[];
  } | null>(null);
  const [form, setForm] = useState({ kind: "fill_blank", prompt: "", answer: "", explanation: "Разберите правило.", options: "" });
  const [editQ, setEditQ] = useState<ContentItem | null>(null);
  const load = () => api(`/admin/exams/${examId}`).then(setData);
  useEffect(() => {
    load();
  }, [examId]);
  if (!data) return <p>Загружаем экзамен…</p>;
  return (
    <div className="grid gap-6">
      <div>
        <Link to="/admin/exams" className="text-sm text-terra">
          ← Экзамены
        </Link>
        <h1 className="font-display mt-2 text-3xl">
          {data.level_code} · {data.title}
        </h1>
      </div>
      <form
        className="card grid gap-3 p-5"
        onSubmit={async (e) => {
          e.preventDefault();
          await api(`/admin/exams/${data.id}/questions`, {
            method: "POST",
            body: JSON.stringify({
              ...form,
              options: form.options ? form.options.split("|").map((item) => item.trim()).filter(Boolean) : null,
            }),
          });
          setForm({ ...form, prompt: "", answer: "", options: "" });
          load();
        }}
      >
        <h2 className="font-semibold">Добавить вопрос экзамена</h2>
        <select className="field" value={form.kind} onChange={(e) => setForm({ ...form, kind: e.target.value })}>
          <option value="multiple_choice">Выбор</option>
          <option value="fill_blank">Пропуск</option>
          <option value="transform">Преобразование</option>
          <option value="error_correction">Исправление</option>
          <option value="order">Порядок слов</option>
        </select>
        <input className="field" placeholder="Вопрос" value={form.prompt} onChange={(e) => setForm({ ...form, prompt: e.target.value })} required />
        <input className="field" placeholder="Варианты через |" value={form.options} onChange={(e) => setForm({ ...form, options: e.target.value })} />
        <input className="field" placeholder="Ответ" value={form.answer} onChange={(e) => setForm({ ...form, answer: e.target.value })} required />
        <button className="btn btn-primary justify-self-start">Сохранить в БД</button>
      </form>
      {data.questions.map((item) => (
        <div key={item.id} className="card grid gap-2 p-4 text-sm">
          {editQ?.id === item.id ? (
            <form
              className="grid gap-2"
              onSubmit={async (e) => {
                e.preventDefault();
                await api(`/admin/exam-questions/${item.id}`, {
                  method: "PATCH",
                  body: JSON.stringify({
                    kind: editQ.kind,
                    prompt: editQ.prompt,
                    answer: editQ.answer,
                    explanation: editQ.explanation,
                    options: editQ.options,
                  }),
                });
                setEditQ(null);
                load();
              }}
            >
              <input className="field" value={editQ.prompt} onChange={(e) => setEditQ({ ...editQ, prompt: e.target.value })} />
              <input className="field" value={editQ.answer} onChange={(e) => setEditQ({ ...editQ, answer: e.target.value })} />
              <div className="flex gap-2">
                <button className="btn btn-primary text-xs">Сохранить</button>
                <button type="button" className="btn btn-ghost text-xs" onClick={() => setEditQ(null)}>
                  Отмена
                </button>
              </div>
            </form>
          ) : (
            <div className="flex flex-wrap items-start justify-between gap-3">
              <span>
                <b>{item.kind}</b>: {item.prompt} → {item.answer}
              </span>
              <div className="flex gap-2">
                <button className="text-terra" onClick={() => setEditQ(item)}>
                  изменить
                </button>
                <button
                  className="text-rose"
                  onClick={async () => {
                    await api(`/admin/exam-questions/${item.id}`, { method: "DELETE" });
                    load();
                  }}
                >
                  удалить
                </button>
              </div>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

export function AdminDonation() {
  const [form, setForm] = useState({
    donation_enabled: false,
    donation_title: "Сайт оказался полезным?",
    donation_message: "Если lEarNinG помогает учить ENG, можно оставить чаевые.",
    donation_url: "",
    donation_button: "Оставить чаевые",
  });
  const [reg, setReg] = useState({ email_verification_required: true });
  const [saved, setSaved] = useState("");
  const [regSaved, setRegSaved] = useState("");

  useEffect(() => {
    api<typeof form>("/admin/donation").then((data) => {
      setForm({
        donation_enabled: data.donation_enabled,
        donation_title: data.donation_title,
        donation_message: data.donation_message,
        donation_url: data.donation_url,
        donation_button: data.donation_button,
      });
    });
    api<typeof reg>("/admin/registration").then(setReg);
  }, []);

  return (
    <div className="grid gap-6">
      <div>
        <h1 className="font-display text-3xl">Настройки сайта</h1>
        <p className="mt-2 max-w-3xl text-ink-soft">Регистрация, подтверждение почты и плашка с чаевыми.</p>
      </div>

      <form
        className="card grid gap-4 p-6"
        onSubmit={async (e) => {
          e.preventDefault();
          await api("/admin/registration", { method: "PATCH", body: JSON.stringify(reg) });
          setRegSaved("Сохранено.");
        }}
      >
        <h2 className="font-display text-2xl">Регистрация</h2>
        <p className="text-sm text-ink-soft">
          Если SMTP на VPS блокируется, отключите подтверждение email — новые ученики сразу смогут войти. Уже
          зарегистрированных без письма можно активировать вручную в разделе «Пользователи».
        </p>
        <label className="flex items-center gap-3">
          <input
            type="checkbox"
            checked={reg.email_verification_required}
            onChange={(e) => setReg({ email_verification_required: e.target.checked })}
          />
          Требовать подтверждение email при регистрации
        </label>
        <button className="btn btn-primary justify-self-start">Сохранить регистрацию</button>
        {regSaved && <p className="text-sm text-sage">{regSaved}</p>}
      </form>

      <div>
        <h2 className="font-display text-2xl">Плашка с чаевыми</h2>
        <p className="mt-2 max-w-3xl text-ink-soft">
          Включите плашку и вставьте ссылку на страницу донатов. Она появится у всех посетителей на главной и в кабинете.
          Скрыть её можно крестиком — до конца сессии браузера.
        </p>
      </div>
      <form
        className="card grid gap-4 p-6"
        onSubmit={async (e) => {
          e.preventDefault();
          await api("/admin/donation", { method: "PATCH", body: JSON.stringify(form) });
          setSaved("Сохранено. Если включено и есть ссылка — плашка уже на сайте.");
        }}
      >
        <label className="flex items-center gap-3">
          <input
            type="checkbox"
            checked={form.donation_enabled}
            onChange={(e) => setForm({ ...form, donation_enabled: e.target.checked })}
          />
          Показывать плашку на всём сайте
        </label>
        <label className="grid gap-1 text-sm">
          Заголовок
          <input className="field" value={form.donation_title} onChange={(e) => setForm({ ...form, donation_title: e.target.value })} />
        </label>
        <label className="grid gap-1 text-sm">
          Текст
          <textarea className="field min-h-24" value={form.donation_message} onChange={(e) => setForm({ ...form, donation_message: e.target.value })} />
        </label>
        <label className="grid gap-1 text-sm">
          Ссылка на чаевые
          <input
            className="field"
            type="url"
            placeholder="https://..."
            value={form.donation_url}
            onChange={(e) => setForm({ ...form, donation_url: e.target.value })}
          />
        </label>
        <label className="grid gap-1 text-sm">
          Текст кнопки
          <input className="field" value={form.donation_button} onChange={(e) => setForm({ ...form, donation_button: e.target.value })} />
        </label>
        <button className="btn btn-primary justify-self-start">Сохранить</button>
        {saved && <p className="text-sm text-sage">{saved}</p>}
      </form>
      <section className="card grid gap-3 p-6 text-sm leading-7 text-ink-soft">
        <h2 className="font-display text-2xl text-ink">Где зарегистрироваться</h2>
        <p>
          <b>Если аудитория в России и удобны СБП / карты РФ</b> — начните с{" "}
          <a className="text-terra" href="https://pay.cloudtips.ru" target="_blank" rel="noreferrer">
            CloudTips
          </a>{" "}
          (Тинькофф): страница чаевых за несколько минут, без своего интернет-магазина. Для регулярной поддержки и «страницы автора» удобнее{" "}
          <a className="text-terra" href="https://boosty.to" target="_blank" rel="noreferrer">
            Boosty
          </a>
          . Разовые «кинуть на чай» во время стримов и постов —{" "}
          <a className="text-terra" href="https://www.donationalerts.com" target="_blank" rel="noreferrer">
            DonationAlerts
          </a>{" "}
          или кошелёк{" "}
          <a className="text-terra" href="https://yoomoney.ru" target="_blank" rel="noreferrer">
            ЮMoney
          </a>
          .
        </p>
        <p>
          <b>Если часть пользователей платит иностранными картами</b> —{" "}
          <a className="text-terra" href="https://www.buymeacoffee.com" target="_blank" rel="noreferrer">
            Buy Me a Coffee
          </a>{" "}
          или{" "}
          <a className="text-terra" href="https://ko-fi.com" target="_blank" rel="noreferrer">
            Ko-fi
          </a>
          : простая кнопка чаевых, минимальная бюрократия. Patreon имеет смысл только если появятся платные уровни.
        </p>
        <p>Практичный старт: CloudTips для РФ + Buy Me a Coffee для остального мира. В плашку вставьте одну главную ссылку.</p>
      </section>
    </div>
  );
}

const STUDY_KIND_OPTIONS = [
  { value: "verbs", label: "Глаголы" },
  { value: "idioms", label: "Идиомы" },
  { value: "exceptions", label: "Исключения" },
] as const;

const SKILL_KIND_OPTIONS = [
  { value: "reading", label: "Чтение" },
  { value: "listening", label: "Аудирование" },
  { value: "dialogue", label: "Диалоги" },
] as const;

const SKILL_QUESTION_KIND_OPTIONS = [
  { value: "choice", label: "Выбор" },
  { value: "dictation", label: "Диктант" },
  { value: "fill_gap", label: "Пропуск" },
] as const;

type StudyDeckRow = {
  id: number;
  slug: string;
  title: string;
  description: string;
  kind: string;
  sort_order: number;
  card_count: number;
};

type StudyCardRow = {
  id: number;
  deck_id: number;
  primary_text: string;
  secondary_text: string;
  tertiary_text: string;
  translation: string;
  example: string;
  example_translation: string;
  category: string;
  sort_order: number;
};

type SkillItemRow = {
  id: number;
  slug: string;
  title: string;
  description: string;
  kind: string;
  level_code: string;
  sort_order: number;
  question_count: number;
  keyword_count: number;
  body?: string;
  lines?: { speaker: string; text: string; ru: string }[];
  keywords?: { en: string; ru: string }[];
  questions?: SkillQuestionRow[];
};

type SkillQuestionRow = {
  id: number;
  item_id: number;
  kind: string;
  prompt: string;
  options: string[] | null;
  answer: string;
  accepted: string[] | null;
  speak: string;
  explanation: string;
  sort_order: number;
};

const emptyCardForm = {
  primary_text: "",
  secondary_text: "",
  tertiary_text: "",
  translation: "",
  example: "",
  example_translation: "",
  category: "",
  sort_order: 1,
};

const emptyQuestionForm = {
  kind: "choice",
  prompt: "",
  optionsText: "",
  answer: "",
  acceptedText: "",
  speak: "",
  explanation: "",
  sort_order: 1,
};

function studyKindLabel(kind: string) {
  return STUDY_KIND_OPTIONS.find((o) => o.value === kind)?.label ?? kind;
}

function skillKindLabel(kind: string) {
  return SKILL_KIND_OPTIONS.find((o) => o.value === kind)?.label ?? kind;
}

function skillLearnerPath(kind: string, slug: string) {
  const base = kind === "dialogue" ? "dialogues" : kind;
  return `/app/${base}/${slug}`;
}

function keywordsToText(rows: { en: string; ru: string }[] | undefined) {
  return (rows || []).map((row) => `${row.en} | ${row.ru}`).join("\n");
}

function textToKeywords(text: string) {
  return text
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const [en = "", ru = ""] = line.split("|").map((part) => part.trim());
      return { en, ru };
    })
    .filter((row) => row.en || row.ru);
}

function linesToText(rows: { speaker: string; text: string; ru: string }[] | undefined) {
  return (rows || []).map((row) => `${row.speaker} | ${row.text} | ${row.ru}`).join("\n");
}

function textToLines(text: string) {
  return text
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const [speaker = "", textPart = "", ru = ""] = line.split("|").map((part) => part.trim());
      return { speaker, text: textPart, ru };
    })
    .filter((row) => row.speaker || row.text || row.ru);
}

function listToText(rows: string[] | null | undefined) {
  return (rows || []).join("\n");
}

function textToList(text: string) {
  return text
    .split(/\n|,/)
    .map((part) => part.trim())
    .filter(Boolean);
}

export function AdminStudy() {
  const [decks, setDecks] = useState<StudyDeckRow[]>([]);
  const [form, setForm] = useState({
    slug: "",
    title: "",
    description: "Новая колода",
    kind: "verbs",
    sort_order: 99,
  });
  const [error, setError] = useState("");
  const load = () => api<StudyDeckRow[]>("/admin/study/decks").then(setDecks);
  useEffect(() => {
    load();
  }, []);

  return (
    <div className="grid gap-6">
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          try {
            await api("/admin/study/decks", { method: "POST", body: JSON.stringify(form) });
            setForm({ slug: "", title: "", description: "Новая колода", kind: form.kind, sort_order: 99 });
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось создать колоду");
          }
        }}
      >
        <h2 className="font-display text-2xl md:col-span-2">Новая колода</h2>
        <input className="field" placeholder="slug" value={form.slug} onChange={(e) => setForm({ ...form, slug: e.target.value })} required />
        <input className="field" placeholder="Название" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} required />
        <input
          className="field md:col-span-2"
          placeholder="Описание"
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
        />
        <select className="field" value={form.kind} onChange={(e) => setForm({ ...form, kind: e.target.value })}>
          {STUDY_KIND_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
        <input
          className="field"
          type="number"
          placeholder="Порядок"
          value={form.sort_order}
          onChange={(e) => setForm({ ...form, sort_order: Number(e.target.value) })}
        />
        <button className="btn btn-primary justify-self-start">Добавить колоду</button>
        {error && <p className="text-sm text-rose md:col-span-2">{error}</p>}
      </form>
      <div className="grid gap-3">
        {decks.map((deck) => (
          <div key={deck.id} className="card flex flex-wrap items-center justify-between gap-3 p-4">
            <div>
              <p className="text-xs text-terra">{studyKindLabel(deck.kind)}</p>
              <p className="font-semibold">{deck.title}</p>
              <p className="text-sm text-ink-soft">
                {deck.slug} · карточек {deck.card_count} · порядок {deck.sort_order}
              </p>
            </div>
            <div className="flex gap-2">
              <Link to={`/admin/study/${deck.id}`} className="btn btn-ghost text-sm">
                Редактировать
              </Link>
              <button
                className="btn btn-ghost text-sm"
                onClick={async () => {
                  if (confirm(`Удалить колоду «${deck.title}» и все её карточки?`)) {
                    await api(`/admin/study/decks/${deck.id}`, { method: "DELETE" });
                    load();
                  }
                }}
              >
                Удалить
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export function AdminStudyDeck() {
  const { deckId } = useParams();
  const id = Number(deckId);
  const [data, setData] = useState<(StudyDeckRow & { cards: StudyCardRow[] }) | null>(null);
  const [meta, setMeta] = useState({ slug: "", title: "", description: "", kind: "verbs", sort_order: 99 });
  const [cardForm, setCardForm] = useState(emptyCardForm);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [draft, setDraft] = useState<StudyCardRow | null>(null);
  const [error, setError] = useState("");
  const [saved, setSaved] = useState("");

  const load = () =>
    api<StudyDeckRow & { cards: StudyCardRow[] }>(`/admin/study/decks/${id}`).then((row) => {
      setData(row);
      setMeta({
        slug: row.slug,
        title: row.title,
        description: row.description,
        kind: row.kind,
        sort_order: row.sort_order,
      });
    });

  useEffect(() => {
    load();
  }, [id]);

  if (!data) return <p>Загружаем колоду…</p>;

  return (
    <div className="grid gap-6">
      <div>
        <Link to="/admin/study" className="text-sm text-terra">
          ← Колоды
        </Link>
        <h1 className="font-display mt-2 text-3xl">{data.title}</h1>
        <p className="text-sm text-ink-soft">
          {data.card_count} карточек · ученики: /app/{data.kind}/{data.slug}
        </p>
      </div>
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          setSaved("");
          try {
            await api(`/admin/study/decks/${id}`, { method: "PATCH", body: JSON.stringify(meta) });
            setSaved("Колода сохранена.");
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось сохранить колоду");
          }
        }}
      >
        <h2 className="font-semibold md:col-span-2">Параметры колоды</h2>
        <label className="grid gap-1 text-sm">
          Название
          <input className="field" value={meta.title} onChange={(e) => setMeta({ ...meta, title: e.target.value })} required />
        </label>
        <label className="grid gap-1 text-sm">
          Slug
          <input className="field" value={meta.slug} onChange={(e) => setMeta({ ...meta, slug: e.target.value })} required />
        </label>
        <label className="grid gap-1 text-sm md:col-span-2">
          Описание
          <textarea className="field min-h-24" value={meta.description} onChange={(e) => setMeta({ ...meta, description: e.target.value })} />
        </label>
        <label className="grid gap-1 text-sm">
          Раздел
          <select className="field" value={meta.kind} onChange={(e) => setMeta({ ...meta, kind: e.target.value })}>
            {STUDY_KIND_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
        </label>
        <label className="grid gap-1 text-sm">
          Порядок
          <input className="field" type="number" value={meta.sort_order} onChange={(e) => setMeta({ ...meta, sort_order: Number(e.target.value) })} />
        </label>
        <button className="btn btn-primary justify-self-start">Сохранить колоду</button>
        {saved && <p className="text-sm text-sage md:col-span-2">{saved}</p>}
        {error && <p className="text-sm text-rose md:col-span-2">{error}</p>}
      </form>
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          try {
            await api("/admin/study/cards", { method: "POST", body: JSON.stringify({ ...cardForm, deck_id: id }) });
            setCardForm(emptyCardForm);
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось добавить карточку");
          }
        }}
      >
        <h2 className="font-semibold md:col-span-2">Добавить карточку</h2>
        <input
          className="field"
          placeholder="Основной текст (V1 / фраза)"
          value={cardForm.primary_text}
          onChange={(e) => setCardForm({ ...cardForm, primary_text: e.target.value })}
          required
        />
        <input
          className="field"
          placeholder="Перевод"
          value={cardForm.translation}
          onChange={(e) => setCardForm({ ...cardForm, translation: e.target.value })}
          required
        />
        <input
          className="field"
          placeholder="Второй текст (V2 / заметка)"
          value={cardForm.secondary_text}
          onChange={(e) => setCardForm({ ...cardForm, secondary_text: e.target.value })}
        />
        <input
          className="field"
          placeholder="Третий текст (V3)"
          value={cardForm.tertiary_text}
          onChange={(e) => setCardForm({ ...cardForm, tertiary_text: e.target.value })}
        />
        <input
          className="field md:col-span-2"
          placeholder="Пример"
          value={cardForm.example}
          onChange={(e) => setCardForm({ ...cardForm, example: e.target.value })}
        />
        <input
          className="field md:col-span-2"
          placeholder="Перевод примера"
          value={cardForm.example_translation}
          onChange={(e) => setCardForm({ ...cardForm, example_translation: e.target.value })}
        />
        <input
          className="field"
          placeholder="Категория"
          value={cardForm.category}
          onChange={(e) => setCardForm({ ...cardForm, category: e.target.value })}
        />
        <input
          className="field"
          type="number"
          placeholder="Порядок"
          value={cardForm.sort_order}
          onChange={(e) => setCardForm({ ...cardForm, sort_order: Number(e.target.value) })}
        />
        <button className="btn btn-sage justify-self-start">Добавить в колоду</button>
      </form>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl">Карточки</h2>
        {data.cards.map((item) => (
          <div key={item.id} className="card grid gap-3 p-4 text-sm">
            {editingId === item.id && draft ? (
              <form
                className="grid gap-2 md:grid-cols-2"
                onSubmit={async (e) => {
                  e.preventDefault();
                  setError("");
                  try {
                    await api(`/admin/study/cards/${item.id}`, {
                      method: "PATCH",
                      body: JSON.stringify({
                        primary_text: draft.primary_text,
                        secondary_text: draft.secondary_text,
                        tertiary_text: draft.tertiary_text,
                        translation: draft.translation,
                        example: draft.example,
                        example_translation: draft.example_translation,
                        category: draft.category,
                        sort_order: draft.sort_order,
                      }),
                    });
                    setEditingId(null);
                    setDraft(null);
                    load();
                  } catch (err) {
                    setError(err instanceof Error ? err.message : "Не удалось сохранить карточку");
                  }
                }}
              >
                <input className="field" value={draft.primary_text} onChange={(e) => setDraft({ ...draft, primary_text: e.target.value })} required />
                <input className="field" value={draft.translation} onChange={(e) => setDraft({ ...draft, translation: e.target.value })} required />
                <input className="field" placeholder="V2 / заметка" value={draft.secondary_text} onChange={(e) => setDraft({ ...draft, secondary_text: e.target.value })} />
                <input className="field" placeholder="V3" value={draft.tertiary_text} onChange={(e) => setDraft({ ...draft, tertiary_text: e.target.value })} />
                <input className="field md:col-span-2" placeholder="Пример" value={draft.example} onChange={(e) => setDraft({ ...draft, example: e.target.value })} />
                <input
                  className="field md:col-span-2"
                  placeholder="Перевод примера"
                  value={draft.example_translation}
                  onChange={(e) => setDraft({ ...draft, example_translation: e.target.value })}
                />
                <input className="field" placeholder="Категория" value={draft.category} onChange={(e) => setDraft({ ...draft, category: e.target.value })} />
                <input
                  className="field"
                  type="number"
                  value={draft.sort_order}
                  onChange={(e) => setDraft({ ...draft, sort_order: Number(e.target.value) })}
                />
                <div className="flex gap-2 md:col-span-2">
                  <button className="btn btn-primary text-sm">Сохранить карточку</button>
                  <button type="button" className="btn btn-ghost text-sm" onClick={() => { setEditingId(null); setDraft(null); }}>
                    Отмена
                  </button>
                </div>
              </form>
            ) : (
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <p className="font-semibold">
                    {item.primary_text}
                    {item.secondary_text ? ` · ${item.secondary_text}` : ""}
                    {item.tertiary_text ? ` · ${item.tertiary_text}` : ""}
                  </p>
                  <p>{item.translation}</p>
                  {(item.example || item.example_translation) && (
                    <p className="mt-1 text-ink-soft">
                      {item.example}
                      {item.example_translation ? ` — ${item.example_translation}` : ""}
                    </p>
                  )}
                  <p className="mt-1 text-xs text-ink-soft">
                    {item.category || "без категории"} · порядок {item.sort_order}
                  </p>
                </div>
                <div className="flex gap-2">
                  <button className="btn btn-ghost text-xs" onClick={() => { setEditingId(item.id); setDraft({ ...item }); }}>
                    изменить
                  </button>
                  <button
                    className="text-rose"
                    onClick={async () => {
                      if (confirm(`Удалить «${item.primary_text}»?`)) {
                        await api(`/admin/study/cards/${item.id}`, { method: "DELETE" });
                        load();
                      }
                    }}
                  >
                    удалить
                  </button>
                </div>
              </div>
            )}
          </div>
        ))}
      </section>
    </div>
  );
}

export function AdminSkills() {
  const [items, setItems] = useState<SkillItemRow[]>([]);
  const [form, setForm] = useState({
    slug: "",
    title: "",
    description: "Новый материал",
    kind: "reading",
    level_code: "A1",
    sort_order: 99,
  });
  const [error, setError] = useState("");
  const load = () => api<SkillItemRow[]>("/admin/skills").then(setItems);
  useEffect(() => {
    load();
  }, []);

  return (
    <div className="grid gap-6">
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          try {
            await api("/admin/skills", {
              method: "POST",
              body: JSON.stringify({ ...form, body: "", lines: [], keywords: [] }),
            });
            setForm({
              slug: "",
              title: "",
              description: "Новый материал",
              kind: form.kind,
              level_code: form.level_code,
              sort_order: 99,
            });
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось создать материал");
          }
        }}
      >
        <h2 className="font-display text-2xl md:col-span-2">Новый материал навыка</h2>
        <input className="field" placeholder="slug" value={form.slug} onChange={(e) => setForm({ ...form, slug: e.target.value })} required />
        <input className="field" placeholder="Название" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} required />
        <input
          className="field md:col-span-2"
          placeholder="Описание"
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
        />
        <select className="field" value={form.kind} onChange={(e) => setForm({ ...form, kind: e.target.value })}>
          {SKILL_KIND_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
        <select className="field" value={form.level_code} onChange={(e) => setForm({ ...form, level_code: e.target.value })}>
          {["A1", "A2", "B1", "B2", "C1", "C2"].map((code) => (
            <option key={code}>{code}</option>
          ))}
        </select>
        <input
          className="field"
          type="number"
          placeholder="Порядок"
          value={form.sort_order}
          onChange={(e) => setForm({ ...form, sort_order: Number(e.target.value) })}
        />
        <button className="btn btn-primary justify-self-start">Добавить материал</button>
        {error && <p className="text-sm text-rose md:col-span-2">{error}</p>}
      </form>
      <div className="grid gap-3">
        {items.map((item) => (
          <div key={item.id} className="card flex flex-wrap items-center justify-between gap-3 p-4">
            <div>
              <p className="text-xs text-terra">
                {skillKindLabel(item.kind)} · {item.level_code}
              </p>
              <p className="font-semibold">{item.title}</p>
              <p className="text-sm text-ink-soft">
                {item.slug} · вопросов {item.question_count} · слов {item.keyword_count} · порядок {item.sort_order}
              </p>
            </div>
            <div className="flex gap-2">
              <Link to={`/admin/skills/${item.id}`} className="btn btn-ghost text-sm">
                Редактировать
              </Link>
              <button
                className="btn btn-ghost text-sm"
                onClick={async () => {
                  if (confirm(`Удалить «${item.title}» и все вопросы?`)) {
                    await api(`/admin/skills/${item.id}`, { method: "DELETE" });
                    load();
                  }
                }}
              >
                Удалить
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export function AdminSkillItem() {
  const { itemId } = useParams();
  const id = Number(itemId);
  const [data, setData] = useState<SkillItemRow | null>(null);
  const [meta, setMeta] = useState({
    slug: "",
    title: "",
    description: "",
    kind: "reading",
    level_code: "A1",
    sort_order: 99,
    body: "",
    keywordsText: "",
    linesText: "",
  });
  const [questionForm, setQuestionForm] = useState(emptyQuestionForm);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [draft, setDraft] = useState<(SkillQuestionRow & { optionsText: string; acceptedText: string }) | null>(null);
  const [error, setError] = useState("");
  const [saved, setSaved] = useState("");

  const load = () =>
    api<SkillItemRow>(`/admin/skills/${id}`).then((row) => {
      setData(row);
      setMeta({
        slug: row.slug,
        title: row.title,
        description: row.description,
        kind: row.kind,
        level_code: row.level_code,
        sort_order: row.sort_order,
        body: row.body || "",
        keywordsText: keywordsToText(row.keywords),
        linesText: linesToText(row.lines),
      });
    });

  useEffect(() => {
    load();
  }, [id]);

  if (!data) return <p>Загружаем материал…</p>;

  return (
    <div className="grid gap-6">
      <div>
        <Link to="/admin/skills" className="text-sm text-terra">
          ← Навыки
        </Link>
        <h1 className="font-display mt-2 text-3xl">{data.title}</h1>
        <p className="text-sm text-ink-soft">
          {data.question_count} вопросов · ученики: {skillLearnerPath(data.kind, data.slug)}
        </p>
      </div>
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          setSaved("");
          try {
            await api(`/admin/skills/${id}`, {
              method: "PATCH",
              body: JSON.stringify({
                slug: meta.slug,
                title: meta.title,
                description: meta.description,
                kind: meta.kind,
                level_code: meta.level_code,
                sort_order: meta.sort_order,
                body: meta.body,
                keywords: textToKeywords(meta.keywordsText),
                lines: textToLines(meta.linesText),
              }),
            });
            setSaved("Материал сохранён.");
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось сохранить материал");
          }
        }}
      >
        <h2 className="font-semibold md:col-span-2">Параметры материала</h2>
        <label className="grid gap-1 text-sm">
          Название
          <input className="field" value={meta.title} onChange={(e) => setMeta({ ...meta, title: e.target.value })} required />
        </label>
        <label className="grid gap-1 text-sm">
          Slug
          <input className="field" value={meta.slug} onChange={(e) => setMeta({ ...meta, slug: e.target.value })} required />
        </label>
        <label className="grid gap-1 text-sm md:col-span-2">
          Описание
          <textarea className="field min-h-20" value={meta.description} onChange={(e) => setMeta({ ...meta, description: e.target.value })} />
        </label>
        <label className="grid gap-1 text-sm">
          Раздел
          <select className="field" value={meta.kind} onChange={(e) => setMeta({ ...meta, kind: e.target.value })}>
            {SKILL_KIND_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
        </label>
        <label className="grid gap-1 text-sm">
          Уровень
          <select className="field" value={meta.level_code} onChange={(e) => setMeta({ ...meta, level_code: e.target.value })}>
            {["A1", "A2", "B1", "B2", "C1", "C2"].map((code) => (
              <option key={code}>{code}</option>
            ))}
          </select>
        </label>
        <label className="grid gap-1 text-sm">
          Порядок
          <input className="field" type="number" value={meta.sort_order} onChange={(e) => setMeta({ ...meta, sort_order: Number(e.target.value) })} />
        </label>
        <label className="grid gap-1 text-sm md:col-span-2">
          Текст / транскрипт
          <textarea className="field min-h-32" value={meta.body} onChange={(e) => setMeta({ ...meta, body: e.target.value })} />
        </label>
        <label className="grid gap-1 text-sm md:col-span-2">
          Реплики диалога (по строке: speaker | english | русский)
          <textarea className="field min-h-28 font-mono text-xs" value={meta.linesText} onChange={(e) => setMeta({ ...meta, linesText: e.target.value })} />
        </label>
        <label className="grid gap-1 text-sm md:col-span-2">
          Ключевые слова (по строке: english | русский)
          <textarea className="field min-h-24 font-mono text-xs" value={meta.keywordsText} onChange={(e) => setMeta({ ...meta, keywordsText: e.target.value })} />
        </label>
        <button className="btn btn-primary justify-self-start">Сохранить материал</button>
        {saved && <p className="text-sm text-sage md:col-span-2">{saved}</p>}
        {error && <p className="text-sm text-rose md:col-span-2">{error}</p>}
      </form>
      <form
        className="card grid gap-3 p-5 md:grid-cols-2"
        onSubmit={async (e) => {
          e.preventDefault();
          setError("");
          try {
            await api("/admin/skills/questions", {
              method: "POST",
              body: JSON.stringify({
                item_id: id,
                kind: questionForm.kind,
                prompt: questionForm.prompt,
                answer: questionForm.answer,
                options: textToList(questionForm.optionsText),
                accepted: textToList(questionForm.acceptedText),
                speak: questionForm.speak,
                explanation: questionForm.explanation,
                sort_order: questionForm.sort_order,
              }),
            });
            setQuestionForm(emptyQuestionForm);
            load();
          } catch (err) {
            setError(err instanceof Error ? err.message : "Не удалось добавить вопрос");
          }
        }}
      >
        <h2 className="font-semibold md:col-span-2">Добавить вопрос</h2>
        <select className="field" value={questionForm.kind} onChange={(e) => setQuestionForm({ ...questionForm, kind: e.target.value })}>
          {SKILL_QUESTION_KIND_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
        <input
          className="field"
          type="number"
          placeholder="Порядок"
          value={questionForm.sort_order}
          onChange={(e) => setQuestionForm({ ...questionForm, sort_order: Number(e.target.value) })}
        />
        <textarea
          className="field md:col-span-2 min-h-20"
          placeholder="Вопрос / задание"
          value={questionForm.prompt}
          onChange={(e) => setQuestionForm({ ...questionForm, prompt: e.target.value })}
          required
        />
        <input
          className="field md:col-span-2"
          placeholder="Правильный ответ"
          value={questionForm.answer}
          onChange={(e) => setQuestionForm({ ...questionForm, answer: e.target.value })}
          required
        />
        <textarea
          className="field md:col-span-2 min-h-20 font-mono text-xs"
          placeholder="Варианты выбора (по строке или через запятую)"
          value={questionForm.optionsText}
          onChange={(e) => setQuestionForm({ ...questionForm, optionsText: e.target.value })}
        />
        <textarea
          className="field md:col-span-2 min-h-16 font-mono text-xs"
          placeholder="Допустимые ответы (по строке или через запятую)"
          value={questionForm.acceptedText}
          onChange={(e) => setQuestionForm({ ...questionForm, acceptedText: e.target.value })}
        />
        <input
          className="field md:col-span-2"
          placeholder="Текст для озвучки (диктант)"
          value={questionForm.speak}
          onChange={(e) => setQuestionForm({ ...questionForm, speak: e.target.value })}
        />
        <input
          className="field md:col-span-2"
          placeholder="Пояснение"
          value={questionForm.explanation}
          onChange={(e) => setQuestionForm({ ...questionForm, explanation: e.target.value })}
        />
        <button className="btn btn-sage justify-self-start">Добавить вопрос</button>
      </form>
      <section className="grid gap-2">
        <h2 className="font-display text-2xl">Вопросы</h2>
        {(data.questions || []).map((item) => (
          <div key={item.id} className="card grid gap-3 p-4 text-sm">
            {editingId === item.id && draft ? (
              <form
                className="grid gap-2 md:grid-cols-2"
                onSubmit={async (e) => {
                  e.preventDefault();
                  setError("");
                  try {
                    await api(`/admin/skills/questions/${item.id}`, {
                      method: "PATCH",
                      body: JSON.stringify({
                        kind: draft.kind,
                        prompt: draft.prompt,
                        answer: draft.answer,
                        options: textToList(draft.optionsText),
                        accepted: textToList(draft.acceptedText),
                        speak: draft.speak,
                        explanation: draft.explanation,
                        sort_order: draft.sort_order,
                      }),
                    });
                    setEditingId(null);
                    setDraft(null);
                    load();
                  } catch (err) {
                    setError(err instanceof Error ? err.message : "Не удалось сохранить вопрос");
                  }
                }}
              >
                <select className="field" value={draft.kind} onChange={(e) => setDraft({ ...draft, kind: e.target.value })}>
                  {SKILL_QUESTION_KIND_OPTIONS.map((opt) => (
                    <option key={opt.value} value={opt.value}>
                      {opt.label}
                    </option>
                  ))}
                </select>
                <input
                  className="field"
                  type="number"
                  value={draft.sort_order}
                  onChange={(e) => setDraft({ ...draft, sort_order: Number(e.target.value) })}
                />
                <textarea className="field md:col-span-2 min-h-20" value={draft.prompt} onChange={(e) => setDraft({ ...draft, prompt: e.target.value })} required />
                <input className="field md:col-span-2" value={draft.answer} onChange={(e) => setDraft({ ...draft, answer: e.target.value })} required />
                <textarea
                  className="field md:col-span-2 min-h-20 font-mono text-xs"
                  value={draft.optionsText}
                  onChange={(e) => setDraft({ ...draft, optionsText: e.target.value })}
                />
                <textarea
                  className="field md:col-span-2 min-h-16 font-mono text-xs"
                  value={draft.acceptedText}
                  onChange={(e) => setDraft({ ...draft, acceptedText: e.target.value })}
                />
                <input className="field md:col-span-2" value={draft.speak} onChange={(e) => setDraft({ ...draft, speak: e.target.value })} />
                <input className="field md:col-span-2" value={draft.explanation} onChange={(e) => setDraft({ ...draft, explanation: e.target.value })} />
                <div className="flex gap-2 md:col-span-2">
                  <button className="btn btn-primary text-sm">Сохранить вопрос</button>
                  <button type="button" className="btn btn-ghost text-sm" onClick={() => { setEditingId(null); setDraft(null); }}>
                    Отмена
                  </button>
                </div>
              </form>
            ) : (
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                  <p className="text-xs text-terra">
                    {SKILL_QUESTION_KIND_OPTIONS.find((o) => o.value === item.kind)?.label ?? item.kind} · порядок {item.sort_order}
                  </p>
                  <p className="font-semibold">{item.prompt}</p>
                  <p>Ответ: {item.answer}</p>
                  {item.options?.length ? <p className="text-ink-soft">Варианты: {item.options.join(" · ")}</p> : null}
                  {item.accepted?.length ? <p className="text-ink-soft">Допустимо: {item.accepted.join(" · ")}</p> : null}
                  {item.speak ? <p className="text-ink-soft">Озвучка: {item.speak}</p> : null}
                  {item.explanation ? <p className="text-ink-soft">{item.explanation}</p> : null}
                </div>
                <div className="flex gap-2">
                  <button
                    className="btn btn-ghost text-xs"
                    onClick={() => {
                      setEditingId(item.id);
                      setDraft({
                        ...item,
                        optionsText: listToText(item.options),
                        acceptedText: listToText(item.accepted),
                      });
                    }}
                  >
                    изменить
                  </button>
                  <button
                    className="text-rose"
                    onClick={async () => {
                      if (confirm("Удалить вопрос?")) {
                        await api(`/admin/skills/questions/${item.id}`, { method: "DELETE" });
                        load();
                      }
                    }}
                  >
                    удалить
                  </button>
                </div>
              </div>
            )}
          </div>
        ))}
      </section>
    </div>
  );
}

