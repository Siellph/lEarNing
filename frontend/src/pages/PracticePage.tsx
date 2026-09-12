import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { Quiz, type QuizItem } from "../components/Quiz";
import { useAuth } from "../context/AuthContext";

export function PracticePage() {
  const { slug } = useParams();
  const { refresh } = useAuth();
  const [pack, setPack] = useState<{ module: { slug: string; title: string }; exercises: QuizItem[] } | null>(null);

  useEffect(() => {
    if (slug) api(`/grammar/modules/${slug}/practice`).then(setPack);
  }, [slug]);

  if (!pack) return <p className="text-ink-soft">Готовим упражнения…</p>;

  return (
    <div className="mx-auto grid max-w-3xl gap-6">
      <div>
        <Link to={`/app/module/${pack.module.slug}`} className="text-sm text-terra">
          ← {pack.module.title}
        </Link>
        <h1 className="font-display mt-2 text-4xl">Практика</h1>
        <p className="mt-2 text-ink-soft">Ответьте на задания. Объяснение появится сразу после проверки.</p>
      </div>
      <Quiz
        items={pack.exercises}
        onCheck={async (id, answer) => {
          const res = await api<{ correct: boolean; explanation: string; expected?: string | null }>(
            `/practice/exercises/${id}/check`,
            { method: "POST", body: JSON.stringify({ answer }) },
          );
          if (res.correct) refresh();
          return res;
        }}
      />
      <Link to={`/app/module/${pack.module.slug}/test`} className="btn btn-sage justify-self-start">
        Перейти к тесту модуля
      </Link>
    </div>
  );
}
