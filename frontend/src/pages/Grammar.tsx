import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { ProgressBar } from "../components/ProgressBar";

type Level = {
  id: number;
  code: string;
  title: string;
  subtitle: string;
  description: string;
  module_count: number;
  completed_count: number;
};

export function GrammarLevels() {
  const [levels, setLevels] = useState<Level[]>([]);
  useEffect(() => {
    api<Level[]>("/grammar/levels").then(setLevels);
  }, []);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Грамматика</p>
        <h1 className="font-display mt-1 text-4xl">Все блоки курса</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">
          Структура соответствует CEFR и тематическим картам Cambridge, British Council и Oxford Practice Grammar.
        </p>
      </div>
      <div className="grid gap-4 lg:grid-cols-2">
        {levels.map((level) => (
          <Link key={level.code} to={`/app/grammar/${level.code}`} className="card card-lift p-6">
            <div className="flex items-start justify-between gap-3">
              <div>
                <p className="text-sm font-semibold text-terra">{level.code}</p>
                <h2 className="font-display text-2xl">{level.title}</h2>
                <p className="mt-1 text-ink-soft">{level.subtitle}</p>
              </div>
              <span className="rounded-full bg-paper-2 px-3 py-1 text-sm">
                {level.completed_count}/{level.module_count}
              </span>
            </div>
            <p className="mt-4 text-sm leading-6 text-ink-soft">{level.description}</p>
            <div className="mt-4">
              <ProgressBar value={level.module_count ? (level.completed_count / level.module_count) * 100 : 0} />
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

type ModuleRow = {
  id: number;
  slug: string;
  title: string;
  description: string;
  estimated_minutes: number;
  sources: string[];
  exercise_count: number;
  progress: { status: string; lesson_done: boolean; practice_score: number; test_score: number | null };
};

export function ModuleList() {
  const { code } = useParams();
  const [pack, setPack] = useState<{
    level: { code: string; title: string; subtitle: string; description: string };
    modules: ModuleRow[];
  } | null>(null);

  useEffect(() => {
    if (code) api(`/grammar/levels/${code}/modules`).then(setPack);
  }, [code]);

  if (!pack) return <p className="text-ink-soft">Загружаем модули…</p>;

  return (
    <div className="grid gap-6">
      <div>
        <Link to="/app/grammar" className="text-sm text-terra">
          ← Все уровни
        </Link>
        <h1 className="font-display mt-2 text-4xl">{pack.level.title}</h1>
        <p className="mt-2 max-w-3xl text-ink-soft">{pack.level.description}</p>
      </div>
      <div className="grid gap-3">
        {pack.modules.map((module, i) => (
          <Link key={module.slug} to={`/app/module/${module.slug}`} className="card card-lift flex flex-col gap-3 p-5 sm:flex-row sm:items-center">
            <div className="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-paper-2 font-display text-lg">
              {i + 1}
            </div>
            <div className="min-w-0 flex-1">
              <div className="flex flex-wrap items-center gap-2">
                <h2 className="font-semibold">{module.title}</h2>
                <Status status={module.progress.status} />
              </div>
              <p className="mt-1 text-sm text-ink-soft">{module.description}</p>
              <p className="mt-2 text-xs text-ink-soft">
                {module.estimated_minutes} мин · {module.exercise_count} упражнений
                {module.progress.test_score != null ? ` · тест ${module.progress.test_score}%` : ""}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

function Status({ status }: { status: string }) {
  const map: Record<string, string> = {
    completed: "Завершён",
    in_progress: "В работе",
    not_started: "Не начат",
  };
  const cls: Record<string, string> = {
    completed: "bg-sage-soft text-sage",
    in_progress: "bg-[#fff1eb] text-terra",
    not_started: "bg-paper-2 text-ink-soft",
  };
  return <span className={`rounded-full px-2.5 py-1 text-xs font-semibold ${cls[status] || cls.not_started}`}>{map[status] || status}</span>;
}
