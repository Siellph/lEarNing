import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { extractEnglish, looksEnglish } from "../lib/speech";
import { SpeakButton } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";

type Question = { id: number; kind: string; prompt: string; options?: string[] | null; sort_order: number };
type Detail = { id: number; prompt: string; given: string; correct: boolean; expected: string; explanation: string };

export function TestPage() {
  const { slug } = useParams();
  const [testId, setTestId] = useState<number | null>(null);

  useEffect(() => {
    if (slug) api<{ test_id: number }>(`/tests/by-module/${slug}`).then((d) => setTestId(d.test_id));
  }, [slug]);

  if (!testId) return <p className="text-ink-soft">Открываем тест…</p>;
  return <AssessmentRunner kind="test" id={testId} back={`/app/module/${slug}`} />;
}

export function ExamsPage() {
  const [exams, setExams] = useState<
    {
      id: number;
      title: string;
      description: string;
      time_limit_sec: number;
      passing_score: number;
      question_count: number;
      level: { code: string; title: string };
      last_attempt: { score: number; passed: boolean } | null;
    }[]
  >([]);

  useEffect(() => {
    api("/exams").then(setExams);
  }, []);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Контроль уровня</p>
        <h1 className="font-display mt-1 text-4xl">Экзамены</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">Один экзамен на каждый уровень CEFR. Проходной балл — 75%.</p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {exams.map((exam) => (
          <Link key={exam.id} to={`/app/exams/${exam.id}`} className="card p-6 hover:border-terra/40">
            <p className="text-sm font-semibold text-terra">{exam.level.code}</p>
            <h2 className="font-display text-2xl">{exam.title}</h2>
            <p className="mt-2 text-sm text-ink-soft">{exam.description}</p>
            <p className="mt-4 text-sm">
              {exam.question_count} вопросов · {Math.round(exam.time_limit_sec / 60)} мин
            </p>
            {exam.last_attempt && (
              <p className={`mt-2 text-sm font-semibold ${exam.last_attempt.passed ? "text-sage" : "text-terra"}`}>
                Последняя попытка: {exam.last_attempt.score}% {exam.last_attempt.passed ? "— сдан" : "— не сдан"}
              </p>
            )}
          </Link>
        ))}
      </div>
    </div>
  );
}

export function ExamPage() {
  const { examId } = useParams();
  if (!examId) return null;
  return <AssessmentRunner kind="exam" id={Number(examId)} back="/app/exams" />;
}

function AssessmentRunner({ kind, id, back }: { kind: "test" | "exam"; id: number; back: string }) {
  const { refresh } = useAuth();
  const [meta, setMeta] = useState<{
    title: string;
    time_limit_sec: number;
    passing_score: number;
    questions: Question[];
    module?: { title: string };
    level?: { code: string };
  } | null>(null);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [left, setLeft] = useState<number | null>(null);
  const [result, setResult] = useState<{ score: number; passed: boolean; passing_score: number; details: Detail[] } | null>(null);
  const [busy, setBusy] = useState(false);
  const [sent, setSent] = useState(false);

  useEffect(() => {
    const path = kind === "test" ? `/tests/${id}` : `/exams/${id}`;
    api<typeof meta>(path).then((data) => {
      setMeta(data);
      setLeft(data?.time_limit_sec ?? 0);
    });
  }, [kind, id]);

  useEffect(() => {
    if (left == null || result || sent) return;
    if (left <= 0) {
      submit();
      return;
    }
    const t = setTimeout(() => setLeft((v) => (v == null ? v : v - 1)), 1000);
    return () => clearTimeout(t);
  }, [left, result]);

  const submit = async () => {
    if (!meta || busy || result || sent) return;
    setSent(true);
    setBusy(true);
    try {
      const path = kind === "test" ? `/tests/${id}/submit` : `/exams/${id}/submit`;
      const data = await api<typeof result>(path, { method: "POST", body: JSON.stringify({ answers }) });
      setResult(data);
      refresh();
    } finally {
      setBusy(false);
    }
  };

  const clock = useMemo(() => {
    if (left == null) return "";
    const m = Math.floor(left / 60);
    const s = left % 60;
    return `${m}:${String(s).padStart(2, "0")}`;
  }, [left]);

  if (!meta) return <p className="text-ink-soft">Готовим задания…</p>;

  return (
    <div className="mx-auto grid max-w-3xl gap-5">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <Link to={back} className="text-sm text-terra">
            ← Назад
          </Link>
          <h1 className="font-display mt-2 text-4xl">{meta.title}</h1>
          <p className="text-sm text-ink-soft">Проходной балл {meta.passing_score}%</p>
        </div>
        {!result && <div className="rounded-full bg-card px-4 py-2 font-semibold">{clock}</div>}
      </div>
      {result ? (
        <div className="grid gap-4">
          <div className={`card p-6 ${result.passed ? "border-sage" : "border-terra"}`}>
            <p className="font-display text-3xl">{result.score}%</p>
            <p className="mt-1">{result.passed ? "Зачёт. Тема закреплена." : "Пока не зачёт. Разберите ошибки и попробуйте снова."}</p>
          </div>
          {result.details.map((item, i) => (
            <article key={item.id} className="card p-5">
              <p className="text-sm text-ink-soft">{i + 1}.</p>
              <p className="mt-1 font-medium">{item.prompt}</p>
              <p className={`mt-2 text-sm ${item.correct ? "text-sage" : "text-rose"}`}>
                Ваш ответ: {item.given || "—"} {item.correct ? "" : `· верно: ${item.expected}`}
              </p>
              <p className="mt-2 text-sm text-ink-soft">{item.explanation}</p>
            </article>
          ))}
        </div>
      ) : (
        <div className="grid gap-4">
          {meta.questions.map((q, i) => (
            <article key={q.id} className="card p-5">
              <p className="mb-3 text-sm text-ink-soft">{i + 1}.</p>
              <div className="mb-3 flex items-start justify-between gap-3">
                <p className="text-lg">{q.prompt}</p>
                {extractEnglish(q.prompt) && <SpeakButton text={extractEnglish(q.prompt) || q.prompt} />}
              </div>
              {q.options ? (
                <div className="grid gap-2">
                  {q.options.map((opt) => (
                    <div key={opt} className="flex items-center gap-2">
                      <button
                        type="button"
                        onClick={() => setAnswers((a) => ({ ...a, [q.id]: opt }))}
                        className={`min-w-0 flex-1 rounded-xl border px-4 py-3 text-left ${
                          answers[q.id] === opt ? "border-terra bg-[#fff1eb]" : "border-line"
                        }`}
                      >
                        {opt}
                      </button>
                      {looksEnglish(opt) && <SpeakButton text={opt} />}
                    </div>
                  ))}
                </div>
              ) : (
                <input
                  className="field"
                  value={answers[q.id] || ""}
                  onChange={(e) => setAnswers((a) => ({ ...a, [q.id]: e.target.value }))}
                />
              )}
            </article>
          ))}
          <button className="btn btn-primary justify-self-start" onClick={submit} disabled={busy}>
            {busy ? "Считаем…" : "Сдать работу"}
          </button>
        </div>
      )}
    </div>
  );
}
