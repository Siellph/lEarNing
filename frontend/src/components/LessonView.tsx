import { speakableEnglish } from "../lib/speech";
import { HoverTranslateText } from "./HoverTranslate";
import { SpeakButton } from "./SpeakButton";

type Example = { en: string; ru: string };
type Rule = { title: string; body: string; examples?: Example[] };
type Compare = { left: string; right: string; note?: string };
export type LessonContent = {
  intro: string;
  rules: Rule[];
  compare?: Compare[];
  watch_out?: string[];
  remember?: string;
  articulation?: string;
  contrast?: string;
  tips?: string[];
};

function NoteBlock({ title, text }: { title: string; text: string }) {
  return (
    <section className="card p-5 sm:p-6">
      <h3>{title}</h3>
      <p className="leading-7 text-ink-soft">{text}</p>
    </section>
  );
}

export function LessonView({ content }: { content: LessonContent }) {
  return (
    <div className="prose-lesson grid gap-6">
      <p className="text-lg leading-8 text-ink-soft">{content.intro}</p>
      {content.articulation ? <NoteBlock title="Как это устроено" text={content.articulation} /> : null}
      {content.contrast ? <NoteBlock title="Не путайте" text={content.contrast} /> : null}
      {content.rules?.map((rule) => (
        <section key={rule.title} className="card p-5 sm:p-6">
          <h3>{rule.title}</h3>
          <p className="mb-4 leading-7 text-ink-soft">{rule.body}</p>
          <div className="grid gap-2">
            {rule.examples?.map((ex) => (
              <div key={ex.en} className="flex items-start justify-between gap-3 rounded-xl bg-paper px-4 py-3">
                <div>
                  <p className="font-medium">
                    <HoverTranslateText text={ex.en} />
                  </p>
                  <p className="text-sm text-ink-soft">{ex.ru}</p>
                </div>
                <SpeakButton text={ex.en} speak={speakableEnglish(ex.en)} />
              </div>
            ))}
          </div>
        </section>
      ))}
      {!!content.compare?.length && (
        <section className="grid gap-3 md:grid-cols-2">
          {content.compare.map((row) => (
            <div key={row.left} className="card p-5">
              <div className="flex items-start justify-between gap-3">
                <p className="font-medium">
                  <HoverTranslateText text={row.left} />
                </p>
                <SpeakButton text={row.left} speak={speakableEnglish(row.left)} />
              </div>
              <div className="mt-2 flex items-start justify-between gap-3">
                <p className="font-medium">
                  <HoverTranslateText text={row.right} />
                </p>
                <SpeakButton text={row.right} speak={speakableEnglish(row.right)} />
              </div>
              {row.note && <p className="mt-3 text-sm text-ink-soft">{row.note}</p>}
            </div>
          ))}
        </section>
      )}
      {!!content.watch_out?.length && (
        <section className="rounded-2xl border border-[#f0c7b8] bg-[#fff4ef] p-5">
          <h3 className="mb-2">Типичные ошибки</h3>
          <ul className="grid gap-2 text-ink-soft">
            {content.watch_out.map((item) => (
              <li key={item}>• {item}</li>
            ))}
          </ul>
        </section>
      )}
      {!!content.tips?.length && (
        <section className="card p-5 sm:p-6">
          <h3>Как слушать</h3>
          <ul className="grid gap-2 text-ink-soft">
            {content.tips.map((item) => (
              <li key={item}>• {item}</li>
            ))}
          </ul>
        </section>
      )}
      {content.remember && (
        <section className="rounded-2xl bg-sage-soft p-5 text-sage">
          <p className="font-display text-xl">Запомните</p>
          <p className="mt-2 leading-7">{content.remember}</p>
        </section>
      )}
    </div>
  );
}
