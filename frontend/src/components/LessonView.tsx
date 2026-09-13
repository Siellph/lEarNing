import { Fragment, type ReactNode } from "react";
import { speakableEnglish } from "../lib/speech";
import { HoverTranslateText } from "./HoverTranslate";
import { SpeakButton } from "./SpeakButton";

type Example = { en: string; ru: string };
type LessonTable = { headers: string[]; rows: string[][] };
type LessonCallout = { tone?: "key" | "warn" | "tip" | string; text: string };
type LessonPair = { wrong: string; right: string; note?: string };
type Rule = {
  title: string;
  body: string;
  examples?: Example[];
  tables?: LessonTable[];
  callouts?: LessonCallout[];
  pairs?: LessonPair[];
};
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

/** Light emphasis: **text** → highlighted span (no HTML from content). */
function renderEmphasized(text: string): ReactNode {
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  return parts.map((part, i) => {
    if (part.startsWith("**") && part.endsWith("**") && part.length > 4) {
      return (
        <strong key={i} className="lesson-em">
          {part.slice(2, -2)}
        </strong>
      );
    }
    return <Fragment key={i}>{part}</Fragment>;
  });
}

function BodyText({ text }: { text: string }) {
  const paragraphs = text.split(/\n\n+/).map((p) => p.trim()).filter(Boolean);
  if (paragraphs.length <= 1) {
    return <p className="mb-4 leading-7 text-ink-soft">{renderEmphasized(text)}</p>;
  }
  return (
    <div className="mb-4 grid gap-3">
      {paragraphs.map((p) => (
        <p key={p.slice(0, 48)} className="leading-7 text-ink-soft">
          {renderEmphasized(p)}
        </p>
      ))}
    </div>
  );
}

function RuleTable({ table }: { table: LessonTable }) {
  return (
    <div className="lesson-table-wrap mb-4">
      <table className="lesson-table">
        <thead>
          <tr>
            {table.headers.map((h) => (
              <th key={h}>{renderEmphasized(h)}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {table.rows.map((row, ri) => (
            <tr key={ri}>
              {row.map((cell, ci) => (
                <td key={ci}>{renderEmphasized(cell)}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function CalloutBlock({ item }: { item: LessonCallout }) {
  const tone = item.tone === "warn" || item.tone === "tip" ? item.tone : "key";
  return (
    <aside className={`lesson-callout lesson-callout-${tone} mb-4`}>
      <p className="leading-7">{renderEmphasized(item.text)}</p>
    </aside>
  );
}

function PairBlock({ item }: { item: LessonPair }) {
  return (
    <div className="lesson-pair mb-3">
      <div className="lesson-pair-wrong">
        <span className="lesson-pair-label">Неверно</span>
        <p className="font-medium">
          <HoverTranslateText text={item.wrong} />
        </p>
      </div>
      <div className="lesson-pair-right">
        <span className="lesson-pair-label">Верно</span>
        <p className="font-medium">
          <HoverTranslateText text={item.right} />
        </p>
      </div>
      {item.note ? <p className="lesson-pair-note">{renderEmphasized(item.note)}</p> : null}
    </div>
  );
}

function NoteBlock({ title, text }: { title: string; text: string }) {
  return (
    <section className="card p-5 sm:p-6">
      <h3>{title}</h3>
      <BodyText text={text} />
    </section>
  );
}

export function LessonView({ content }: { content: LessonContent }) {
  return (
    <div className="prose-lesson motion-stagger grid gap-6">
      <p className="text-lg leading-8 text-ink-soft">{renderEmphasized(content.intro)}</p>
      {content.articulation ? <NoteBlock title="Как это устроено" text={content.articulation} /> : null}
      {content.contrast ? <NoteBlock title="Не путайте" text={content.contrast} /> : null}
      {content.rules?.map((rule) => (
        <section key={rule.title} className="card p-5 sm:p-6">
          <h3>{rule.title}</h3>
          <BodyText text={rule.body} />
          {rule.tables?.map((t, i) => (
            <RuleTable key={`${rule.title}-t-${i}`} table={t} />
          ))}
          {rule.callouts?.map((c, i) => (
            <CalloutBlock key={`${rule.title}-c-${i}`} item={c} />
          ))}
          {!!rule.pairs?.length && (
            <div className="mb-4 grid gap-2">
              {rule.pairs.map((p) => (
                <PairBlock key={`${p.wrong}|${p.right}`} item={p} />
              ))}
            </div>
          )}
          <div className="grid gap-2">
            {rule.examples?.map((ex) => (
              <div key={ex.en} className="flex items-start justify-between gap-3 rounded-xl bg-paper px-4 py-3">
                <div>
                  {/* Hover RU glosses: lesson examples only (offline glossary). */}
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
              {row.note && <p className="mt-3 text-sm text-ink-soft">{renderEmphasized(row.note)}</p>}
            </div>
          ))}
        </section>
      )}
      {!!content.watch_out?.length && (
        <section className="rounded-2xl border border-[#f0c7b8] bg-[#fff4ef] p-5">
          <h3 className="mb-2">Типичные ошибки</h3>
          <ul className="grid gap-2 text-ink-soft">
            {content.watch_out.map((item) => (
              <li key={item}>• {renderEmphasized(item)}</li>
            ))}
          </ul>
        </section>
      )}
      {!!content.tips?.length && (
        <section className="card p-5 sm:p-6">
          <h3>Как слушать</h3>
          <ul className="grid gap-2 text-ink-soft">
            {content.tips.map((item) => (
              <li key={item}>• {renderEmphasized(item)}</li>
            ))}
          </ul>
        </section>
      )}
      {content.remember && (
        <section className="rounded-2xl bg-sage-soft p-5 text-sage">
          <p className="font-display text-xl">Главное</p>
          <p className="mt-2 leading-7">{renderEmphasized(content.remember)}</p>
        </section>
      )}
    </div>
  );
}
