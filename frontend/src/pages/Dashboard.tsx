import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client";
import { ProgressBar } from "../components/ProgressBar";
import { useAuth } from "../context/AuthContext";

type Progress = {
  modules: { completed: number; total: number };
  by_level: { code: string; title: string; completed: number; total: number }[];
  practice_correct: number;
  tests_passed: number;
  exams: { passed: number; total: number };
  vocab: { learned: number; total: number };
};

export function Dashboard() {
  const { user } = useAuth();
  const [data, setData] = useState<Progress | null>(null);

  useEffect(() => {
    api<Progress>("/progress/me").then(setData);
  }, []);

  if (!data) return <p className="text-ink-soft">Собираем прогресс…</p>;

  const grammarPct = data.modules.total ? Math.round((data.modules.completed / data.modules.total) * 100) : 0;

  return (
    <div className="dash-page">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Сегодня</p>
        <h1 className="font-display mt-1 text-[clamp(1.7rem,3.4vh,2.25rem)] leading-tight">
          Здравствуйте, {user?.name.split(" ")[0]}
        </h1>
        <p className="dash-lead max-w-2xl text-ink-soft">
          Сначала грамматика, затем звуки и слова. Нажимайте на динамик, чтобы услышать английскую речь.
        </p>
      </div>
      <div className="grid gap-[clamp(0.55rem,1.2vh,1rem)] sm:grid-cols-2 xl:grid-cols-4">
        <Stat title="Грамматика" value={`${data.modules.completed}/${data.modules.total}`} hint="модулей закрыто" />
        <Stat title="Практика" value={String(data.practice_correct)} hint="верных ответов" />
        <Stat title="Тесты" value={String(data.tests_passed)} hint="успешных попыток" />
        <Stat title="Словарь" value={`${data.vocab.learned}/${data.vocab.total}`} hint="слов в памяти" />
      </div>
      <section className="card p-[clamp(0.9rem,1.8vh,1.5rem)]">
        <div className="mb-[clamp(0.55rem,1.2vh,1rem)] flex items-center justify-between gap-4">
          <h2 className="font-display text-[clamp(1.25rem,2.4vh,1.5rem)]">Путь по CEFR</h2>
          <Link to="/app/grammar" className="btn btn-primary text-sm">
            Продолжить
          </Link>
        </div>
        <ProgressBar value={grammarPct} label="Весь курс" />
        <div className="mt-[clamp(0.7rem,1.6vh,1.5rem)] grid gap-3 md:grid-cols-2 xl:grid-cols-3">
          {data.by_level.map((level) => (
            <Link key={level.code} to={`/app/grammar/${level.code}`} className="rounded-2xl bg-paper px-4 py-[clamp(0.65rem,1.4vh,1rem)] hover:bg-paper-2">
              <div className="flex items-center justify-between">
                <p className="font-semibold">{level.code}</p>
                <span className="text-sm text-ink-soft">
                  {level.completed}/{level.total}
                </span>
              </div>
              <p className="dash-level-title mb-2 mt-1 text-sm text-ink-soft">{level.title}</p>
              <ProgressBar value={level.total ? (level.completed / level.total) * 100 : 0} />
            </Link>
          ))}
        </div>
      </section>
      <Link
        to="/app/sounds"
        className="card card-lift flex flex-col gap-2 p-[clamp(0.9rem,1.8vh,1.5rem)] sm:flex-row sm:items-center sm:justify-between"
      >
        <div>
          <p className="text-sm font-semibold text-terra">Произношение</p>
          <h2 className="font-display text-[clamp(1.25rem,2.4vh,1.5rem)]">Транскрипция, правила чтения и связная речь</h2>
          <p className="mt-1 text-sm text-ink-soft">
            Интерактивная таблица IPA и 10 блоков: от гласных до linking и weak forms.
          </p>
        </div>
        <span className="btn btn-primary self-start">Открыть звуки</span>
      </Link>
    </div>
  );
}

function Stat({ title, value, hint }: { title: string; value: string; hint: string }) {
  return (
    <div className="card p-[clamp(0.75rem,1.5vh,1.25rem)]">
      <p className="text-sm text-ink-soft">{title}</p>
      <p className="font-display mt-1 text-[clamp(1.5rem,2.8vh,1.875rem)] leading-tight">{value}</p>
      <p className="text-sm text-ink-soft">{hint}</p>
    </div>
  );
}
