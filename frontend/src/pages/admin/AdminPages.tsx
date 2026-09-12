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
    ["/admin/exams", "Экзамены", false],
    ["/admin/donation", "Чаевые", false],
  ] as const;

  return (
    <div className="surface-grid h-full overflow-y-auto">
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
    { id: number; email: string; name: string; role: string; is_active: boolean; xp: number; streak: number }[]
  >([]);
  useEffect(() => {
    api("/admin/users").then(setUsers);
  }, []);

  const patch = async (id: number, body: object) => {
    await api(`/admin/users/${id}`, { method: "PATCH", body: JSON.stringify(body) });
    api("/admin/users").then(setUsers);
  };

  return (
    <div className="card overflow-x-auto">
      <table className="w-full min-w-[720px] text-left text-sm">
        <thead className="text-ink-soft">
          <tr>
            <th className="px-4 py-3">Имя</th>
            <th>Email</th>
            <th>Роль</th>
            <th>XP</th>
            <th>Статус</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u.id} className="border-t border-line">
              <td className="px-4 py-3 font-medium">{u.name}</td>
              <td>{u.email}</td>
              <td>
                <select className="field !py-1" value={u.role} onChange={(e) => patch(u.id, { role: e.target.value })}>
                  <option value="student">ученик</option>
                  <option value="admin">админ</option>
                </select>
              </td>
              <td>{u.xp}</td>
              <td>
                <button className="btn btn-ghost text-xs" onClick={() => patch(u.id, { is_active: !u.is_active })}>
                  {u.is_active ? "Активен" : "Отключён"}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
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

export function AdminModuleContent() {
  const { moduleId } = useParams();
  const id = Number(moduleId);
  const [data, setData] = useState<{
    module: { id: number; title: string; slug: string };
    lessons: { id: number; title: string }[];
    exercises: { id: number; kind: string; prompt: string; answer: string }[];
    test: { id: number; title: string; questions: { id: number; kind: string; prompt: string; answer: string }[] } | null;
  } | null>(null);
  const [ex, setEx] = useState({ kind: "fill_blank", prompt: "", answer: "", explanation: "Проверьте форму.", options: "" });
  const [tq, setTq] = useState({ kind: "fill_blank", prompt: "", answer: "", explanation: "Проверьте форму.", options: "" });

  const load = () => api(`/admin/modules/${id}/content`).then(setData);
  useEffect(() => {
    load();
  }, [id]);

  if (!data) return <p>Загружаем…</p>;

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
        <select className="field" value={ex.kind} onChange={(e) => setEx({ ...ex, kind: e.target.value })}>
          <option value="multiple_choice">Выбор</option>
          <option value="fill_blank">Пропуск</option>
          <option value="transform">Преобразование</option>
          <option value="error_correction">Исправление</option>
        </select>
        <input className="field" placeholder="Задание" value={ex.prompt} onChange={(e) => setEx({ ...ex, prompt: e.target.value })} required />
        <input className="field" placeholder="Варианты через | (для выбора)" value={ex.options} onChange={(e) => setEx({ ...ex, options: e.target.value })} />
        <input className="field" placeholder="Ответ" value={ex.answer} onChange={(e) => setEx({ ...ex, answer: e.target.value })} required />
        <button className="btn btn-primary justify-self-start">Добавить в практику</button>
      </form>
      <div className="grid gap-2">
        {data.exercises.map((item) => (
          <div key={item.id} className="card flex justify-between gap-3 p-4 text-sm">
            <span>
              <b>{item.kind}</b>: {item.prompt} → {item.answer}
            </span>
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
        ))}
      </div>
      {data.test && (
        <section className="grid gap-3">
          <h2 className="font-display text-2xl">Вопросы теста модуля</h2>
          <p className="text-sm text-ink-soft">
            Тест хранится в базе. Здесь можно добавить новый вопрос — он сразу появится у учеников.
          </p>
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
            <select className="field" value={tq.kind} onChange={(e) => setTq({ ...tq, kind: e.target.value })}>
              <option value="multiple_choice">Выбор</option>
              <option value="fill_blank">Пропуск</option>
              <option value="transform">Преобразование</option>
              <option value="error_correction">Исправление</option>
            </select>
            <input className="field" placeholder="Вопрос теста" value={tq.prompt} onChange={(e) => setTq({ ...tq, prompt: e.target.value })} required />
            <input className="field" placeholder="Варианты через |" value={tq.options} onChange={(e) => setTq({ ...tq, options: e.target.value })} />
            <input className="field" placeholder="Ответ" value={tq.answer} onChange={(e) => setTq({ ...tq, answer: e.target.value })} required />
            <button className="btn btn-sage justify-self-start">Добавить в тест</button>
          </form>
          {data.test.questions.map((item) => (
            <div key={item.id} className="card flex justify-between gap-3 p-4 text-sm">
              <span>
                <b>{item.kind}</b>: {item.prompt} → {item.answer}
              </span>
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
    questions: { id: number; kind: string; prompt: string; answer: string }[];
  } | null>(null);
  const [form, setForm] = useState({ kind: "fill_blank", prompt: "", answer: "", explanation: "Разберите правило.", options: "" });
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
        </select>
        <input className="field" placeholder="Вопрос" value={form.prompt} onChange={(e) => setForm({ ...form, prompt: e.target.value })} required />
        <input className="field" placeholder="Варианты через |" value={form.options} onChange={(e) => setForm({ ...form, options: e.target.value })} />
        <input className="field" placeholder="Ответ" value={form.answer} onChange={(e) => setForm({ ...form, answer: e.target.value })} required />
        <button className="btn btn-primary justify-self-start">Сохранить в БД</button>
      </form>
      {data.questions.map((item) => (
        <div key={item.id} className="card flex justify-between gap-3 p-4 text-sm">
          <span>
            <b>{item.kind}</b>: {item.prompt} → {item.answer}
          </span>
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
      ))}
    </div>
  );
}

export function AdminDonation() {
  const [form, setForm] = useState({
    donation_enabled: false,
    donation_title: "Сайт оказался полезным?",
    donation_message: "Если lEarNing помогает учить EN, можно оставить чаевые.",
    donation_url: "",
    donation_button: "Оставить чаевые",
  });
  const [saved, setSaved] = useState("");

  useEffect(() => {
    api<typeof form>("/admin/donation").then(setForm);
  }, []);

  return (
    <div className="grid gap-6">
      <div>
        <h1 className="font-display text-3xl">Плашка с чаевыми</h1>
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
