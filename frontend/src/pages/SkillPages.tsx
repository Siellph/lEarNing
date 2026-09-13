import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { ProgressBar } from "../components/ProgressBar";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";
import { speakEnglish } from "../lib/speech";

type SkillKind = "reading" | "listening" | "dialogue";

type SkillSummary = {
  id: number;
  slug: string;
  title: string;
  description: string;
  kind: string;
  level_code: string;
  question_count: number;
  keyword_count: number;
  strength: number;
  learned: boolean;
};

type Keyword = { en: string; ru: string };
type DialogueLine = { speaker: string; text: string; ru?: string };

type SkillDetail = SkillSummary & {
  body: string;
  lines: DialogueLine[];
  keywords: Keyword[];
};

type PracticeItem = {
  uid: string;
  id: number;
  kind: string;
  prompt: string;
  options?: string[] | null;
  speak?: string | null;
  explanation?: string;
};

const META: Record<
  SkillKind,
  { path: string; eyebrow: string; title: string; subtitle: string }
> = {
  reading: {
    path: "reading",
    eyebrow: "Тексты",
    title: "Чтение по уровням",
    subtitle: "Короткие оригинальные тексты A1–B2, ключевые слова и вопросы на понимание.",
  },
  listening: {
    path: "listening",
    eyebrow: "Слух",
    title: "Слушание и диктант",
    subtitle: "Короткие фразы с озвучкой: понимание на слух и набор услышанного.",
  },
  dialogue: {
    path: "dialogues",
    eyebrow: "Речь",
    title: "Мини-диалоги",
    subtitle: "Короткие сцены: скрипт, озвучка реплик, пропуски и понимание.",
  },
};

const KIND_API: Record<SkillKind, string> = {
  reading: "reading",
  listening: "listening",
  dialogue: "dialogue",
};

export function SkillHub({ kind }: { kind: SkillKind }) {
  const [items, setItems] = useState<SkillSummary[]>([]);
  const meta = META[kind];
  useEffect(() => {
    api<SkillSummary[]>(`/skills/${KIND_API[kind]}`).then(setItems);
  }, [kind]);

  const learned = items.filter((i) => i.learned).length;

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">{meta.eyebrow}</p>
        <h1 className="font-display mt-1 text-4xl">{meta.title}</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">{meta.subtitle}</p>
        {items.length > 0 && (
          <div className="mt-4 max-w-md">
            <ProgressBar
              value={(learned / items.length) * 100}
              label={`${learned}/${items.length} освоено`}
            />
          </div>
        )}
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {items.map((item) => (
          <Link
            key={item.slug}
            to={`/app/${meta.path}/${item.slug}`}
            className="card p-5 hover:border-terra/40"
          >
            <div className="flex items-start justify-between gap-3">
              <h2 className="font-display text-2xl">{item.title}</h2>
              <span className="rounded-full bg-paper-2 px-2.5 py-1 text-xs font-semibold text-ink-soft">
                {item.level_code}
              </span>
            </div>
            <p className="mt-2 text-sm text-ink-soft">{item.description}</p>
            <p className="mt-3 text-xs text-ink-soft">
              {item.question_count} заданий
              {item.keyword_count ? ` · ${item.keyword_count} слов` : ""} · сила {item.strength}/5
            </p>
          </Link>
        ))}
        {!items.length && <p className="text-ink-soft">Пока пусто — запустите seed/expand.</p>}
      </div>
    </div>
  );
}

export function SkillItemPage({ kind }: { kind: SkillKind }) {
  const { slug } = useParams();
  const { refresh } = useAuth();
  const meta = META[kind];
  const [item, setItem] = useState<SkillDetail | null>(null);
  const [mode, setMode] = useState<"study" | "practice">("study");
  const [showTranscript, setShowTranscript] = useState(kind !== "listening");
  const [items, setItems] = useState<PracticeItem[]>([]);
  const [index, setIndex] = useState(0);
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState<{
    correct: boolean;
    expected?: string | null;
    explanation?: string;
  } | null>(null);

  const load = () => {
    if (!slug) return;
    api<SkillDetail>(`/skills/${KIND_API[kind]}/${slug}`).then(setItem);
  };

  useEffect(() => {
    setMode("study");
    setShowTranscript(kind !== "listening");
    setItems([]);
    setIndex(0);
    setAnswer("");
    setFeedback(null);
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [kind, slug]);

  const startPractice = async () => {
    if (!slug) return;
    const data = await api<{ items: PracticeItem[] }>(`/skills/${KIND_API[kind]}/${slug}/practice`);
    setItems(data.items);
    setIndex(0);
    setAnswer("");
    setFeedback(null);
    setMode("practice");
  };

  const current = items[index];

  useEffect(() => {
    if (mode !== "practice" || !current) return;
    if (current.kind === "dictation" && current.speak) {
      speakEnglish(current.speak);
    }
  }, [mode, current?.uid, current?.kind, current?.speak]);

  const check = async () => {
    if (!current) return;
    const res = await api<{
      correct: boolean;
      expected?: string | null;
      explanation?: string;
    }>(`/skills/questions/${current.id}/check`, {
      method: "POST",
      body: JSON.stringify({ answer, kind: current.kind }),
    });
    setFeedback(res);
    refresh();
  };

  const next = () => {
    setFeedback(null);
    setAnswer("");
    if (index + 1 >= items.length) {
      setMode("study");
      load();
      return;
    }
    setIndex((i) => i + 1);
  };

  if (!item) return <p className="text-ink-soft">Загружаем…</p>;

  return (
    <div className="mx-auto grid max-w-3xl gap-5">
      <div>
        <Link to={`/app/${meta.path}`} className="text-sm text-terra">
          ← Назад
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-2">
          <h1 className="font-display text-4xl">{item.title}</h1>
          <span className="rounded-full bg-card px-3 py-1 text-sm text-ink-soft">{item.level_code}</span>
        </div>
        <p className="mt-1 text-ink-soft">{item.description}</p>
      </div>

      <div className="flex flex-wrap items-center gap-2">
        <VoiceControls />
        {kind === "listening" && (
          <button
            type="button"
            className="btn btn-ghost text-sm"
            onClick={() => setShowTranscript((v) => !v)}
          >
            {showTranscript ? "Скрыть текст" : "Показать текст"}
          </button>
        )}
        <button className="btn btn-primary ml-auto text-sm" onClick={startPractice}>
          Практика
        </button>
      </div>

      {mode === "study" ? (
        <div className="grid gap-4">
          {kind === "dialogue" ? (
            <article className="card grid gap-3 p-5">
              <p className="text-xs uppercase tracking-wide text-ink-soft">{item.body || "Сцена"}</p>
              {item.lines.map((line, i) => (
                <div key={`${line.speaker}-${i}`} className="rounded-xl bg-paper px-4 py-3">
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <p className="text-xs font-semibold text-terra">{line.speaker}</p>
                      <p className="mt-1 text-lg">{line.text}</p>
                      {line.ru && <p className="mt-1 text-sm text-ink-soft">{line.ru}</p>}
                    </div>
                    <SpeakButton text={line.text} label="реплика" />
                  </div>
                </div>
              ))}
            </article>
          ) : (
            <article className="card grid gap-3 p-5">
              <div className="flex items-center justify-between gap-3">
                <p className="text-xs uppercase tracking-wide text-ink-soft">
                  {kind === "listening" ? "Аудио" : "Текст"}
                </p>
                <SpeakButton text={item.body} label={kind === "listening" ? "Слушать" : "Прочитать"} />
              </div>
              {kind === "listening" && !showTranscript ? (
                <p className="text-ink-soft">Слушайте без текста или откройте расшифровку кнопкой выше.</p>
              ) : (
                <p className="whitespace-pre-wrap text-lg leading-relaxed">{item.body}</p>
              )}
            </article>
          )}

          {item.keywords.length > 0 && (
            <article className="card p-5">
              <h2 className="font-display text-xl">Ключевые слова</h2>
              <ul className="mt-3 grid gap-2 sm:grid-cols-2">
                {item.keywords.map((kw) => (
                  <li key={kw.en} className="flex items-center justify-between gap-2 rounded-xl bg-paper px-3 py-2">
                    <span>
                      <span className="font-semibold">{kw.en}</span>
                      <span className="text-ink-soft"> — {kw.ru}</span>
                    </span>
                    <SpeakButton text={kw.en} label="слово" />
                  </li>
                ))}
              </ul>
            </article>
          )}

          <p className="text-sm text-ink-soft">Сила материала: {item.strength}/5</p>
        </div>
      ) : current ? (
        <article className="card grid gap-4 p-6">
          <div className="flex items-center justify-between gap-3">
            <p className="text-sm text-ink-soft">
              {index + 1} / {items.length}
            </p>
            <span className="rounded-full bg-paper-2 px-2.5 py-1 text-xs font-semibold text-ink-soft">
              {current.kind === "dictation"
                ? "Диктант"
                : current.kind === "fill_gap"
                  ? "Пропуск"
                  : "Понимание"}
            </span>
          </div>
          <p className="text-xl">{current.prompt}</p>
          {current.kind === "dictation" && current.speak && (
            <div className="flex justify-end">
              <SpeakButton text={current.speak} label="Ещё раз" />
            </div>
          )}
          {current.options ? (
            <div className="grid gap-2">
              {current.options.map((opt) => (
                <button
                  key={opt}
                  type="button"
                  className={`rounded-xl border px-4 py-3 text-left ${
                    answer === opt ? "border-terra bg-[#fff1eb]" : "border-line"
                  }`}
                  onClick={() => setAnswer(opt)}
                >
                  {opt}
                </button>
              ))}
            </div>
          ) : (
            <input
              className="field"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              placeholder={current.kind === "dictation" ? "Что услышали…" : "Ответ"}
              autoComplete="off"
            />
          )}
          <div className="flex flex-wrap gap-3">
            {!feedback ? (
              <button className="btn btn-primary" disabled={!answer.trim()} onClick={check}>
                Проверить
              </button>
            ) : (
              <button className="btn btn-sage" onClick={next}>
                {index + 1 >= items.length ? "Готово" : "Дальше"}
              </button>
            )}
            {feedback && (
              <span className={feedback.correct ? "text-sage" : "text-rose"}>
                {feedback.correct ? "Верно" : `Ответ: ${feedback.expected}`}
              </span>
            )}
          </div>
          {feedback && !feedback.correct && feedback.explanation && (
            <p className="text-sm text-ink-soft">{feedback.explanation}</p>
          )}
        </article>
      ) : (
        <p className="text-ink-soft">Нет заданий для практики.</p>
      )}
    </div>
  );
}
