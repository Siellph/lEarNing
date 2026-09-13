import type { ReactNode } from "react";
import { lookupGloss } from "../lib/glossary";

const TOKEN_RE = /([A-Za-z]+(?:'[A-Za-z]+)?|[^A-Za-z]+)/g;
const LATIN_WORD = /^[A-Za-z]+(?:'[A-Za-z]+)?$/;

function WordTip({ word }: { word: string }) {
  const gloss = lookupGloss(word);
  if (!gloss) return <>{word}</>;
  return (
    <span className="word-tip" tabIndex={0}>
      {word}
      <span className="word-tip-bubble" role="tooltip">
        {gloss}
      </span>
    </span>
  );
}

/** Wrap English words so hover/focus shows a Russian gloss when known. */
export function withHoverTranslate(text: string): ReactNode[] {
  const parts = text.match(TOKEN_RE) || [text];
  return parts.map((part, i) =>
    LATIN_WORD.test(part) ? <WordTip key={`${i}-${part}`} word={part} /> : <span key={`${i}-${part}`}>{part}</span>,
  );
}

export function HoverTranslateText({
  text,
  className = "",
}: {
  text: string;
  className?: string;
}) {
  return <span className={className}>{withHoverTranslate(text)}</span>;
}
