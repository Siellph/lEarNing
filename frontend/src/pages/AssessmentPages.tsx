import { useEffect, useMemo, useRef, useState } from "react";
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
import { useSearchHighlight } from "../lib/searchHighlight";

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
type HistoryItem = {
  id: number;
  score: number | null;
  passed: boolean | null;
  status: string;
  started_at: string;
  created_at: string;
};
type Meta = {
  title: string;
  description?: string;
  time_limit_sec: number;
  passing_score: number;
  bank_size: number;
  sample_size: number;
  module?: { title: string; slug?: string };
  level?: { code: string };
  active_attempt: { id: number; started_at: string; ends_at: string | null; remaining_sec: number | null } | null;
  history: HistoryItem[];
  last_attempt: { score: number; passed: boolean } | null;
};
type AttemptPayload = {
  id: number;
  status: string;
  answers: Record<string, string>;
  questions?: Question[];
  ends_at: string | null;
  remaining_sec: number | null;
  score?: number | null;
  passed?: boolean | null;
  details?: Detail[] | null;
  passing_score?: number;
};
type Phase = "lobby" | "running" | "results";

function storageKey(kind: "test" | "exam", id: number) {
  return `learning_attempt_${kind}_${id}`;
}

function formatClock(sec: number) {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${m}:${String(s).padStart(2, "0")}`;
}

function formatWhen(iso: string) {
  try {
    return new Date(iso).toLocaleString("ru-RU", { dateStyle: "short", timeStyle: "short" });
  } catch {
    return iso;
  }
}

function remainingFromDeadline(endsAt: string | null, fallback: number | null) {
  if (endsAt) {
    const ms = new Date(endsAt).getTime() - Date.now();
    return Math.max(0, Math.floor(ms / 1000));
  }
  return fallback ?? null;
}

function splitGapValue(value: string, blankCount: number): string[] {
  if (blankCount <= 1) return [value || ""];
  const parts = value.split(" / ");
  if (parts.length === blankCount) return parts;
  return Array.from({ length: blankCount }, (_, i) => parts[i] || "");
}

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
  useSearchHighlight(exams.length > 0);

  return (
    <div className="grid gap-6">
      <div>
        <p className="text-sm uppercase tracking-[0.18em] text-terra">Контроль уровня</p>
        <h1 className="font-display mt-1 text-4xl">Экзамены</h1>
        <p className="mt-2 max-w-2xl text-ink-soft">Один экзамен на каждый уровень CEFR. Проходной балл — 75%.</p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {exams.map((exam) => (
          <Link key={exam.id} to={`/app/exams/${exam.id}`} data-search-id={String(exam.id)} className="card card-lift p-6">
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
  const [meta, setMeta] = useState<Meta | null>(null);
  const [phase, setPhase] = useState<Phase>("lobby");
  const [attemptId, setAttemptId] = useState<number | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [endsAt, setEndsAt] = useState<string | null>(null);
  const [left, setLeft] = useState<number | null>(null);
  const [result, setResult] = useState<{ score: number; passed: boolean; passing_score: number; details: Detail[] } | null>(
    null,
  );
  const [busy, setBusy] = useState(false);
  const [sent, setSent] = useState(false);
  const [bootError, setBootError] = useState("");
  const answersRef = useRef(answers);
  answersRef.current = answers;

  const basePath = kind === "test" ? `/tests/${id}` : `/exams/${id}`;
  const attemptBase = kind === "test" ? "/tests/attempts" : "/exams/attempts";

  const applyAttempt = (data: AttemptPayload) => {
    setAttemptId(data.id);
    localStorage.setItem(storageKey(kind, id), String(data.id));
    setQuestions(data.questions || []);
    setAnswers(data.answers || {});
    setEndsAt(data.ends_at);
    setLeft(remainingFromDeadline(data.ends_at, data.remaining_sec));
    setPhase("running");
    setResult(null);
    setSent(false);
  };

  const loadMeta = async () => {
    const data = await api<Meta>(basePath);
    setMeta(data);
    return data;
  };

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const data = await loadMeta();
        if (cancelled) return;
        if (data.active_attempt) {
          const active = await api<AttemptPayload>(`${basePath}/attempts/active`);
          if (cancelled) return;
          if (active.status === "in_progress") {
            applyAttempt(active);
            return;
          }
        }
        const cachedId = localStorage.getItem(storageKey(kind, id));
        if (cachedId) {
          try {
            const finished = await api<AttemptPayload & { passing_score: number; details: Detail[] }>(
              `${basePath}/attempts/${cachedId}`,
            );
            if (cancelled) return;
            if (finished.status === "submitted") {
              setResult({
                score: finished.score ?? 0,
                passed: Boolean(finished.passed),
                passing_score: finished.passing_score ?? data.passing_score,
                details: finished.details || [],
              });
              setPhase("results");
              localStorage.removeItem(storageKey(kind, id));
              return;
            }
          } catch {
            localStorage.removeItem(storageKey(kind, id));
          }
        }
        setPhase("lobby");
      } catch (e) {
        if (!cancelled) setBootError(e instanceof Error ? e.message : "Не удалось открыть");
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [kind, id]);

  useEffect(() => {
    if (phase !== "running" || left == null || result || sent) return;
    if (left <= 0) {
      submit();
      return;
    }
    const t = setTimeout(() => setLeft(remainingFromDeadline(endsAt, left - 1)), 1000);
    return () => clearTimeout(t);
  }, [left, phase, result, sent, endsAt]);

  useEffect(() => {
    if (phase !== "running" || !attemptId || result) return;
    const t = setInterval(() => {
      api(`${attemptBase}/${attemptId}`, {
        method: "PATCH",
        body: JSON.stringify({ answers: answersRef.current }),
      }).catch(() => undefined);
    }, 15000);
    return () => clearInterval(t);
  }, [phase, attemptId, result, attemptBase]);

  const start = async () => {
    setBusy(true);
    setBootError("");
    try {
      const data = await api<AttemptPayload>(`${basePath}/attempts`, { method: "POST" });
      applyAttempt(data);
    } catch (e) {
      setBootError(e instanceof Error ? e.message : "Не удалось начать");
    } finally {
      setBusy(false);
    }
  };

  const continueActive = async () => {
    setBusy(true);
    try {
      const data = await api<AttemptPayload>(`${basePath}/attempts/active`);
      applyAttempt(data);
    } catch (e) {
      setBootError(e instanceof Error ? e.message : "Активная попытка не найдена");
      await loadMeta();
      setPhase("lobby");
    } finally {
      setBusy(false);
    }
  };

  const submit = async () => {
    if (!attemptId || busy || result || sent) return;
    setSent(true);
    setBusy(true);
    try {
      await api(`${attemptBase}/${attemptId}`, {
        method: "PATCH",
        body: JSON.stringify({ answers: answersRef.current }),
      }).catch(() => undefined);
      const data = await api<{ score: number; passed: boolean; passing_score: number; details: Detail[] }>(
        `${attemptBase}/${attemptId}/submit`,
        { method: "POST", body: JSON.stringify({ answers: answersRef.current }) },
      );
      setResult(data);
      setPhase("results");
      localStorage.removeItem(storageKey(kind, id));
      refresh();
      loadMeta().catch(() => undefined);
    } finally {
      setBusy(false);
    }
  };

  const openHistory = async (historyId: number) => {
    setBusy(true);
    try {
      const data = await api<AttemptPayload & { passing_score: number; details: Detail[] }>(
        `${basePath}/attempts/${historyId}`,
      );
      if (data.status === "in_progress" && data.questions) {
        applyAttempt(data);
        return;
      }
      setResult({
        score: data.score ?? 0,
        passed: Boolean(data.passed),
        passing_score: data.passing_score ?? meta?.passing_score ?? 0,
        details: data.details || [],
      });
      setPhase("results");
      setAttemptId(data.id);
    } catch (e) {
      setBootError(e instanceof Error ? e.message : "Не удалось открыть попытку");
    } finally {
      setBusy(false);
    }
  };

  const clock = useMemo(() => {
    if (left == null) return "";
    return formatClock(left);
  }, [left]);

  if (bootError && !meta) return <p className="text-terra">{bootError}</p>;
  if (!meta) return <p className="text-ink-soft">Готовим задания…</p>;

  const minutes = Math.round((meta.time_limit_sec || 0) / 60);

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
          {phase === "running" && !result && left != null && (
            <div className="rounded-full bg-card px-4 py-2 font-semibold">{clock}</div>
          )}
        </div>
      </div>

      {phase === "lobby" && (
        <div className="grid gap-5">
          <div className="card grid gap-3 p-6">
            <h2 className="font-display text-2xl">Перед стартом</h2>
            <ul className="grid gap-2 text-sm text-ink-soft">
              <li>
                В этой попытке будет <strong className="text-ink">{meta.sample_size}</strong> вопросов
                {meta.bank_size > meta.sample_size ? ` (выборка из ${meta.bank_size})` : ""}.
              </li>
              <li>
                {meta.time_limit_sec
                  ? `Лимит времени: ${minutes} мин. Таймер запускается только после «Начать» и считается по серверному дедлайну.`
                  : "Ограничения по времени нет."}
              </li>
              <li>
                Нужно набрать не меньше <strong className="text-ink">{meta.passing_score}%</strong>.
              </li>
              <li>
                Обновление страницы или уход и возврат не сбрасывают попытку: сохранятся те же вопросы, ответы и оставшееся
                время.
              </li>
            </ul>
            {bootError && <p className="text-sm text-terra">{bootError}</p>}
            <div className="mt-2 flex flex-wrap gap-3">
              {meta.active_attempt ? (
                <button className="btn btn-primary" onClick={continueActive} disabled={busy}>
                  {busy ? "Открываем…" : "Продолжить попытку"}
                </button>
              ) : (
                <button className="btn btn-primary" onClick={start} disabled={busy}>
                  {busy ? "Готовим…" : "Начать"}
                </button>
              )}
            </div>
          </div>

          {meta.history.length > 0 && (
            <section className="grid gap-3">
              <h2 className="font-display text-2xl">История попыток</h2>
              <div className="grid gap-2">
                {meta.history.map((item) => (
                  <button
                    key={item.id}
                    type="button"
                    className="card flex flex-wrap items-center justify-between gap-3 p-4 text-left hover:bg-paper"
                    onClick={() => openHistory(item.id)}
                    disabled={busy}
                  >
                    <span className="text-sm text-ink-soft">{formatWhen(item.created_at)}</span>
                    <span className={`font-semibold ${item.passed ? "text-sage" : "text-terra"}`}>
                      {item.score ?? "—"}%{item.passed ? " — зачёт" : " — не зачёт"}
                    </span>
                  </button>
                ))}
              </div>
            </section>
          )}
        </div>
      )}

      {phase === "results" && result && (
        <div className="grid gap-4">
          <div className={`quiz-card p-6 ${result.passed ? "quiz-card-ok" : "quiz-card-bad"}`}>
            <p className="font-display text-3xl">{result.score}%</p>
            <p className="mt-1">
              {result.passed ? "Зачёт. Тема закреплена." : "Пока не зачёт. Разберите ошибки и попробуйте снова."}
            </p>
            <div className="mt-4 flex flex-wrap gap-3">
              <button
                className="btn btn-primary"
                onClick={() => {
                  setResult(null);
                  setPhase("lobby");
                  setAttemptId(null);
                  setQuestions([]);
                  setAnswers({});
                  loadMeta();
                }}
              >
                К лобби
              </button>
              {!meta.active_attempt && (
                <button className="btn" onClick={start} disabled={busy}>
                  Новая попытка
                </button>
              )}
            </div>
          </div>
          {result.details.map((item, i) => (
            <article key={`${item.id}-${i}`} className={`quiz-card ${item.correct ? "quiz-card-ok" : "quiz-card-bad"}`}>
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
      )}

      {phase === "running" && (
        <div className="grid gap-5">
          {questions.map((q, i) => (
            <AssessmentQuestion
              key={q.id}
              index={i}
              question={q}
              value={answers[String(q.id)] || ""}
              onChange={(next) => setAnswers((a) => ({ ...a, [String(q.id)]: next }))}
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
  const [blanks, setBlanks] = useState<string[]>(() =>
    useInlineGaps ? splitGapValue(value, blankCount) : Array.from({ length: blankCount }, () => ""),
  );
  const speakText = speakableEnglish(q.prompt);
  const showSpeak = Boolean(extractEnglish(q.prompt) || speakText);
  const rewriteHint = fullSentenceInstruction(q.kind, blankCount > 0);

  useEffect(() => {
    if (!useInlineGaps) return;
    setBlanks(splitGapValue(value, blankCount));
  }, [q.id]);

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
