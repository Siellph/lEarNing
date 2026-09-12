import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { ProgressBar } from "../components/ProgressBar";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";
import { speakEnglish } from "../lib/speech";

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
  transcription?: string;
  translation?: string;
  part_of_speech?: string;
  example?: string;
  example_translation?: string;
  gap?: string;
  hint?: string;
  target?: string;
  word_ids?: number[];
  left?: { id: number; text: string }[];
  right?: { id: number; text: string }[];
};

type PracticePack = {
  topic: { slug: string; title: string };
  batch_index: number;
  batch_count: number;
  new_count: number;
  review_count: number;
  word_count: number;
  learned_count: number;
  items: ExerciseItem[];
};

type CheckResult = {
  correct: boolean;
  word: string;
  translation: string;
  example: string;
  strength: number;
  expected?: string | null;
};

export function VocabPage() {
  const [topics, setTopics] = useState<Topic[]>([]);
  useEffect(() => {
    api<Topic[]>("/vocab/topics").then(setTopics);
  }, []);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Лексика</p>
        <h1 className="font-display mt-1 text-4xl">Тематические словари</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">
          Учите партиями по 8–12 слов: карточки, выбор, набор, слух и пары. Не весь словарь сразу.
          Правила чтения — в разделе <Link to="/app/sounds" className="text-terra">Звуки</Link>.
        </p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {topics.map((topic) => (
          <Link key={topic.slug} to={`/app/vocab/${topic.slug}`} className="card p-5 hover:border-terra/40">
            <p className="text-sm font-semibold text-terra">{topic.level_code}</p>
            <h2 className="font-display text-2xl">{topic.title}</h2>
            <p className="mt-2 text-sm text-ink-soft">{topic.description}</p>
            <div className="mt-4">
              <ProgressBar
                value={topic.word_count ? (topic.learned_count / topic.word_count) * 100 : 0}
                label={`${topic.learned_count}/${topic.word_count} в памяти · партия ${topic.suggested_batch} из ${topic.batch_count}`}
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
    loadTopic(batch ?? undefined);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [slug]);

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
            value={topic.word_count ? (topic.learned_count / topic.word_count) * 100 : 0}
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
          <button className={`btn ${mode === "cards" ? "btn-primary" : "btn-ghost"}`} onClick={() => setMode("cards")}>
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
            onCheck={async (item, answer, extra) => {
              const res = await api<CheckResult>(`/vocab/words/${item.id}/check`, {
                method: "POST",
                body: JSON.stringify({
                  answer,
                  kind: item.kind,
                  target: extra?.target ?? item.target,
                  remembered: extra?.remembered,
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
          />
        )
      )}
    </div>
  );
}

function StudyCard({ word }: { word: Word }) {
  const [open, setOpen] = useState(false);
  return (
    <article className="card cursor-pointer p-5" onClick={() => setOpen((value) => !value)}>
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
        <span className="rounded-full bg-paper-2 px-2 py-1 text-xs">{word.strength}/5</span>
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
}: {
  pack: PracticePack;
  onCheck: (
    item: ExerciseItem,
    answer: string,
    extra?: { remembered?: boolean; target?: string },
  ) => Promise<CheckResult>;
  onFinished: () => void;
  onNextBatch?: () => void;
  onRetry: () => void;
}) {
  const [index, setIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [done, setDone] = useState(false);
  const item = pack.items[index];
  const total = pack.items.length;

  const next = (correct: boolean) => {
    if (correct) setCorrectCount((value) => value + 1);
    if (index + 1 >= total) {
      setDone(true);
      onFinished();
      return;
    }
    setIndex((value) => value + 1);
  };

  if (done) {
    return (
      <section className="card grid gap-4 p-6">
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Партия закрыта</p>
        <h2 className="font-display text-3xl">
          {correctCount} из {total} верно
        </h2>
        <p className="text-ink-soft">
          Партия {pack.batch_index} из {pack.batch_count}. В теме {pack.learned_count}/{pack.word_count} слов уже в
          памяти. Можно повторить эту партию или взять следующую.
        </p>
        <div className="flex flex-wrap gap-2">
          <button type="button" className="btn btn-ghost" onClick={onRetry}>
            Ещё раз эту партию
          </button>
          {onNextBatch && (
            <button type="button" className="btn btn-primary" onClick={onNextBatch}>
              Следующая партия
            </button>
          )}
        </div>
      </section>
    );
  }

  return (
    <div className="grid gap-4">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-sm font-semibold text-terra">
            Партия {pack.batch_index} из {pack.batch_count}
          </p>
          <p className="text-sm text-ink-soft">
            {pack.new_count} из этой партии
            {pack.review_count ? ` · ${pack.review_count} на повторение` : ""}
          </p>
        </div>
        <p className="text-sm text-ink-soft">
          {index + 1} / {total}
        </p>
      </div>
      <ProgressBar value={total ? ((index + 1) / total) * 100 : 0} />
      <ExerciseCard key={item.uid} item={item} onCheck={onCheck} onNext={next} />
    </div>
  );
}

const KIND_LABEL: Record<string, string> = {
  card: "Карточка",
  choice_en_ru: "Выбор EN→RU",
  choice_ru_en: "Выбор RU→EN",
  type_word: "Набор слова",
  listen_pick: "Слух",
  match_pairs: "Пары",
};

function ExerciseCard({
  item,
  onCheck,
  onNext,
}: {
  item: ExerciseItem;
  onCheck: (
    item: ExerciseItem,
    answer: string,
    extra?: { remembered?: boolean; target?: string },
  ) => Promise<CheckResult>;
  onNext: (correct: boolean) => void;
}) {
  if (item.kind === "card") return <CardExercise item={item} onCheck={onCheck} onNext={onNext} />;
  if (item.kind === "match_pairs") return <MatchExercise item={item} onCheck={onCheck} onNext={onNext} />;
  if (item.kind === "type_word") return <TypeExercise item={item} onCheck={onCheck} onNext={onNext} />;
  if (item.kind === "listen_pick") return <ListenExercise item={item} onCheck={onCheck} onNext={onNext} />;
  return <ChoiceExercise item={item} onCheck={onCheck} onNext={onNext} />;
}

function KindBadge({ kind }: { kind: string }) {
  return (
    <span className="rounded-full bg-paper-2 px-2.5 py-1 text-xs font-semibold text-ink-soft">
      {KIND_LABEL[kind] || "Задание"}
    </span>
  );
}

function CardExercise({
  item,
  onCheck,
  onNext,
}: {
  item: ExerciseItem;
  onCheck: (
    item: ExerciseItem,
    answer: string,
    extra?: { remembered?: boolean; target?: string },
  ) => Promise<CheckResult>;
  onNext: (correct: boolean) => void;
}) {
  const [open, setOpen] = useState(false);
  const [busy, setBusy] = useState(false);

  const mark = async (remembered: boolean) => {
    setBusy(true);
    try {
      const res = await onCheck(item, item.prompt, { remembered });
      onNext(res.correct);
    } finally {
      setBusy(false);
    }
  };

  return (
    <article className="card grid gap-4 p-6">
      <KindBadge kind="card" />
      <div className="flex items-center justify-between gap-3">
        <h2 className="font-display text-4xl">{item.prompt}</h2>
        <SpeakButton text={item.speak || item.prompt} label="слово" />
      </div>
      <p className="text-sm text-ink-soft">
        {item.transcription} · {item.part_of_speech}
      </p>
      {open ? (
        <div>
          <p className="text-xl font-semibold">{item.translation}</p>
          <p className="mt-2 text-sm">{item.example}</p>
          <p className="text-sm text-ink-soft">{item.example_translation}</p>
        </div>
      ) : (
        <button type="button" className="btn btn-ghost justify-self-start" onClick={() => setOpen(true)}>
          Показать перевод
        </button>
      )}
      {open && (
        <div className="flex flex-wrap gap-2">
          <button type="button" className="btn btn-primary" disabled={busy} onClick={() => mark(true)}>
            Помню
          </button>
          <button type="button" className="btn btn-ghost" disabled={busy} onClick={() => mark(false)}>
            Ещё нет
          </button>
        </div>
      )}
    </article>
  );
}

function ChoiceExercise({
  item,
  onCheck,
  onNext,
}: {
  item: ExerciseItem;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onNext: (correct: boolean) => void;
}) {
  const options = useMemo(() => [...(item.options || [])].sort(() => Math.random() - 0.5), [item.uid]);
  const [value, setValue] = useState("");
  const [result, setResult] = useState<CheckResult | null>(null);
  const [busy, setBusy] = useState(false);

  const submit = async () => {
    if (!value) return;
    setBusy(true);
    try {
      const res = await onCheck(item, value);
      setResult(res);
    } finally {
      setBusy(false);
    }
  };

  return (
    <article className="card grid gap-4 p-6">
      <KindBadge kind={item.kind} />
      <div className="flex items-start justify-between gap-3">
        <p className="text-lg">{item.prompt}</p>
        {item.speak && <SpeakButton text={item.speak} />}
      </div>
      <div className="grid gap-2">
        {options.map((opt) => (
          <button
            key={opt}
            type="button"
            disabled={!!result}
            onClick={() => setValue(opt)}
            className={`rounded-xl border px-4 py-3 text-left transition ${
              value === opt ? "border-terra bg-[#fff1eb]" : "border-line bg-white hover:border-terra/50"
            }`}
          >
            {opt}
          </button>
        ))}
      </div>
      {!result ? (
        <button type="button" className="btn btn-primary justify-self-start" disabled={busy || !value} onClick={submit}>
          {busy ? "Проверяем…" : "Проверить"}
        </button>
      ) : (
        <ResultFooter result={result} onNext={onNext} />
      )}
    </article>
  );
}

function TypeExercise({
  item,
  onCheck,
  onNext,
}: {
  item: ExerciseItem;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onNext: (correct: boolean) => void;
}) {
  const [value, setValue] = useState("");
  const [showHint, setShowHint] = useState(false);
  const [result, setResult] = useState<CheckResult | null>(null);
  const [busy, setBusy] = useState(false);

  const submit = async () => {
    if (!value.trim()) return;
    setBusy(true);
    try {
      const res = await onCheck(item, value.trim());
      setResult(res);
    } finally {
      setBusy(false);
    }
  };

  return (
    <article className="card grid gap-4 p-6">
      <KindBadge kind="type_word" />
      <p className="text-lg font-semibold">{item.prompt}</p>
      {item.gap && <p className="text-lg">{item.gap}</p>}
      {item.example_translation && <p className="text-sm text-ink-soft">{item.example_translation}</p>}
      <input
        className="field"
        value={value}
        autoCapitalize="none"
        autoCorrect="off"
        placeholder="Введите английское слово"
        onChange={(event) => setValue(event.target.value)}
        onKeyDown={(event) => event.key === "Enter" && submit()}
        disabled={!!result}
      />
      <div className="flex flex-wrap items-center gap-2">
        {!result && (
          <>
            <button type="button" className="btn btn-primary" disabled={busy || !value.trim()} onClick={submit}>
              {busy ? "Проверяем…" : "Проверить"}
            </button>
            <button type="button" className="btn btn-ghost" onClick={() => setShowHint(true)}>
              Подсказка
            </button>
          </>
        )}
        {showHint && item.hint && <span className="text-sm text-ink-soft">Первая буква: {item.hint}</span>}
      </div>
      {result && <ResultFooter result={result} onNext={onNext} />}
    </article>
  );
}

function ListenExercise({
  item,
  onCheck,
  onNext,
}: {
  item: ExerciseItem;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onNext: (correct: boolean) => void;
}) {
  useEffect(() => {
    if (item.speak) speakEnglish(item.speak);
  }, [item.uid, item.speak]);

  return (
    <div className="grid gap-3">
      <div className="flex justify-end">
        <SpeakButton text={item.speak || ""} label="Ещё раз" />
      </div>
      <ChoiceExercise item={item} onCheck={onCheck} onNext={onNext} />
    </div>
  );
}

function MatchExercise({
  item,
  onCheck,
  onNext,
}: {
  item: ExerciseItem;
  onCheck: (item: ExerciseItem, answer: string, extra?: { target?: string }) => Promise<CheckResult>;
  onNext: (correct: boolean) => void;
}) {
  const [leftId, setLeftId] = useState<number | null>(null);
  const [pairs, setPairs] = useState<Record<number, string>>({});
  const [busy, setBusy] = useState(false);
  const [result, setResult] = useState<{ correct: number; total: number } | null>(null);
  const usedRight = new Set(Object.values(pairs));

  const pickRight = (text: string) => {
    if (leftId == null || result) return;
    setPairs((current) => ({ ...current, [leftId]: text }));
    setLeftId(null);
  };

  const submit = async () => {
    const left = item.left || [];
    if (left.some((entry) => !pairs[entry.id])) return;
    setBusy(true);
    try {
      let correct = 0;
      for (const entry of left) {
        const res = await onCheck({ ...item, id: entry.id }, pairs[entry.id], { target: "translation" });
        if (res.correct) correct += 1;
      }
      setResult({ correct, total: left.length });
    } finally {
      setBusy(false);
    }
  };

  return (
    <article className="card grid gap-4 p-6">
      <KindBadge kind="match_pairs" />
      <p className="text-lg">{item.prompt}</p>
      <div className="grid gap-4 md:grid-cols-2">
        <div className="grid gap-2">
          {(item.left || []).map((entry) => (
            <button
              key={entry.id}
              type="button"
              disabled={!!result}
              onClick={() => setLeftId(entry.id)}
              className={`rounded-xl border px-4 py-3 text-left ${
                leftId === entry.id ? "border-terra bg-[#fff1eb]" : "border-line bg-white"
              } ${pairs[entry.id] ? "opacity-70" : ""}`}
            >
              <span className="font-semibold">{entry.text}</span>
              {pairs[entry.id] && <span className="mt-1 block text-sm text-ink-soft">{pairs[entry.id]}</span>}
            </button>
          ))}
        </div>
        <div className="grid gap-2">
          {(item.right || []).map((entry) => (
            <button
              key={entry.text}
              type="button"
              disabled={!!result || usedRight.has(entry.text)}
              onClick={() => pickRight(entry.text)}
              className={`rounded-xl border px-4 py-3 text-left ${
                usedRight.has(entry.text) ? "border-sage bg-sage-soft" : "border-line bg-white hover:border-terra/50"
              }`}
            >
              {entry.text}
            </button>
          ))}
        </div>
      </div>
      {!result ? (
        <button
          type="button"
          className="btn btn-primary justify-self-start"
          disabled={busy || (item.left || []).some((entry) => !pairs[entry.id])}
          onClick={submit}
        >
          {busy ? "Проверяем…" : "Проверить пары"}
        </button>
      ) : (
        <div className="flex flex-wrap items-center gap-3">
          <p className={`font-semibold ${result.correct === result.total ? "text-sage" : "text-rose"}`}>
            {result.correct} из {result.total} пар верно
          </p>
          <button type="button" className="btn btn-primary" onClick={() => onNext(result.correct === result.total)}>
            Дальше
          </button>
        </div>
      )}
    </article>
  );
}

function ResultFooter({ result, onNext }: { result: CheckResult; onNext: (correct: boolean) => void }) {
  return (
    <div className="grid gap-2">
      <p className={`font-semibold ${result.correct ? "text-sage" : "text-rose"}`}>
        {result.correct ? "Отлично" : `Правильный ответ: ${result.expected || result.word}`}
      </p>
      <p className="text-sm text-ink-soft">
        {result.word} — {result.translation}. {result.example}
      </p>
      <button type="button" className="btn btn-primary justify-self-start" onClick={() => onNext(result.correct)}>
        Дальше
      </button>
    </div>
  );
}
