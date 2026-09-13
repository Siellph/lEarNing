import { useEffect, useMemo, useState, type CSSProperties } from "react";
import { CheckCircle2, CircleAlert } from "lucide-react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { ProgressBar } from "../components/ProgressBar";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";
import { looksEnglish } from "../lib/speech";

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

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Лексика</p>
        <h1 className="font-display mt-1 text-4xl">Тематические словари</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">
          Учите партиями: сначала карточки для просмотра, затем тренировка — четыре задания на слово
          (выбор и набор в обе стороны). Слово считается выученным, когда все четыре верны.
          Правила чтения — в разделе <Link to="/app/sounds" className="text-terra">Звуки</Link>.
        </p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {topics.map((topic) => (
          <Link key={topic.slug} to={`/app/vocab/${topic.slug}`} className="card card-lift p-5">
            <p className="text-sm font-semibold text-terra">{topic.level_code}</p>
            <h2 className="font-display text-2xl">{topic.title}</h2>
            <p className="mt-2 text-sm text-ink-soft">{topic.description}</p>
            <div className="mt-4">
              <ProgressBar
                value={topic.word_count ? (topic.learned_count / topic.word_count) * 100 : 0}
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
        <span className={`rounded-full px-2 py-1 text-xs ${word.learned ? "bg-sage-soft text-sage" : "bg-paper-2"}`}>
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
  const [doneCount, setDoneCount] = useState(0);
  const [wordsMastered, setWordsMastered] = useState(pack.batch_learned || 0);
  const [newlyLearned, setNewlyLearned] = useState<Set<number>>(() => new Set());
  const [done, setDone] = useState(false);
  const item = pack.items[index];
  const total = pack.items.length;
  const left = Math.max(total - doneCount, 0);

  useEffect(() => {
    setIndex(0);
    setDoneCount(0);
    setWordsMastered(pack.batch_learned || 0);
    setNewlyLearned(new Set());
    setDone(false);
  }, [pack]);

  useEffect(() => {
    if (!total) {
      setDone(true);
      onFinished();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [total]);

  const advance = (res: CheckResult) => {
    setDoneCount((value) => value + 1);
    if (res.learned && item && !newlyLearned.has(item.id)) {
      setNewlyLearned((prev) => new Set(prev).add(item.id));
      setWordsMastered((value) => Math.min(value + 1, pack.batch_word_count || pack.new_count || value + 1));
    }
    if (index + 1 >= total) {
      setDone(true);
      onFinished();
      return;
    }
    setIndex((value) => value + 1);
  };

  if (!total || done) {
    const cleared = wordsMastered >= (pack.batch_word_count || pack.new_count);
    return (
      <section className="card grid gap-4 p-6 motion-enter">
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Сессия завершена</p>
        <h2 className="font-display text-3xl">
          {cleared ? "Партия закрыта" : "Прогресс сохранён"}
        </h2>
        <p className="text-ink-soft">
          Выполнено заданий: {doneCount} из {total || doneCount}. В партии выучено {wordsMastered}/
          {pack.batch_word_count || pack.new_count} слов. В теме {pack.learned_count}/{pack.word_count}. Следующая
          тренировка этой партии возьмёт только слова без полного набора из 4 заданий.
        </p>
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
    <div className="grid gap-4">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className="text-sm font-semibold text-terra">
            Партия {pack.batch_index} из {pack.batch_count}
          </p>
          <p className="text-sm text-ink-soft">
            Осталось заданий: {left} · выучено слов: {wordsMastered}/{pack.batch_word_count || pack.new_count}
          </p>
        </div>
        <p className="text-sm text-ink-soft">
          {doneCount + 1} / {total}
        </p>
      </div>
      <ProgressBar value={total ? (doneCount / total) * 100 : 0} />
      <ExerciseCard key={item.uid} item={item} index={index} onCheck={onCheck} onSolved={advance} />
    </div>
  );
}

const KIND_LABEL: Record<string, string> = {
  choice_en_ru: "Выбор EN→RU",
  type_en_ru: "Набор RU",
  choice_ru_en: "Выбор RU→EN",
  type_ru_en: "Набор EN",
  type_word: "Набор EN",
};

function ExerciseCard({
  item,
  index,
  onCheck,
  onSolved,
}: {
  item: ExerciseItem;
  index: number;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onSolved: (res: CheckResult) => void;
}) {
  const isType = item.kind === "type_en_ru" || item.kind === "type_ru_en" || item.kind === "type_word";
  if (isType) return <TypeExercise item={item} index={index} onCheck={onCheck} onSolved={onSolved} />;
  return <ChoiceExercise item={item} index={index} onCheck={onCheck} onSolved={onSolved} />;
}

function KindBadge({ kind }: { kind: string }) {
  return (
    <span className="rounded-full bg-paper-2 px-2.5 py-1 text-xs font-semibold text-ink-soft">
      {KIND_LABEL[kind] || "Задание"}
    </span>
  );
}

function ChoiceExercise({
  item,
  index,
  onCheck,
  onSolved,
}: {
  item: ExerciseItem;
  index: number;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onSolved: (res: CheckResult) => void;
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
    <article
      className={`quiz-card motion-enter ${result ? (result.correct ? "quiz-card-ok" : "quiz-card-bad") : ""}`}
      style={{ "--motion-i": Math.min(index, 8) } as CSSProperties}
    >
      <header className="quiz-card-head">
        <KindBadge kind={item.kind} />
        {result?.correct && (
          <span className="quiz-status-ok">
            <CheckCircle2 size={14} /> Верно
          </span>
        )}
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-lg">{item.prompt}</p>
          {item.speak && <SpeakButton text={item.speak} label="слово" />}
        </div>
        <div className="grid gap-2">
          {options.map((opt) => (
            <div key={opt} className="flex items-center gap-2">
              <button
                type="button"
                disabled={!!result?.correct}
                onClick={() => {
                  setValue(opt);
                  setResult(null);
                }}
                className={`quiz-choice ${value === opt ? "is-selected" : ""}`}
              >
                {opt}
              </button>
              {looksEnglish(opt) && <SpeakButton text={opt} />}
            </div>
          ))}
        </div>
        {!result?.correct ? (
          <button type="button" className="btn btn-primary justify-self-start" disabled={busy || !value} onClick={submit}>
            {busy ? "Проверяем…" : "Проверить"}
          </button>
        ) : (
          <button type="button" className="btn btn-primary justify-self-start" onClick={() => onSolved(result)}>
            Дальше
          </button>
        )}
        {result && <SoftFeedback result={result} />}
      </div>
    </article>
  );
}

function TypeExercise({
  item,
  index,
  onCheck,
  onSolved,
}: {
  item: ExerciseItem;
  index: number;
  onCheck: (item: ExerciseItem, answer: string) => Promise<CheckResult>;
  onSolved: (res: CheckResult) => void;
}) {
  const [value, setValue] = useState("");
  const [showHint, setShowHint] = useState(false);
  const [result, setResult] = useState<CheckResult | null>(null);
  const [busy, setBusy] = useState(false);
  const toRussian = item.kind === "type_en_ru";
  const placeholder = toRussian ? "Введите перевод по-русски" : "Введите английское слово";

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
    <article
      className={`quiz-card motion-enter ${result ? (result.correct ? "quiz-card-ok" : "quiz-card-bad") : ""}`}
      style={{ "--motion-i": Math.min(index, 8) } as CSSProperties}
    >
      <header className="quiz-card-head">
        <KindBadge kind={item.kind} />
        {result?.correct && (
          <span className="quiz-status-ok">
            <CheckCircle2 size={14} /> Верно
          </span>
        )}
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-lg font-semibold">{item.prompt}</p>
          {item.speak && <SpeakButton text={item.speak} label="слово" />}
        </div>
        {item.example && <p className="text-sm text-ink-soft">{item.example}</p>}
        {item.example_translation && <p className="text-sm text-ink-soft">{item.example_translation}</p>}
        <input
          className="field"
          value={value}
          autoCapitalize="none"
          autoCorrect="off"
          placeholder={placeholder}
          onChange={(event) => {
            setValue(event.target.value);
            setResult(null);
          }}
          onKeyDown={(event) => event.key === "Enter" && !result?.correct && submit()}
          disabled={!!result?.correct}
        />
        <div className="flex flex-wrap items-center gap-2">
          {!result?.correct && (
            <>
              <button type="button" className="btn btn-primary" disabled={busy || !value.trim()} onClick={submit}>
                {busy ? "Проверяем…" : "Проверить"}
              </button>
              <button type="button" className="btn btn-ghost" onClick={() => setShowHint(true)}>
                Подсказка
              </button>
            </>
          )}
          {result?.correct && (
            <button type="button" className="btn btn-primary" onClick={() => onSolved(result)}>
              Дальше
            </button>
          )}
          {showHint && item.hint && <span className="text-sm text-ink-soft">Первая буква: {item.hint}</span>}
        </div>
        {result && <SoftFeedback result={result} />}
      </div>
    </article>
  );
}

function SoftFeedback({ result }: { result: CheckResult }) {
  return (
    <div className={`quiz-feedback ${result.correct ? "is-ok" : "is-bad"}`} aria-live="polite">
      <div className="quiz-feedback-title">
        {result.correct ? (
          <>
            <CheckCircle2 size={18} /> Отлично
          </>
        ) : (
          <>
            <CircleAlert size={18} /> Нужно иначе
          </>
        )}
      </div>
      {!result.correct && result.expected && (
        <p className="quiz-feedback-expected">
          Верный ответ: <strong>{result.expected}</strong>
        </p>
      )}
      {result.correct && (
        <p className="quiz-feedback-note">
          {result.word} — {result.translation}
          {result.learned ? " · слово выучено" : result.mastery_count != null ? ` · ${result.mastery_count}/4` : ""}
        </p>
      )}
    </div>
  );
}
