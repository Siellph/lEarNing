import { useEffect, useMemo, useState } from "react";
import { CheckCircle2, CircleAlert } from "lucide-react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { fullSentenceInstruction, kindLabel } from "../lib/kindLabels";
import { extractEnglish, looksEnglish, speakableEnglish } from "../lib/speech";
import type { QuizOptions } from "../lib/match";
import { MatchQuestion } from "../components/MatchQuestion";
import { PromptWithBlanks, countBlanks, joinGapAnswers } from "../components/PromptWithBlanks";
import { SpeakButton, VoiceControls } from "../components/SpeakButton";
import { useAuth } from "../context/AuthContext";

type Question = { id: number; kind: string; prompt: string; options?: QuizOptions; sort_order: number };
type Detail = {
  id: number;
  kind?: string;
  prompt: string;
  given: string;
  correct: boolean;
  expected: string;
  explanation: string;
};

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
          <Link key={exam.id} to={`/app/exams/${exam.id}`} className="card card-lift p-6">
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
    bank_size?: number;
    sample_size?: number;
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
          <p className="text-sm text-ink-soft">
            Проходной балл {meta.passing_score}%
            {meta.bank_size && meta.sample_size
              ? ` · в попытке ${meta.sample_size} из банка ${meta.bank_size}`
              : ""}
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-3">
          <VoiceControls />
          {!result && <div className="rounded-full bg-card px-4 py-2 font-semibold">{clock}</div>}
        </div>
      </div>
      {result ? (
        <div className="grid gap-4">
          <div className={`quiz-card p-6 ${result.passed ? "quiz-card-ok" : "quiz-card-bad"}`}>
            <p className="font-display text-3xl">{result.score}%</p>
            <p className="mt-1">{result.passed ? "Зачёт. Тема закреплена." : "Пока не зачёт. Разберите ошибки и попробуйте снова."}</p>
          </div>
          {result.details.map((item, i) => (
            <article key={item.id} className={`quiz-card ${item.correct ? "quiz-card-ok" : "quiz-card-bad"}`}>
              <header className="quiz-card-head">
                <span className="quiz-kind">
                  {i + 1}. {kindLabel(item.kind || "")}
                </span>
                {item.correct ? (
                  <span className="quiz-status-ok">
                    <CheckCircle2 size={14} /> Верно
                  </span>
                ) : null}
              </header>
              <div className="grid gap-3 p-5">
                <p className="font-medium leading-relaxed">
                  <PromptWithBlanks text={item.prompt} />
                </p>
                <p className="text-sm text-ink-soft">Ваш ответ: {item.given || "—"}</p>
                {!item.correct && (
                  <div className="quiz-feedback is-bad">
                    <div className="quiz-feedback-title">
                      <CircleAlert size={18} /> Нужно иначе
                    </div>
                    <p className="quiz-feedback-expected">
                      Верный ответ: <strong>{item.expected}</strong>
                    </p>
                    {item.explanation && <p className="quiz-feedback-note">{item.explanation}</p>}
                  </div>
                )}
                {item.correct && item.explanation && (
                  <div className="quiz-feedback is-ok">
                    <div className="quiz-feedback-title">
                      <CheckCircle2 size={18} /> Отлично
                    </div>
                    <p className="quiz-feedback-note">{item.explanation}</p>
                  </div>
                )}
              </div>
            </article>
          ))}
        </div>
      ) : (
        <div className="grid gap-5">
          {meta.questions.map((q, i) => (
            <AssessmentQuestion
              key={q.id}
              index={i}
              question={q}
              value={answers[q.id] || ""}
              onChange={(next) => setAnswers((a) => ({ ...a, [q.id]: next }))}
            />
          ))}
          <button className="btn btn-primary justify-self-start" onClick={submit} disabled={busy}>
            {busy ? "Считаем…" : "Сдать работу"}
          </button>
        </div>
      )}
    </div>
  );
}

function AssessmentQuestion({
  index,
  question: q,
  value,
  onChange,
}: {
  index: number;
  question: Question;
  value: string;
  onChange: (next: string) => void;
}) {
  const blankCount = countBlanks(q.prompt);
  const isMatch = q.kind === "match";
  const isMcq = Boolean(q.options && Array.isArray(q.options));
  const useInlineGaps = blankCount > 0 && !isMatch && !isMcq;
  const [blanks, setBlanks] = useState<string[]>(() => Array.from({ length: blankCount }, () => ""));
  const speakText = speakableEnglish(q.prompt);
  const showSpeak = Boolean(extractEnglish(q.prompt) || speakText);
  const rewriteHint = fullSentenceInstruction(q.kind, blankCount > 0);

  return (
    <article className="quiz-card">
      <header className="quiz-card-head">
        <span className="quiz-kind">
          {index + 1}. {kindLabel(q.kind)}
        </span>
      </header>
      <div className="grid gap-4 p-5 sm:p-6">
        <div className="flex items-start justify-between gap-3">
          <p className="text-[1.05rem] leading-relaxed sm:text-lg">
            <PromptWithBlanks
              text={q.prompt}
              values={useInlineGaps ? blanks : undefined}
              onChange={
                useInlineGaps
                  ? (next) => {
                      setBlanks(next);
                      onChange(joinGapAnswers(next));
                    }
                  : undefined
              }
            />
          </p>
          {showSpeak && <SpeakButton text={q.prompt} speak={speakText} />}
        </div>
        {rewriteHint && !isMcq && !isMatch && <p className="quiz-hint">{rewriteHint}</p>}
        {isMatch ? (
          <MatchQuestion options={q.options} value={value} onChange={onChange} />
        ) : isMcq && Array.isArray(q.options) ? (
          <div className="grid gap-2">
            {q.options.map((opt) => (
              <div key={opt} className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => onChange(opt)}
                  className={`quiz-choice ${value === opt ? "is-selected" : ""}`}
                >
                  {opt}
                </button>
                {looksEnglish(opt) && <SpeakButton text={opt} />}
              </div>
            ))}
          </div>
        ) : useInlineGaps ? null : (
          <input
            className="field"
            value={value}
            onChange={(e) => onChange(e.target.value)}
            placeholder={rewriteHint ? "Введите предложение целиком" : "Введите ответ"}
          />
        )}
      </div>
    </article>
  );
}
