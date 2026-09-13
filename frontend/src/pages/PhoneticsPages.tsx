import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { LessonView, type LessonContent } from "../components/LessonView";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { speakEnglish } from "../lib/speech";
import { useSearchHighlight } from "../lib/searchHighlight";

type ChartItem = {
  ipa: string;
  keyword: string;
  hint: string;
  articulation: string;
  contrast: string;
  tip: string;
  examples: string[];
};

type ChartGroup = {
  group: string;
  tip: string;
  items: ChartItem[];
};

type TopicCard = {
  slug: string;
  title: string;
  description: string;
  minutes: number;
};

function SoundDetail({ item }: { item: ChartItem }) {
  return (
    <section className="card mt-3 grid gap-4 p-5 sm:p-6">
      <div className="flex flex-wrap items-center gap-2">
        <h3 className="font-display text-2xl">
          /{item.ipa}/ · {item.keyword}
        </h3>
        <SpeakButton text={item.keyword} label="слово" />
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        <div>
          <p className="text-sm font-semibold text-terra">Как произносить</p>
          <p className="mt-1 leading-7 text-ink-soft">{item.articulation}</p>
        </div>
        <div>
          <p className="text-sm font-semibold text-terra">Не путайте</p>
          <p className="mt-1 leading-7 text-ink-soft">{item.contrast}</p>
        </div>
      </div>
      <p className="rounded-xl bg-paper px-4 py-3 text-sm leading-6 text-ink-soft">{item.tip}</p>
      <div>
        <p className="mb-2 text-sm font-semibold">Примеры</p>
        <div className="flex flex-wrap gap-2">
          {item.examples.map((word) => (
            <span key={word} className="inline-flex items-center gap-1 rounded-full bg-paper px-3 py-1.5 text-sm font-medium">
              {word}
              <SpeakButton text={word} />
            </span>
          ))}
        </div>
      </div>
    </section>
  );
}

export function PhoneticsPage() {
  const [chart, setChart] = useState<ChartGroup[]>([]);
  const [topics, setTopics] = useState<TopicCard[]>([]);
  const [selected, setSelected] = useState<string | null>(null);

  useEffect(() => {
    api<ChartGroup[]>("/phonetics/chart").then(setChart);
    api<TopicCard[]>("/phonetics/topics").then(setTopics);
  }, []);
  useSearchHighlight(topics.length > 0);

  const selectedItem = chart.flatMap((group) => group.items).find((item) => item.ipa === selected) || null;

  return (
    <div className="grid gap-8">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <p className="text-sm uppercase tracking-[0.18em] text-terra">Произношение</p>
          <h1 className="font-display mt-1 text-4xl">Транскрипция и слух</h1>
          <p className="mt-2 max-w-2xl text-ink-soft">
            Нажмите символ — услышите ключевое слово и откроете постановку. Ниже — правила чтения, слабые формы и то,
            как слова склеиваются в потоке. Темп и акцент действуют на все динамики.
          </p>
        </div>
        <VoiceControls />
      </div>
      {chart.map((group) => {
        const open = group.items.find((item) => item.ipa === selected) || null;
        return (
          <section key={group.group}>
            <div className="mb-3">
              <h2 className="font-display text-2xl">{group.group}</h2>
              <p className="text-sm text-ink-soft">{group.tip}</p>
            </div>
            <div className="grid grid-cols-2 gap-2 sm:grid-cols-3 md:grid-cols-4 xl:grid-cols-5">
              {group.items.map((item) => (
                <div
                  key={item.ipa}
                  className={`ipa-tile ${selected === item.ipa ? "ipa-tile-open" : ""}`}
                  role="button"
                  tabIndex={0}
                  onClick={() => {
                    setSelected(item.ipa);
                    speakEnglish(item.keyword);
                  }}
                  onKeyDown={(event) => {
                    if (event.key === "Enter" || event.key === " ") {
                      event.preventDefault();
                      setSelected(item.ipa);
                      speakEnglish(item.keyword);
                    }
                  }}
                >
                  <div className="flex items-center justify-center gap-1">
                    <span className="font-display text-2xl">/{item.ipa}/</span>
                    <SpeakButton text={item.keyword} />
                  </div>
                  <p className="text-sm font-semibold">{item.keyword}</p>
                  <p className="text-xs leading-4 text-ink-soft">{item.hint}</p>
                </div>
              ))}
            </div>
            {open ? <SoundDetail item={open} /> : null}
          </section>
        );
      })}
      {selectedItem ? null : (
        <p className="text-sm text-ink-soft">Выберите звук в таблице, чтобы увидеть постановку, контраст и примеры.</p>
      )}
      <section className="grid gap-3">
        <h2 className="font-display text-2xl">Блоки разбора</h2>
        {topics.map((topic, index) => (
          <Link key={topic.slug} to={`/app/sounds/${topic.slug}`} data-search-id={topic.slug} className="card card-lift flex flex-col gap-2 p-5 sm:flex-row sm:items-center">
            <div className="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-paper-2 font-display text-lg">
              {index + 1}
            </div>
            <div className="min-w-0 flex-1">
              <h3 className="font-semibold">{topic.title}</h3>
              <p className="text-sm text-ink-soft">{topic.description}</p>
              <p className="mt-1 text-xs text-ink-soft">{topic.minutes} мин · справочник</p>
            </div>
          </Link>
        ))}
      </section>
    </div>
  );
}

export function PhoneticsTopicPage() {
  const { slug } = useParams();
  const [topic, setTopic] = useState<{
    slug: string;
    title: string;
    lesson: { title: string; content: LessonContent };
  } | null>(null);

  useEffect(() => {
    if (slug) api(`/phonetics/topics/${slug}`).then(setTopic);
  }, [slug]);

  if (!topic) return <p className="text-ink-soft">Открываем тему…</p>;

  return (
    <div className="mx-auto grid max-w-3xl gap-6">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <Link to="/app/sounds" className="text-sm text-terra">
            ← Все звуки
          </Link>
          <h1 className="font-display mt-2 text-4xl">{topic.title}</h1>
          <p className="mt-1 text-ink-soft">{topic.lesson.title}</p>
        </div>
        <VoiceControls />
      </div>
      <LessonView content={topic.lesson.content} />
    </div>
  );
}
