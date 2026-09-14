import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { LessonView, type LessonContent } from "../components/LessonView";

export function LessonPage() {
  const { slug, lessonId } = useParams();
  const [data, setData] = useState<{ title: string; content: LessonContent; module: { slug: string; title: string } } | null>(null);

  useEffect(() => {
    if (slug && lessonId) api(`/grammar/modules/${slug}/lessons/${lessonId}`).then(setData);
  }, [slug, lessonId]);

  if (!data) return <p className="text-ink-soft">Открываем урок…</p>;

  return (
    <div className="mx-auto grid max-w-3xl gap-6">
      <div>
        <Link to={`/app/module/${data.module.slug}`} className="text-sm text-terra">
          ← {data.module.title}
        </Link>
        <h1 className="font-display mt-2 text-4xl">{data.title}</h1>
      </div>
      <LessonView content={data.content} />
      <div className="flex flex-wrap gap-3">
        <Link to={`/app/module/${data.module.slug}/practice`} className="btn btn-primary">
          Перейти к практике
        </Link>
        <Link to={`/app/module/${data.module.slug}`} className="btn btn-ghost">
          К модулю
        </Link>
      </div>
    </div>
  );
}
