import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";

type Module = {
  id: number;
  slug: string;
  title: string;
  description: string;
  estimated_minutes: number;
  sources: string[];
  level: { code: string; title: string };
  lessons: { id: number; title: string; sort_order: number }[];
  exercise_count: number;
  test: { id: number; title: string; time_limit_sec: number; passing_score: number; question_count: number } | null;
  progress: { status: string; lesson_done: boolean; practice_score: number; test_score: number | null };
};

function stepStatus(kind: "practice" | "test", progress: Module["progress"]): string {
  if (kind === "practice") {
    if (progress.practice_score >= 70) return "completed";
    if (progress.practice_score > 0) return "in_progress";
    return "not_started";
  }
  if ((progress.test_score || 0) >= 70) return "completed";
  if (progress.test_score != null) return "in_progress";
  return "not_started";
}

export function ModuleHub() {
  const { slug } = useParams();
  const [module, setModule] = useState<Module | null>(null);

  useEffect(() => {
    if (slug) api<Module>(`/grammar/modules/${slug}`).then(setModule);
  }, [slug]);

  if (!module) return <p className="text-ink-soft">Открываем модуль…</p>;
  const lesson = module.lessons[0];

  return (
    <div className="grid gap-6">
      <div>
        <Link to={`/app/grammar/${module.level.code}`} className="text-sm text-terra">
          ← {module.level.code}
        </Link>
        <h1 className="font-display mt-2 text-4xl">{module.title}</h1>
        <p className="mt-2 max-w-3xl text-ink-soft">{module.description}</p>
        <p className="mt-3 text-sm text-ink-soft">
          {module.estimated_minutes} минут · источники: {module.sources.join(" · ")}
        </p>
      </div>
      <div className="grid gap-4 md:grid-cols-3">
        <Step
          n="01"
          title="Теория"
          text={lesson?.title || "Урок"}
          to={lesson ? `/app/module/${module.slug}/lesson/${lesson.id}` : "#"}
        />
        <Step
          n="02"
          title="Практика"
          text={`${module.exercise_count} заданий`}
          to={`/app/module/${module.slug}/practice`}
          status={stepStatus("practice", module.progress)}
          meta={module.progress.practice_score ? `${module.progress.practice_score}%` : undefined}
        />
        <Step
          n="03"
          title="Тест"
          text={
            module.test
              ? `${module.test.question_count} вопросов · ${Math.round(module.test.time_limit_sec / 60)} мин`
              : "Нет теста"
          }
          to={module.test ? `/app/module/${module.slug}/test` : "#"}
          status={stepStatus("test", module.progress)}
          meta={module.progress.test_score != null ? `${module.progress.test_score}%` : undefined}
        />
      </div>
    </div>
  );
}

function StatusBadge({ status }: { status: string }) {
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
  return (
    <span className={`rounded-full px-2.5 py-1 text-xs font-semibold ${cls[status] || cls.not_started}`}>
      {map[status] || status}
    </span>
  );
}

function Step({
  n,
  title,
  text,
  to,
  status,
  meta,
}: {
  n: string;
  title: string;
  text: string;
  to: string;
  status?: string;
  meta?: string;
}) {
  return (
    <Link to={to} className="card card-lift relative p-5">
      <div className="absolute right-4 top-4">
        <StatusBadge status={status} />
      </div>
      <div className="pr-24">
        <span className="font-display text-2xl text-terra">{n}</span>
        <h2 className="mt-3 font-semibold">{title}</h2>
        <p className="mt-1 text-sm text-ink-soft">{text}</p>
        {meta && <p className="mt-3 text-sm font-semibold">{meta}</p>}
      </div>
    </Link>
  );
}
