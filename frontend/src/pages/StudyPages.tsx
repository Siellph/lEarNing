import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { ProgressBar } from "../components/ProgressBar";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";

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
  options?: string[];
  target?: string;
  accepted?: string[];
  example?: string;
};

const META: Record<string, { title: string; subtitle: string; eyebrow: string }> = {
  verbs: {
    eyebrow: "Спряжение",
    title: "Неправильные глаголы",
    subtitle: "V1 / V2 / V3 с переводом. Учите партиями и проверяйте формы.",
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

export function StudyHub({ kind }: { kind: "verbs" | "idioms" | "exceptions" }) {
  const [decks, setDecks] = useState<Deck[]>([]);
  const meta = META[kind];
  useEffect(() => {
    api<Deck[]>(`/study/${kind}`).then(setDecks);
  }, [kind]);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">{meta.eyebrow}</p>
        <h1 className="font-display mt-1 text-4xl">{meta.title}</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">{meta.subtitle}</p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {decks.map((deck) => (
          <Link key={deck.slug} to={`/app/${kind}/${deck.slug}`} className="card p-5 hover:border-terra/40">
            <h2 className="font-display text-2xl">{deck.title}</h2>
            <p className="mt-2 text-sm text-ink-soft">{deck.description}</p>
            <div className="mt-4">
              <ProgressBar
                value={deck.card_count ? (deck.learned_count / deck.card_count) * 100 : 0}
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
  const { refresh } = useAuth();
  const [deck, setDeck] = useState<DeckDetail | null>(null);
  const [batch, setBatch] = useState<number | null>(null);
  const [mode, setMode] = useState<"cards" | "practice">("cards");
  const [items, setItems] = useState<PracticeItem[]>([]);
  const [index, setIndex] = useState(0);
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState<{ correct: boolean; expected?: string | null } | null>(null);
  const [flipped, setFlipped] = useState(false);

  const load = (nextBatch?: number) => {
    if (!slug) return;
    const q = nextBatch ? `?batch=${nextBatch}` : "";
    api<DeckDetail>(`/study/${kind}/${slug}${q}`).then((data) => {
      setDeck(data);
      setBatch(data.batch_index);
    });
  };

  useEffect(() => {
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [kind, slug]);

  const startPractice = async () => {
    if (!slug) return;
    const data = await api<{ items: PracticeItem[] }>(
      `/study/${kind}/${slug}/practice${batch ? `?batch=${batch}` : ""}`,
    );
    setItems(data.items);
    setIndex(0);
    setAnswer("");
    setFeedback(null);
    setMode("practice");
  };

  const current = items[index];
  const card = deck?.cards.find((c) => c.id === current?.id);

  const check = async () => {
    if (!current) return;
    const body =
      current.kind === "choice_translation" || current.options
        ? { answer, kind: current.kind, target: current.target }
        : { answer, kind: current.kind, target: current.target, accepted: current.accepted };
    const res = await api<{ correct: boolean; expected?: string | null }>(`/study/cards/${current.id}/check`, {
      method: "POST",
      body: JSON.stringify(body),
    });
    setFeedback(res);
    refresh();
  };

  const next = () => {
    setFeedback(null);
    setAnswer("");
    if (index + 1 >= items.length) {
      setMode("cards");
      load(batch ?? undefined);
      return;
    }
    setIndex((i) => i + 1);
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
      </div>
      <div className="flex flex-wrap items-center gap-2">
        {batches.map((n) => (
          <button
            key={n}
            type="button"
            className={`rounded-full px-3 py-1 text-sm ${batch === n ? "bg-ink text-paper" : "bg-card text-ink-soft"}`}
            onClick={() => {
              setMode("cards");
              load(n);
            }}
          >
            {n}
          </button>
        ))}
        <VoiceControls />
        <button className="btn btn-primary ml-auto text-sm" onClick={startPractice}>
          Практика партии
        </button>
      </div>

      {mode === "cards" ? (
        <div className="grid gap-3">
          {deck.cards.map((c) => (
            <article
              key={c.id}
              className="card cursor-pointer p-5"
              onClick={() => {
                setFlipped((f) => !f);
              }}
            >
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
                <span className="text-xs text-ink-soft">сила {c.strength}/5</span>
                {c.primary_text && <SpeakButton text={c.primary_text.split("→")[0].trim()} />}
              </div>
            </article>
          ))}
        </div>
      ) : current ? (
        <article className="card grid gap-4 p-6">
          <p className="text-sm text-ink-soft">
            {index + 1} / {items.length}
          </p>
          <p className="text-xl">{current.prompt}</p>
          {current.example && <p className="text-sm text-ink-soft">{current.example}</p>}
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
            <input className="field" value={answer} onChange={(e) => setAnswer(e.target.value)} placeholder="Ответ" />
          )}
          <div className="flex flex-wrap gap-3">
            {!feedback ? (
              <button className="btn btn-primary" disabled={!answer.trim()} onClick={check}>
                Проверить
              </button>
            ) : (
              <button className="btn btn-sage" onClick={next}>
                Дальше
              </button>
            )}
            {feedback && (
              <span className={feedback.correct ? "text-sage" : "text-rose"}>
                {feedback.correct ? "Верно" : `Ответ: ${feedback.expected}`}
              </span>
            )}
          </div>
          {card && kind === "verbs" && feedback && (
            <p className="text-sm text-ink-soft">
              {card.primary_text} — {card.secondary_text} — {card.tertiary_text}
            </p>
          )}
        </article>
      ) : null}
      {flipped ? null : null}
    </div>
  );
}
