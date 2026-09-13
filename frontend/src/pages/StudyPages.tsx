import {
  useCallback,
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
import { ProgressBar } from "../components/ProgressBar";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";
import { percent } from "../lib/percent";
import { looksEnglish } from "../lib/speech";
import { useSearchHighlight } from "../lib/searchHighlight";

type Deck = {
  id: number;
  slug: string;
  title: string;
  description: string;
  kind: string;
  card_count: number;
  learned_count: number;
  batch_count: number;
  suggested_batch: number;
};

type Card = {
  id: number;
  primary_text: string;
  secondary_text: string;
  tertiary_text: string;
  translation: string;
  example: string;
  example_translation: string;
  category: string;
  strength: number;
  mastery?: number;
  mastery_count?: number;
  learned?: boolean;
};

type DeckDetail = {
  slug: string;
  title: string;
  description: string;
  kind: string;
  card_count: number;
  learned_count: number;
  batch_size: number;
  batch_index: number;
  batch_count: number;
  batch_learned: number;
  suggested_batch: number;
  cards: Card[];
};

type PracticeItem = {
  uid: string;
  id: number;
  kind: string;
  prompt: string;
  options?: string[] | null;
  speak?: string | null;
  target?: string;
  example?: string | null;
};

type PracticePack = {
  deck: { slug: string; title: string; kind: string };
  batch_index: number;
  batch_count: number;
  card_count: number;
  learned_count: number;
  batch_learned: number;
  batch_card_count: number;
  pending_tasks: number;
  items: PracticeItem[];
};

type CheckResult = {
  correct: boolean;
  expected?: string | null;
  strength: number;
  mastery?: number;
  mastery_count?: number;
  learned?: boolean;
  primary_text?: string;
  translation?: string;
  example?: string;
  word?: string;
};

const META: Record<string, { title: string; subtitle: string; eyebrow: string }> = {
  verbs: {
    eyebrow: "Спряжение",
    title: "Неправильные глаголы",
    subtitle: "V1 / V2 / V3 с переводом. Учите партиями и проверяйте смысл в обе стороны.",
  },
  idioms: {
    eyebrow: "Речь",
    title: "Идиомы и пословицы",
    subtitle: "Устойчивые выражения с русским смыслом и коротким примером.",
  },
  exceptions: {
    eyebrow: "Ловушки",
    title: "Исключения",
    subtitle: "Частые исключения: plural, артикли, орфография — компактный набор.",
  },
};

const KIND_LABEL: Record<string, string> = {
  choice_en_ru: "Выбор EN→RU",
  choice_ru_en: "Выбор RU→EN",
};

const EXCEPTION_KIND_LABEL: Record<string, string> = {
  choice_en_ru: "Правило",
  choice_ru_en: "Пример",
};

function kindLabel(taskKind: string, deckKind?: string) {
  if (deckKind === "exceptions") {
    return EXCEPTION_KIND_LABEL[taskKind] || KIND_LABEL[taskKind] || taskKind;
  }
  return KIND_LABEL[taskKind] || taskKind;
}

const FEEDBACK_ADVANCE_MS = 1500;

export function StudyHub({ kind }: { kind: "verbs" | "idioms" | "exceptions" }) {
  const [decks, setDecks] = useState<Deck[]>([]);
  const meta = META[kind];
  useEffect(() => {
    api<Deck[]>(`/study/${kind}`).then(setDecks);
  }, [kind]);
  useSearchHighlight(decks.length > 0);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">{meta.eyebrow}</p>
        <h1 className="font-display mt-1 text-4xl">{meta.title}</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">{meta.subtitle}</p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {decks.map((deck) => (
          <Link key={deck.slug} to={`/app/${kind}/${deck.slug}`} data-search-id={deck.slug} className="card card-lift p-5">
            <h2 className="font-display text-2xl">{deck.title}</h2>
            <p className="mt-2 text-sm text-ink-soft">{deck.description}</p>
            <div className="mt-4">
              <ProgressBar
                value={percent(deck.learned_count, deck.card_count)}
                label={`${deck.learned_count}/${deck.card_count} · партия ${deck.suggested_batch}/${deck.batch_count}`}
              />
            </div>
          </Link>
        ))}
        {!decks.length && <p className="text-ink-soft">Пока пусто — запустите seed/expand.</p>}
      </div>
    </div>
  );
}

export function StudyDeckPage({ kind }: { kind: "verbs" | "idioms" | "exceptions" }) {
  const { slug } = useParams();
  const [searchParams] = useSearchParams();
  const batchFromUrl = searchParams.get("batch");
  const highlightFromUrl = searchParams.get("highlight");
  const { refresh } = useAuth();
  const [deck, setDeck] = useState<DeckDetail | null>(null);
  const [batch, setBatch] = useState<number | null>(null);
  const [mode, setMode] = useState<"cards" | "practice">("cards");
  const [practice, setPractice] = useState<PracticePack | null>(null);
  const [busy, setBusy] = useState(false);

  const load = (nextBatch?: number) => {
    if (!slug) return;
    const q = nextBatch ? `?batch=${nextBatch}` : "";
    api<DeckDetail>(`/study/${kind}/${slug}${q}`).then((data) => {
      setDeck(data);
      setBatch(data.batch_index);
    });
  };

  useEffect(() => {
    const initial = batchFromUrl ? Number(batchFromUrl) : undefined;
    if (highlightFromUrl) {
      setMode("cards");
      setPractice(null);
    }
    load(Number.isFinite(initial) && initial && initial > 0 ? initial : undefined);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [kind, slug, batchFromUrl, highlightFromUrl]);
  useSearchHighlight(!!deck && mode === "cards" && deck.slug === slug);

  const startPractice = async () => {
    if (!slug) return;
    setBusy(true);
    try {
      const data = await api<PracticePack>(`/study/${kind}/${slug}/practice${batch ? `?batch=${batch}` : ""}`);
      setPractice(data);
      setMode("practice");
    } finally {
      setBusy(false);
    }
  };

  const goBatch = (n: number) => {
    setMode("cards");
    setPractice(null);
    load(n);
  };

  const batches = useMemo(() => (deck ? Array.from({ length: deck.batch_count }, (_, i) => i + 1) : []), [deck]);

  if (!deck) return <p className="text-ink-soft">Загружаем…</p>;

  return (
    <div className="mx-auto grid max-w-3xl gap-5">
      <div>
        <Link to={`/app/${kind}`} className="text-sm text-terra">
          ← Назад
        </Link>
        <h1 className="font-display mt-2 text-4xl">{deck.title}</h1>
        <p className="mt-1 text-ink-soft">{deck.description}</p>
        <div className="mt-4">
          <ProgressBar
            value={percent(deck.learned_count, deck.card_count)}
            label={`${deck.learned_count}/${deck.card_count} · партия ${deck.batch_index}/${deck.batch_count} · ${deck.batch_learned}/${deck.cards.length} в партии`}
          />
        </div>
      </div>

      <div className="flex flex-wrap items-center gap-2">
        {batches.map((n) => (
          <button
            key={n}
            type="button"
            className={`rounded-full px-3 py-1 text-sm ${batch === n ? "bg-ink text-paper" : "bg-card text-ink-soft"}`}
            onClick={() => goBatch(n)}
          >
            {n}
          </button>
        ))}
        <VoiceControls className="ml-1" />
        <button
          type="button"
          className={`rounded-full px-3 py-1 text-sm ${
            mode === "practice" ? "bg-terra text-paper" : "border border-line bg-transparent text-ink-soft hover:text-ink"
          }`}
          onClick={() => void startPractice()}
          disabled={busy}
          title="Тренировать текущую партию"
        >
          {busy ? "…" : mode === "practice" ? "Ещё раз" : "Практика"}
        </button>
      </div>

      {mode === "cards" ? (
        <div className="grid gap-3">
          {deck.cards.map((c) => (
            <article key={c.id} data-search-id={String(c.id)} className="card p-5">
              {kind === "verbs" ? (
                <>
                  <p className="font-display text-2xl">{c.primary_text}</p>
                  <p className="mt-2 text-sm text-ink-soft">
                    V2: <b className="text-ink">{c.secondary_text}</b> · V3: <b className="text-ink">{c.tertiary_text}</b>
                  </p>
                  <p className="mt-2">{c.translation}</p>
                </>
              ) : (
                <>
                  <p className="font-display text-2xl">{c.primary_text}</p>
                  <p className="mt-2">{c.translation}</p>
                </>
              )}
              {c.example && (
                <p className="mt-3 text-sm text-ink-soft">
                  {c.example}
                  {c.example_translation ? ` — ${c.example_translation}` : ""}
                </p>
              )}
              <div className="mt-3 flex items-center justify-between">
                <span
                  className={`rounded-full px-2 py-1 text-xs ${c.learned ? "bg-sage-soft text-sage" : "text-ink-soft"}`}
                  title={
                    kind === "exceptions"
                      ? "Карточка выучена при силе 5/5. До этого обе стороны (правило и пример) снова попадают в практику."
                      : "Карточка выучена при силе 5/5. До этого обе стороны (EN→RU и RU→EN) снова попадают в практику."
                  }
                >
                  {c.learned
                    ? `выучено · сила ${c.strength}/5`
                    : `${Math.min(c.mastery_count ?? 0, 2)}/2 · сила ${c.strength}/5`}
                </span>
                {c.primary_text && <SpeakButton text={c.primary_text.split("→")[0].trim()} />}
              </div>
            </article>
          ))}
        </div>
      ) : (
        practice && (
          <StudySession
            pack={practice}
            onCheck={async (item, answer) => {
              const res = await api<CheckResult>(`/study/cards/${item.id}/check`, {
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
            onFinished={() => load(deck.batch_index)}
            onNextBatch={
              deck.batch_index < deck.batch_count
                ? () => {
                    goBatch(deck.batch_index + 1);
                  }
                : undefined
            }
            onRetry={() => void startPractice()}
            onBrowse={() => {
              setMode("cards");
              setPractice(null);
              load(deck.batch_index);
            }}
          />
        )
      )}
    </div>
  );
}

type FailedFacet = {
  cardId: number;
  primary: string;
  translation: string;
  kind: string;
};

function StudySession({
  pack,
  onCheck,
  onFinished,
  onNextBatch,
  onRetry,
  onBrowse,
}: {
  pack: PracticePack;
  onCheck: (item: PracticeItem, answer: string) => Promise<CheckResult>;
  onFinished: () => void;
  onNextBatch?: () => void;
  onRetry: () => void;
  onBrowse: () => void;
}) {
  const [index, setIndex] = useState(0);
  const [answeredCount, setAnsweredCount] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [cardsMastered, setCardsMastered] = useState(pack.batch_learned || 0);
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
    setCardsMastered(pack.batch_learned || 0);
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
    (res: CheckResult, current: PracticeItem) => {
      setAnsweredCount((value) => value + 1);
      if (res.correct) {
        setCorrectCount((value) => value + 1);
        if (res.learned) {
          setNewlyLearned((prev) => {
            if (prev.has(current.id)) return prev;
            setCardsMastered((value) => Math.min(value + 1, pack.batch_card_count || value + 1));
            return new Set(prev).add(current.id);
          });
        }
      } else {
        setFailed((prev) => [
          ...prev,
          {
            cardId: current.id,
            primary: res.primary_text || res.word || "",
            translation: res.translation || "",
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
    [index, onFinished, pack.batch_card_count, total],
  );

  if (!total || done) {
    const cleared = cardsMastered >= (pack.batch_card_count || 0);
    const reviewGroups = groupFailedFacets(failed);
    return (
      <section className="card grid gap-4 p-6 motion-enter">
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Сессия завершена</p>
        <h2 className="font-display text-3xl">{cleared ? "Партия закрыта" : "Прогресс сохранён"}</h2>
        <p className="text-ink-soft">
          Верно: {correctCount} из {total || answeredCount}. В партии до силы 5: {cardsMastered}/
          {pack.batch_card_count}. В колоде {pack.learned_count}/{pack.card_count}.
        </p>
        {reviewGroups.length > 0 ? (
          <div className="grid gap-3">
            <p className="font-semibold">Нужно повторить</p>
            <p className="text-sm text-ink-soft">
              Ошибка снижает силу и сбрасывает проход — в следующей тренировке снова обе стороны.
            </p>
            <ul className="grid gap-2">
              {reviewGroups.map((group) => (
                <li key={group.cardId} className="rounded-xl border border-line bg-paper-2/60 px-3 py-2.5">
                  <p className="font-semibold">
                    {group.primary} — {group.translation}
                  </p>
                  <p className="mt-1 text-sm text-ink-soft">
                    {group.kinds.map((k) => kindLabel(k, pack.deck.kind)).join(" · ")}
                  </p>
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
              Осталось: {left} · сила 5: {cardsMastered}/{pack.batch_card_count}
            </p>
          </div>
          <p className="text-sm text-ink-soft">
            {answeredCount + 1} / {total}
          </p>
        </div>
        <ProgressBar value={percent(answeredCount, total)} />
      </div>
      <div className="vocab-session-stage">
        <ChoiceExercise
          key={item.uid}
          item={item}
          index={index}
          deckKind={pack.deck.kind}
          onCheck={onCheck}
          onResolved={advance}
        />
      </div>
    </div>
  );
}

function groupFailedFacets(failed: FailedFacet[]) {
  const map = new Map<number, { cardId: number; primary: string; translation: string; kinds: string[] }>();
  for (const item of failed) {
    const existing = map.get(item.cardId);
    if (existing) {
      if (!existing.kinds.includes(item.kind)) existing.kinds.push(item.kind);
    } else {
      map.set(item.cardId, {
        cardId: item.cardId,
        primary: item.primary,
        translation: item.translation,
        kinds: [item.kind],
      });
    }
  }
  return [...map.values()];
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
  item: PracticeItem,
  resolvedRef: MutableRefObject<boolean>,
  onResolvedRef: MutableRefObject<(res: CheckResult, item: PracticeItem) => void>,
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
  deckKind,
  onCheck,
  onResolved,
}: {
  item: PracticeItem;
  index: number;
  deckKind?: string;
  onCheck: (item: PracticeItem, answer: string) => Promise<CheckResult>;
  onResolved: (res: CheckResult, item: PracticeItem) => void;
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
        <span className="rounded-full bg-paper-2 px-2.5 py-1 text-xs font-semibold text-ink-soft">
          {kindLabel(item.kind, deckKind) || "Задание"}
        </span>
        {result && <CardResultIcon correct={result.correct} />}
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-lg">{item.prompt}</p>
          {item.speak && <SpeakButton text={item.speak} label="фраза" />}
        </div>
        {item.example && <p className="text-sm text-ink-soft">{item.example}</p>}
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
