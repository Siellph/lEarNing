import { useCallback, useEffect, useMemo, useRef, useState, type CSSProperties, type MutableRefObject } from "react";
import { CheckCircle2, CircleAlert } from "lucide-react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import { api } from "../api/client";
import { ProgressBar } from "../components/ProgressBar";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";
import { percent } from "../lib/percent";
import { looksEnglish } from "../lib/speech";
import { useSearchHighlight } from "../lib/searchHighlight";

type Topic = {
  id: number;
  slug: string;
  title: string;
  description: string;
  level_code: string;
  word_count: number;
  learned_count: number;
  batch_count: number;
  suggested_batch: number;
};

type Word = {
  id: number;
  word: string;
  transcription: string;
  translation: string;
  part_of_speech: string;
  example: string;
  example_translation: string;
  strength: number;
  mastery?: number;
  mastery_count?: number;
  learned?: boolean;
  role?: "new" | "review";
};

type TopicDetail = {
  slug: string;
  title: string;
  description: string;
  level_code: string;
  word_count: number;
  learned_count: number;
  batch_size: number;
  batch_index: number;
  batch_count: number;
  batch_learned: number;
  suggested_batch: number;
  words: Word[];
};

type ExerciseItem = {
  uid: string;
  id: number;
  kind: string;
  prompt: string;
  options?: string[] | null;
  speak?: string | null;
  hint?: string;
  example?: string;
  example_translation?: string;
  target?: string;
};

type PracticePack = {
  topic: { slug: string; title: string };
  batch_index: number;
  batch_count: number;
  new_count: number;
  review_count: number;
  word_count: number;
  learned_count: number;
  batch_learned: number;
  batch_word_count: number;
  pending_tasks: number;
  items: ExerciseItem[];
};

type CheckResult = {
  correct: boolean;
  word: string;
  translation: string;
  example: string;
  strength: number;
  mastery?: number;
  mastery_count?: number;
  learned?: boolean;
  expected?: string | null;
};

export function VocabPage() {
  const [topics, setTopics] = useState<Topic[]>([]);
  useEffect(() => {
    api<Topic[]>("/vocab/topics").then(setTopics);
  }, []);
  useSearchHighlight(topics.length > 0);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Лексика</p>
        <h1 className="font-display mt-1 text-4xl">Тематические словари</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">
          Учите партиями: сначала карточки, затем тренировка — четыре задания на слово (выбор и набор
          в обе стороны). Ошибка сразу переходит к следующему заданию; повторить можно в следующей
          тренировке. Слово выучено, когда все четыре верны. Правила чтения — в разделе{" "}
          <Link to="/app/sounds" className="text-terra">
            Звуки
          </Link>
          .
        </p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {topics.map((topic) => (
          <Link key={topic.slug} to={`/app/vocab/${topic.slug}`} data-search-id={topic.slug} className="card card-lift p-5">
            <p className="text-sm font-semibold text-terra">{topic.level_code}</p>
            <h2 className="font-display text-2xl">{topic.title}</h2>
            <p className="mt-2 text-sm text-ink-soft">{topic.description}</p>
            <div className="mt-4">
              <ProgressBar
                value={percent(topic.learned_count, topic.word_count)}
                label={`${topic.learned_count}/${topic.word_count} выучено · партия ${topic.suggested_batch} из ${topic.batch_count}`}
              />
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export function VocabTopicPage() {
  const { slug } = useParams();
  const [searchParams] = useSearchParams();
  const batchFromUrl = searchParams.get("batch");
  const highlightFromUrl = searchParams.get("highlight");
  const { refresh } = useAuth();
  const [topic, setTopic] = useState<TopicDetail | null>(null);
  const [batch, setBatch] = useState<number | null>(null);
  const [mode, setMode] = useState<"cards" | "practice">("cards");
  const [practice, setPractice] = useState<PracticePack | null>(null);
  const [busy, setBusy] = useState(false);

  const loadTopic = (nextBatch?: number) => {
    if (!slug) return;
    const query = nextBatch ? `?batch=${nextBatch}` : "";
    api<TopicDetail>(`/vocab/topics/${slug}${query}`).then((data) => {
      setTopic(data);
      setBatch(data.batch_index);
    });
  };

  useEffect(() => {
    const initial = batchFromUrl ? Number(batchFromUrl) : undefined;
    if (highlightFromUrl) {
      setMode("cards");
      setPractice(null);
    }
    loadTopic(Number.isFinite(initial) && initial && initial > 0 ? initial : undefined);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [slug, batchFromUrl, highlightFromUrl]);
  useSearchHighlight(!!topic && mode === "cards" && topic.slug === slug);

  const startPractice = async () => {
    if (!slug) return;
    setBusy(true);
    try {
      const data = await api<PracticePack>(`/vocab/topics/${slug}/practice${batch ? `?batch=${batch}` : ""}`);
      setPractice(data);
      setMode("practice");
    } finally {
      setBusy(false);
    }
  };

  const goBatch = (index: number) => {
    setMode("cards");
    setPractice(null);
    loadTopic(index);
  };

  if (!topic) return <p className="text-ink-soft">Открываем тему…</p>;

  return (
    <div className="grid gap-6">
      <div>
        <Link to="/app/vocab" className="text-sm text-terra">
          ← Все темы
        </Link>
        <div className="mt-2 flex flex-wrap items-center justify-between gap-3">
          <div>
            <p className="text-sm font-semibold text-terra">{topic.level_code}</p>
            <h1 className="font-display text-4xl">{topic.title}</h1>
          </div>
          <VoiceControls />
        </div>
        <p className="mt-2 max-w-2xl text-ink-soft">{topic.description}</p>
        <div className="mt-4">
          <ProgressBar
            value={percent(topic.learned_count, topic.word_count)}
            label={`${topic.learned_count}/${topic.word_count} в теме · партия ${topic.batch_index} из ${topic.batch_count} · ${topic.batch_learned}/${topic.words.length} в этой партии`}
          />
        </div>
        <div className="mt-4 flex flex-wrap gap-2">
          {Array.from({ length: topic.batch_count }, (_, index) => index + 1).map((index) => (
            <button
              key={index}
              type="button"
              className={`btn ${batch === index ? "btn-primary" : "btn-ghost"} text-sm`}
              onClick={() => goBatch(index)}
            >
              Партия {index}
            </button>
          ))}
        </div>
        <div className="mt-4 flex flex-wrap gap-2">
          <button
            className={`btn ${mode === "cards" ? "btn-primary" : "btn-ghost"}`}
            onClick={() => {
              setMode("cards");
              setPractice(null);
            }}
          >
            Карточки
          </button>
          <button className={`btn ${mode === "practice" ? "btn-primary" : "btn-ghost"}`} onClick={startPractice} disabled={busy}>
            {busy ? "Собираем партию…" : "Тренировать партию"}
          </button>
        </div>
      </div>
      {mode === "cards" ? (
        <div className="grid gap-3 md:grid-cols-2">
          {topic.words.map((word) => (
            <StudyCard key={word.id} word={word} />
          ))}
        </div>
      ) : (
        practice && (
          <VocabSession
            pack={practice}
            onCheck={async (item, answer) => {
              const res = await api<CheckResult>(`/vocab/words/${item.id}/check`, {
                method: "POST",
                body: JSON.stringify({
                  answer,
                  kind: item.kind,
                  target: item.target,
                }),
              });
              if (res.correct) refresh();
              return res;
            }}
            onFinished={() => loadTopic(topic.batch_index)}
            onNextBatch={
              topic.batch_index < topic.batch_count
                ? () => {
                    goBatch(topic.batch_index + 1);
                  }
                : undefined
            }
            onRetry={startPractice}
            onBrowse={() => {
              setMode("cards");
              setPractice(null);
              loadTopic(topic.batch_index);
            }}
          />
        )
      )}
    </div>
  );
}

function StudyCard({ word }: { word: Word }) {
  const [open, setOpen] = useState(false);
  const mastered = word.mastery_count ?? word.strength ?? 0;
  return (
    <article data-search-id={String(word.id)} className="card cursor-pointer p-5" onClick={() => setOpen((value) => !value)}>
      <div className="flex items-start justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <p className="font-display text-2xl">{word.word}</p>
            <SpeakButton text={word.word} label="слово" />
          </div>
          <p className="text-sm text-ink-soft">
            {word.transcription} · {word.part_of_speech}
          </p>
        </div>
        <span
          className={`rounded-full px-2 py-1 text-xs ${word.learned ? "bg-sage-soft text-sage" : "bg-paper-2"}`}
          title="Насколько хорошо запомнилась карточка (0–4 грани)"
        >
          {word.learned ? "выучено" : `${Math.min(mastered, 4)}/4`}
        </span>
      </div>
      {open ? (
        <div className="mt-3">
          <p className="font-semibold">{word.translation}</p>
          <div className="mt-2 flex items-start justify-between gap-3">
            <div>
              <p className="text-sm">{word.example}</p>
              <p className="text-sm text-ink-soft">{word.example_translation}</p>
            </div>
            <SpeakButton text={word.example} label="фраза" />
          </div>
        </div>
      ) : (
        <p className="mt-4 text-sm text-ink-soft">Нажмите, чтобы увидеть перевод</p>
      )}
    </article>
  );
}

function VocabSession({
  pack,
  onCheck,
  onFinished,
  onNextBatch,
  onRetry,
  onBrowse,
}: {
  pack: PracticePack;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onFinished: () => void;
  onNextBatch?: () => void;
  onRetry: () => void;
  onBrowse: () => void;
}) {
  const [index, setIndex] = useState(0);
  const [answeredCount, setAnsweredCount] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [wordsMastered, setWordsMastered] = useState(pack.batch_learned || 0);
  const [newlyLearned, setNewlyLearned] = useState<Set<number>>(() => new Set());
  const [failed, setFailed] = useState<FailedFacet[]>([]);
  const [done, setDone] = useState(false);
  const item = pack.items[index];
  const total = pack.items.length;
  const left = Math.max(total - answeredCount, 0);

  useEffect(() => {
    setIndex(0);
    setAnsweredCount(0);
    setCorrectCount(0);
    setWordsMastered(pack.batch_learned || 0);
    setNewlyLearned(new Set());
    setFailed([]);
    setDone(false);
  }, [pack]);

  useEffect(() => {
    if (!total) {
      setDone(true);
      onFinished();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [total]);

  const advance = useCallback(
    (res: CheckResult, current: ExerciseItem) => {
      setAnsweredCount((value) => value + 1);
      if (res.correct) {
        setCorrectCount((value) => value + 1);
        if (res.learned) {
          setNewlyLearned((prev) => {
            if (prev.has(current.id)) return prev;
            setWordsMastered((value) => Math.min(value + 1, pack.batch_word_count || pack.new_count || value + 1));
            return new Set(prev).add(current.id);
          });
        }
      } else {
        setFailed((prev) => [
          ...prev,
          {
            wordId: current.id,
            word: res.word,
            translation: res.translation,
            kind: current.kind,
          },
        ]);
      }

      const nextIndex = index + 1;
      if (nextIndex >= total) {
        setDone(true);
        onFinished();
        return;
      }
      setIndex(nextIndex);
    },
    [index, onFinished, pack.batch_word_count, pack.new_count, total],
  );

  if (!total || done) {
    const cleared = wordsMastered >= (pack.batch_word_count || pack.new_count);
    const reviewGroups = groupFailedFacets(failed);
    return (
      <section className="card grid gap-4 p-6 motion-enter">
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Сессия завершена</p>
        <h2 className="font-display text-3xl">{cleared ? "Партия закрыта" : "Прогресс сохранён"}</h2>
        <p className="text-ink-soft">
          Верно: {correctCount} из {total || answeredCount}. В партии выучено {wordsMastered}/
          {pack.batch_word_count || pack.new_count} слов. В теме {pack.learned_count}/{pack.word_count}.
        </p>
        {reviewGroups.length > 0 ? (
          <div className="grid gap-3">
            <p className="font-semibold">Нужно повторить</p>
            <p className="text-sm text-ink-soft">
              После ошибки мастерство слова сбрасывается — в следующей тренировке снова все 4 задания.
            </p>
            <ul className="grid gap-2">
              {reviewGroups.map((group) => (
                <li key={group.wordId} className="rounded-xl border border-line bg-paper-2/60 px-3 py-2.5">
                  <p className="font-semibold">
                    {group.word} — {group.translation}
                  </p>
                  <p className="mt-1 text-sm text-ink-soft">{group.kinds.map((kind) => KIND_LABEL[kind] || kind).join(" · ")}</p>
                </li>
              ))}
            </ul>
          </div>
        ) : (
          <p className="text-sm text-ink-soft">В этой сессии ошибок не было.</p>
        )}
        <div className="flex flex-wrap gap-2">
          {!cleared && (
            <button type="button" className="btn btn-primary" onClick={onRetry}>
              Добить партию
            </button>
          )}
          {cleared && onNextBatch && (
            <button type="button" className="btn btn-primary" onClick={onNextBatch}>
              Следующая партия
            </button>
          )}
          <button type="button" className="btn btn-ghost" onClick={onBrowse}>
            К карточкам
          </button>
        </div>
      </section>
    );
  }

  return (
    <div className="vocab-session grid gap-4">
      <div className="vocab-session-progress">
        <div className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <p className="text-sm font-semibold text-terra">
              Партия {pack.batch_index} из {pack.batch_count}
            </p>
            <p className="text-sm text-ink-soft">
              Осталось: {left} · выучено слов: {wordsMastered}/{pack.batch_word_count || pack.new_count}
            </p>
          </div>
          <p className="text-sm text-ink-soft">
            {answeredCount + 1} / {total}
          </p>
        </div>
        <ProgressBar value={percent(answeredCount, total)} />
      </div>
      <div className="vocab-session-stage">
        <ExerciseCard key={item.uid} item={item} index={index} onCheck={onCheck} onResolved={advance} />
      </div>
    </div>
  );
}

type FailedFacet = {
  wordId: number;
  word: string;
  translation: string;
  kind: string;
};

function groupFailedFacets(failed: FailedFacet[]) {
  const map = new Map<number, { wordId: number; word: string; translation: string; kinds: string[] }>();
  for (const item of failed) {
    const existing = map.get(item.wordId);
    if (existing) {
      if (!existing.kinds.includes(item.kind)) existing.kinds.push(item.kind);
    } else {
      map.set(item.wordId, {
        wordId: item.wordId,
        word: item.word,
        translation: item.translation,
        kinds: [item.kind],
      });
    }
  }
  return [...map.values()];
}

const KIND_LABEL: Record<string, string> = {
  choice_en_ru: "Выбор EN→RU",
  type_en_ru: "Набор RU",
  choice_ru_en: "Выбор RU→EN",
  type_ru_en: "Набор EN",
  type_word: "Набор EN",
};

const FEEDBACK_ADVANCE_MS = 1500;

function ExerciseCard({
  item,
  index,
  onCheck,
  onResolved,
}: {
  item: ExerciseItem;
  index: number;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onResolved: (res: CheckResult, item: ExerciseItem) => void;
}) {
  const isType = item.kind === "type_en_ru" || item.kind === "type_ru_en" || item.kind === "type_word";
  if (isType) return <TypeExercise item={item} index={index} onCheck={onCheck} onResolved={onResolved} />;
  return <ChoiceExercise item={item} index={index} onCheck={onCheck} onResolved={onResolved} />;
}

function KindBadge({ kind }: { kind: string }) {
  return (
    <span className="rounded-full bg-paper-2 px-2.5 py-1 text-xs font-semibold text-ink-soft">
      {KIND_LABEL[kind] || "Задание"}
    </span>
  );
}

function CardResultIcon({ correct }: { correct: boolean }) {
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

function useAutoAdvance(
  result: CheckResult | null,
  item: ExerciseItem,
  resolvedRef: MutableRefObject<boolean>,
  onResolvedRef: MutableRefObject<(res: CheckResult, item: ExerciseItem) => void>,
) {
  useEffect(() => {
    if (!result) return;
    const timer = window.setTimeout(() => {
      if (resolvedRef.current) return;
      resolvedRef.current = true;
      onResolvedRef.current(result, item);
    }, FEEDBACK_ADVANCE_MS);
    return () => window.clearTimeout(timer);
  }, [result, item, resolvedRef, onResolvedRef]);
}

function ChoiceExercise({
  item,
  index,
  onCheck,
  onResolved,
}: {
  item: ExerciseItem;
  index: number;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onResolved: (res: CheckResult, item: ExerciseItem) => void;
}) {
  const options = useMemo(() => [...(item.options || [])].sort(() => Math.random() - 0.5), [item.uid]);
  const [value, setValue] = useState("");
  const [result, setResult] = useState<CheckResult | null>(null);
  const [busy, setBusy] = useState(false);
  const resolvedRef = useRef(false);
  const onResolvedRef = useRef(onResolved);
  onResolvedRef.current = onResolved;
  const locked = !!result;

  useAutoAdvance(result, item, resolvedRef, onResolvedRef);

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
        <KindBadge kind={item.kind} />
        {result && <CardResultIcon correct={result.correct} />}
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-lg">{item.prompt}</p>
          {item.speak && <SpeakButton text={item.speak} label="слово" />}
        </div>
        <div className="grid gap-2.5">
          {options.map((opt) => (
            <div key={opt} className="flex items-stretch gap-2">
              <button
                type="button"
                disabled={locked || busy}
                onClick={() => void submit(opt)}
                className={`quiz-choice vocab-choice ${value === opt ? "is-selected" : ""}`}
              >
                {opt}
              </button>
              {looksEnglish(opt) && <SpeakButton text={opt} />}
            </div>
          ))}
        </div>
      </div>
    </article>
  );
}

/** Keep only letters for the expected script; allow space, hyphen, ASCII/curly apostrophe. */
function filterTypedAnswer(raw: string, script: "cyrillic" | "latin"): string {
  const allowed =
    script === "cyrillic"
      ? /[^а-яА-ЯёЁ\s'\u2019-]/g
      : /[^a-zA-Z\s'\u2019-]/g;
  return raw.replace(allowed, "");
}

function TypeExercise({
  item,
  index,
  onCheck,
  onResolved,
}: {
  item: ExerciseItem;
  index: number;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onResolved: (res: CheckResult, item: ExerciseItem) => void;
}) {
  const [value, setValue] = useState("");
  const [result, setResult] = useState<CheckResult | null>(null);
  const [busy, setBusy] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const resolvedRef = useRef(false);
  const onResolvedRef = useRef(onResolved);
  onResolvedRef.current = onResolved;
  const toRussian = item.kind === "type_en_ru";
  const script = toRussian ? "cyrillic" : "latin";
  const placeholder = toRussian ? "Введите перевод по-русски" : "Введите английское слово";
  const locked = !!result;

  useAutoAdvance(result, item, resolvedRef, onResolvedRef);

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
        <KindBadge kind={item.kind} />
        {result && <CardResultIcon correct={result.correct} />}
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-lg font-semibold">{item.prompt}</p>
          {item.speak && <SpeakButton text={item.speak} label="слово" />}
        </div>
        {item.example && <p className="text-sm text-ink-soft">{item.example}</p>}
        {item.example_translation && <p className="text-sm text-ink-soft">{item.example_translation}</p>}
        <div className="vocab-type-slot">
          <input
            ref={inputRef}
            className="field vocab-type-input"
            value={value}
            autoCapitalize="none"
            autoCorrect="off"
            autoComplete="off"
            spellCheck={false}
            inputMode="text"
            enterKeyHint="done"
            placeholder={placeholder}
            onChange={(event) => setValue(filterTypedAnswer(event.target.value, script))}
            onKeyDown={(event) => {
              if (event.key === "Enter") {
                event.preventDefault();
                void submit();
              }
            }}
            disabled={locked}
          />
        </div>
        {!result && (
          <button type="button" className="btn btn-primary w-full sm:w-auto sm:justify-self-start" disabled={busy || !value.trim()} onClick={() => void submit()}>
            {busy ? "Проверяем…" : "Проверить"}
          </button>
        )}
      </div>
    </article>
  );
}
