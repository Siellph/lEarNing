import {
  useEffect,
  useMemo,
  useRef,
  useState,
  type CSSProperties,
  type MutableRefObject,
} from "react";
import { CheckCircle2, CircleAlert } from "lucide-react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import { api } from "../api/client";
import { SpeakButton } from "../components/SpeakButton";
import { speakEnglish, stopSpeech, mapSpeakersToGender, type DialogueSpeakLine } from "../lib/speech";
import { SEARCH_HIGHLIGHT_PARAM, useSearchHighlight } from "../lib/searchHighlight";

const FEEDBACK_ADVANCE_MS = 1500;

type CheckResult = {
  correct: boolean;
  expected?: string | null;
  explanation?: string;
};

type SkillKind = "reading" | "listening" | "dialogue";

const CEFR_LEVELS = ["A1", "A2", "B1", "B2", "B2+", "C1", "C2"] as const;

type SkillSummary = {
  id: number;
  slug: string;
  title: string;
  description: string;
  kind: string;
  level_code: string;
  question_count: number;
  keyword_count: number;
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
    subtitle: "Оригинальные тексты A1–C2: от коротких абзацев до статей, ключевые слова и вопросы на понимание.",
  },
  listening: {
    path: "listening",
    eyebrow: "Слух",
    title: "Аудирование и диктант",
    subtitle: "Пассажи с озвучкой A1–C2: понимание на слух и набор услышанного.",
  },
  dialogue: {
    path: "dialogues",
    eyebrow: "Речь",
    title: "Диалоги",
    subtitle: "Развёрнутые сцены A1–C2: скрипт, озвучка реплик, пропуски и понимание.",
  },
};

const KIND_API: Record<SkillKind, string> = {
  reading: "reading",
  listening: "listening",
  dialogue: "dialogue",
};

function DialogueThread({ body, lines }: { body: string; lines: DialogueLine[] }) {
  const firstSpeaker = useMemo(() => {
    for (const line of lines) {
      const name = line.speaker.trim();
      if (name) return name;
    }
    return lines[0]?.speaker ?? "";
  }, [lines]);

  // First unique speaker → female voice, second → male (then alternate).
  const speakerGenders = useMemo(
    () => mapSpeakersToGender(lines.map((line) => line.speaker)),
    [lines],
  );

  const dialogueSpeakLines = useMemo((): DialogueSpeakLine[] => {
    return lines
      .filter((line) => line.text.trim())
      .map((line) => ({
        text: line.text,
        voiceGender: speakerGenders.get(line.speaker.trim()) ?? "female",
      }));
  }, [lines, speakerGenders]);

  const fullScript = useMemo(
    () => lines.map((line) => line.text).filter(Boolean).join(". "),
    [lines],
  );

  return (
    <article className="card grid min-w-0 gap-4 p-4 sm:p-5">
      <div className="flex items-center justify-between gap-2">
        <p className="min-w-0 flex-1 truncate text-xs uppercase tracking-wide text-ink-soft">
          {body || "Сцена"}
        </p>
        {dialogueSpeakLines.length ? (
          <SpeakButton
            text={fullScript}
            dialogueLines={dialogueSpeakLines}
            label="Весь диалог"
            compact
            showRestart
            className="shrink-0"
          />
        ) : null}
      </div>
      <div className="grid min-w-0 gap-3.5" role="log" aria-label="Диалог">
        {lines.map((line, i) => {
          const isLeft = line.speaker.trim() === firstSpeaker || (!firstSpeaker && i % 2 === 0);
          const voiceGender = speakerGenders.get(line.speaker.trim()) ?? "female";
          return (
            <div
              key={`${line.speaker}-${i}`}
              className={`motion-bubble flex min-w-0 ${isLeft ? "justify-start" : "justify-end"}`}
              style={{ "--motion-i": Math.min(i, 10) } as CSSProperties}
            >
              <div
                className={`flex w-full max-w-[min(100%,22rem)] min-w-0 flex-col ${
                  isLeft ? "items-start" : "items-end"
                }`}
              >
                <div
                  className={`mb-1 flex max-w-full items-center gap-1 ${
                    isLeft ? "flex-row" : "flex-row-reverse"
                  }`}
                >
                  <p className="min-w-0 truncate text-[11px] font-semibold tracking-wide text-ink-soft/80">
                    {line.speaker}
                  </p>
                  <SpeakButton
                    text={line.text}
                    label="реплика"
                    voiceGender={voiceGender}
                    compact
                    showRestart
                    className="shrink-0"
                  />
                </div>
                <div
                  className={`max-w-full px-3.5 py-2.5 ${
                    isLeft
                      ? "rounded-2xl rounded-tl-md border border-line/70 bg-paper-2 text-ink"
                      : "rounded-2xl rounded-tr-md border border-sage/25 bg-sage-soft text-ink"
                  }`}
                >
                  <p className="break-words text-lg leading-snug">{line.text}</p>
                </div>
                {line.ru ? (
                  <p
                    className={`mt-1 max-w-full break-words text-sm leading-snug text-ink-soft/70 ${
                      isLeft ? "text-left" : "text-right"
                    }`}
                  >
                    {line.ru}
                  </p>
                ) : null}
              </div>
            </div>
          );
        })}
      </div>
    </article>
  );
}

export function SkillHub({ kind }: { kind: SkillKind }) {
  const [items, setItems] = useState<SkillSummary[]>([]);
  const [levelFilter, setLevelFilter] = useState<string>("all");
  const [searchParams] = useSearchParams();
  const meta = META[kind];
  useEffect(() => {
    setLevelFilter("all");
    api<SkillSummary[]>(`/skills/${KIND_API[kind]}`).then(setItems);
  }, [kind]);
  useEffect(() => {
    if (searchParams.get(SEARCH_HIGHLIGHT_PARAM)) setLevelFilter("all");
  }, [searchParams]);
  useSearchHighlight(items.length > 0 && levelFilter === "all");

  const levelOptions = useMemo(() => {
    const present = new Set(items.map((i) => i.level_code));
    const ordered = CEFR_LEVELS.filter((code) => present.has(code));
    const extras = [...present].filter((code) => !CEFR_LEVELS.includes(code as (typeof CEFR_LEVELS)[number]));
    extras.sort();
    return [...ordered, ...extras];
  }, [items]);

  const filtered = useMemo(() => {
    if (levelFilter === "all") return items;
    return items.filter((i) => i.level_code === levelFilter);
  }, [items, levelFilter]);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">{meta.eyebrow}</p>
        <h1 className="font-display mt-1 text-4xl">{meta.title}</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">{meta.subtitle}</p>
      </div>

      {levelOptions.length > 0 && (
        <div className="flex flex-wrap items-center gap-2" role="group" aria-label="Фильтр по уровню CEFR">
          <button
            type="button"
            className={`rounded-full px-3 py-1.5 text-sm font-semibold transition ${
              levelFilter === "all"
                ? "bg-terra text-white"
                : "bg-paper-2 text-ink-soft hover:bg-paper"
            }`}
            onClick={() => setLevelFilter("all")}
          >
            Все
          </button>
          {levelOptions.map((code) => {
            const count = items.filter((i) => i.level_code === code).length;
            const active = levelFilter === code;
            return (
              <button
                key={code}
                type="button"
                className={`rounded-full px-3 py-1.5 text-sm font-semibold transition ${
                  active ? "bg-terra text-white" : "bg-paper-2 text-ink-soft hover:bg-paper"
                }`}
                onClick={() => setLevelFilter(code)}
                aria-pressed={active}
              >
                {code}
                <span className={`ml-1.5 text-xs ${active ? "text-white/80" : "text-ink-soft/80"}`}>
                  {count}
                </span>
              </button>
            );
          })}
        </div>
      )}

      <div className="grid gap-4 md:grid-cols-2">
        {filtered.map((item) => (
          <Link
            key={item.slug}
            to={`/app/${meta.path}/${item.slug}`}
            data-search-id={item.slug}
            className="card card-lift p-5"
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
              {item.keyword_count ? ` · ${item.keyword_count} слов` : ""}
            </p>
          </Link>
        ))}
        {!items.length && <p className="text-ink-soft">Пока пусто — запустите seed/expand.</p>}
        {!!items.length && !filtered.length && (
          <p className="text-ink-soft">Нет материалов для уровня {levelFilter}.</p>
        )}
      </div>
    </div>
  );
}

function skillKindLabel(kind: string): string {
  if (kind === "dictation") return "Диктант";
  if (kind === "fill_gap") return "Пропуск";
  return "Понимание";
}

function SkillKindBadge({ kind }: { kind: string }) {
  return (
    <span className="rounded-full bg-paper-2 px-2.5 py-1 text-xs font-semibold text-ink-soft">
      {skillKindLabel(kind)}
    </span>
  );
}

function SkillCardResultIcon({ correct }: { correct: boolean }) {
  return correct ? (
    <span className="quiz-status-ok quiz-status-icon" aria-label="Верно" role="status">
      <CheckCircle2 size={20} aria-hidden />
    </span>
  ) : (
    <span className="quiz-status-bad quiz-status-icon" aria-label="Неверно" role="status">
      <CircleAlert size={20} aria-hidden />
    </span>
  );
}

function useSkillAutoAdvance(
  result: CheckResult | null,
  item: PracticeItem,
  resolvedRef: MutableRefObject<boolean>,
  onResolvedRef: MutableRefObject<(res: CheckResult) => void>,
) {
  useEffect(() => {
    if (!result) return;
    const timer = window.setTimeout(() => {
      if (resolvedRef.current) return;
      resolvedRef.current = true;
      onResolvedRef.current(result);
    }, FEEDBACK_ADVANCE_MS);
    return () => window.clearTimeout(timer);
  }, [result, item, resolvedRef, onResolvedRef]);
}

function SkillChoiceQuestion({
  item,
  index,
  progressLabel,
  onCheck,
  onResolved,
}: {
  item: PracticeItem;
  index: number;
  progressLabel: string;
  onCheck: (item: PracticeItem, answer: string) => Promise<CheckResult>;
  onResolved: (res: CheckResult) => void;
}) {
  const options = useMemo(() => [...(item.options || [])].sort(() => Math.random() - 0.5), [item.uid]);
  const [value, setValue] = useState("");
  const [result, setResult] = useState<CheckResult | null>(null);
  const [busy, setBusy] = useState(false);
  const resolvedRef = useRef(false);
  const onResolvedRef = useRef(onResolved);
  onResolvedRef.current = onResolved;
  const locked = !!result;

  useSkillAutoAdvance(result, item, resolvedRef, onResolvedRef);

  const submit = async (answer: string) => {
    if (!answer || locked || busy || resolvedRef.current) return;
    setBusy(true);
    setValue(answer);
    try {
      const res = await onCheck(item, answer);
      setResult(res);
    } finally {
      setBusy(false);
    }
  };

  return (
    <article
      className={`quiz-card motion-enter ${result ? (result.correct ? "quiz-card-ok" : "quiz-card-bad quiz-card-shake") : ""}`}
      style={{ "--motion-i": Math.min(index, 8) } as CSSProperties}
    >
      <header className="quiz-card-head">
        <div className="flex min-w-0 flex-wrap items-center gap-2">
          <span className="text-sm text-ink-soft">{progressLabel}</span>
          <SkillKindBadge kind={item.kind} />
        </div>
        {result && <SkillCardResultIcon correct={result.correct} />}
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <p className="text-lg">{item.prompt}</p>
        <div className="grid gap-2.5">
          {options.map((opt) => (
            <button
              key={opt}
              type="button"
              disabled={locked || busy}
              onClick={() => void submit(opt)}
              className={`quiz-choice ${value === opt ? "is-selected" : ""}`}
            >
              {opt}
            </button>
          ))}
        </div>
      </div>
    </article>
  );
}

function SkillTypeQuestion({
  item,
  index,
  progressLabel,
  onCheck,
  onResolved,
}: {
  item: PracticeItem;
  index: number;
  progressLabel: string;
  onCheck: (item: PracticeItem, answer: string) => Promise<CheckResult>;
  onResolved: (res: CheckResult) => void;
}) {
  const [value, setValue] = useState("");
  const [result, setResult] = useState<CheckResult | null>(null);
  const [busy, setBusy] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const resolvedRef = useRef(false);
  const onResolvedRef = useRef(onResolved);
  onResolvedRef.current = onResolved;
  const locked = !!result;
  const isDictation = item.kind === "dictation";

  useSkillAutoAdvance(result, item, resolvedRef, onResolvedRef);

  useEffect(() => {
    if (isDictation && item.speak) speakEnglish(item.speak);
    return () => stopSpeech();
  }, [item.uid, isDictation, item.speak]);

  const submit = async () => {
    if (!value.trim() || locked || busy || resolvedRef.current) return;
    inputRef.current?.blur();
    setBusy(true);
    try {
      const res = await onCheck(item, value.trim());
      setResult(res);
    } finally {
      setBusy(false);
    }
  };

  return (
    <article
      className={`quiz-card motion-enter ${result ? (result.correct ? "quiz-card-ok" : "quiz-card-bad quiz-card-shake") : ""}`}
      style={{ "--motion-i": Math.min(index, 8) } as CSSProperties}
    >
      <header className="quiz-card-head">
        <div className="flex min-w-0 flex-wrap items-center gap-2">
          <span className="text-sm text-ink-soft">{progressLabel}</span>
          <SkillKindBadge kind={item.kind} />
        </div>
        {result && <SkillCardResultIcon correct={result.correct} />}
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-lg">{item.prompt}</p>
          {isDictation && item.speak ? <SpeakButton text={item.speak} label="Ещё раз" /> : null}
        </div>
        <input
          ref={inputRef}
          className="field"
          value={value}
          autoCapitalize="none"
          autoCorrect="off"
          autoComplete="off"
          spellCheck={false}
          placeholder={isDictation ? "Что услышали…" : "Ответ"}
          onChange={(event) => setValue(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter") {
              event.preventDefault();
              void submit();
            }
          }}
          disabled={locked}
        />
        {!result && (
          <button
            type="button"
            className="btn btn-primary w-full sm:w-auto sm:justify-self-start"
            disabled={busy || !value.trim()}
            onClick={() => void submit()}
          >
            {busy ? "Проверяем…" : "Проверить"}
          </button>
        )}
      </div>
    </article>
  );
}

function SkillPracticeCard({
  item,
  index,
  total,
  onCheck,
  onResolved,
}: {
  item: PracticeItem;
  index: number;
  total: number;
  onCheck: (item: PracticeItem, answer: string) => Promise<CheckResult>;
  onResolved: (res: CheckResult) => void;
}) {
  const progressLabel = `${index + 1} / ${total}`;
  const isChoice = Array.isArray(item.options) && item.options.length > 0;
  if (isChoice) {
    return (
      <SkillChoiceQuestion
        item={item}
        index={index}
        progressLabel={progressLabel}
        onCheck={onCheck}
        onResolved={onResolved}
      />
    );
  }
  return (
    <SkillTypeQuestion
      item={item}
      index={index}
      progressLabel={progressLabel}
      onCheck={onCheck}
      onResolved={onResolved}
    />
  );
}

export function SkillItemPage({ kind }: { kind: SkillKind }) {
  const { slug } = useParams();
  const meta = META[kind];
  const [item, setItem] = useState<SkillDetail | null>(null);
  const [mode, setMode] = useState<"study" | "practice" | "done">("study");
  const [showTranscript, setShowTranscript] = useState(kind !== "listening");
  const [items, setItems] = useState<PracticeItem[]>([]);
  const [index, setIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [sessionTotal, setSessionTotal] = useState(0);

  const load = () => {
    if (!slug) return;
    api<SkillDetail>(`/skills/${KIND_API[kind]}/${slug}`).then(setItem);
  };

  useEffect(() => {
    setMode("study");
    setShowTranscript(kind !== "listening");
    setItems([]);
    setIndex(0);
    setCorrectCount(0);
    setSessionTotal(0);
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [kind, slug]);

  const startPractice = async () => {
    if (!slug) return;
    const data = await api<{ items: PracticeItem[] }>(`/skills/${KIND_API[kind]}/${slug}/practice`);
    setItems(data.items);
    setIndex(0);
    setCorrectCount(0);
    setSessionTotal(data.items.length);
    setMode("practice");
  };

  const finishToStudy = () => {
    setMode("study");
    setItems([]);
    setIndex(0);
  };

  const current = items[index];

  const checkAnswer = async (practiceItem: PracticeItem, answer: string): Promise<CheckResult> => {
    return api<CheckResult>(`/skills/questions/${practiceItem.id}/check`, {
      method: "POST",
      body: JSON.stringify({ answer, kind: practiceItem.kind }),
    });
  };

  const advance = (res: CheckResult) => {
    setCorrectCount((count) => count + (res.correct ? 1 : 0));
    if (index + 1 >= items.length) {
      setMode("done");
      setItems([]);
      setIndex(0);
      return;
    }
    setIndex((i) => i + 1);
  };

  if (!item) return <p className="text-ink-soft">Загружаем…</p>;

  return (
    <div className="mx-auto grid min-w-0 max-w-3xl gap-5">
      <div className="min-w-0">
        <Link to={`/app/${meta.path}`} className="text-sm text-terra">
          ← Назад
        </Link>
        <div className="mt-2 flex min-w-0 flex-wrap items-center gap-2">
          <h1 className="font-display min-w-0 break-words text-3xl sm:text-4xl">{item.title}</h1>
          <span className="rounded-full bg-card px-3 py-1 text-sm text-ink-soft">{item.level_code}</span>
        </div>
        <p className="mt-1 break-words text-ink-soft">{item.description}</p>
      </div>

      {mode !== "practice" && mode !== "done" && (
        <div className="flex min-w-0 flex-wrap items-center gap-2">
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
      )}

      {mode === "study" ? (
        <div className="grid gap-4">
          {kind === "dialogue" ? (
            <DialogueThread body={item.body} lines={item.lines} />
          ) : (
            <article className="card grid gap-3 p-5">
              <div className="flex items-center justify-between gap-3">
                <p className="text-xs uppercase tracking-wide text-ink-soft">
                  {kind === "listening" ? "Аудио" : "Текст"}
                </p>
                <SpeakButton
                  text={item.body}
                  label={kind === "listening" ? "Слушать" : "Прочитать"}
                  showRestart
                />
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
        </div>
      ) : mode === "done" ? (
        <section className="card grid gap-4 p-6 motion-enter">
          <p className="text-sm uppercase tracking-[0.18em] text-terra">Практика завершена</p>
          <h2 className="font-display text-3xl">
            Верно {correctCount} из {sessionTotal}
          </h2>
          <div className="flex flex-wrap gap-2">
            <button type="button" className="btn btn-primary" onClick={startPractice}>
              Ещё раз
            </button>
            <button type="button" className="btn btn-ghost" onClick={finishToStudy}>
              К материалу
            </button>
          </div>
        </section>
      ) : current ? (
        <SkillPracticeCard
          key={current.uid}
          item={current}
          index={index}
          total={items.length}
          onCheck={checkAnswer}
          onResolved={advance}
        />
      ) : (
        <p className="text-ink-soft">Нет заданий для практики.</p>
      )}
    </div>
  );
}
