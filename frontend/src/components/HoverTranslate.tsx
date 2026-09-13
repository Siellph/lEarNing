import type { ReactNode } from "react";
import { lookupGloss } from "../lib/glossary";
import { isMetaParenHint } from "../lib/speech";

/** Latin words incl. accented letters (café → cafe after NFD in lookupGloss). */
const TOKEN_RE = /([A-Za-zÀ-ÿ]+(?:'[A-Za-z]+)?|[^A-Za-zÀ-ÿ]+)/g;
const LATIN_WORD = /^[A-Za-zÀ-ÿ]+(?:'[A-Za-z]+)?$/;
const PAREN_CHUNK = /(\([^)]+\))/;

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

function wrapTokens(text: string, keyPrefix: string): ReactNode[] {
  if (!text) return [];
  const parts = text.match(TOKEN_RE) || [text];
  return parts.map((part, i) =>
    LATIN_WORD.test(part) ? (
      <WordTip key={`${keyPrefix}-${i}-${part}`} word={part} />
    ) : (
      <span key={`${keyPrefix}-${i}-${part}`}>{part}</span>
    ),
  );
}

/**
 * Wrap English words with RU hover glosses when known in the offline glossary.
 * Intended for **lesson example** lines only — not quiz prompts or UI chrome.
 */
export function withHoverTranslate(text: string): ReactNode[] {
  if (!text) return [];
  // Keep grammar hints like `(be)` plain — same scope as TTS stripMetaParentheticals.
  const chunks = text.split(PAREN_CHUNK);
  const nodes: ReactNode[] = [];
  chunks.forEach((chunk, i) => {
    if (!chunk) return;
    if (chunk.startsWith("(") && chunk.endsWith(")")) {
      const inner = chunk.slice(1, -1);
      if (isMetaParenHint(inner)) {
        nodes.push(<span key={`meta-${i}`}>{chunk}</span>);
        return;
      }
    }
    nodes.push(...wrapTokens(chunk, `c${i}`));
  });
  return nodes;
}

/** Lesson example / compare English: hover gloss per known word (examples only). */
export function HoverTranslateText({
  text,
  className = "",
}: {
  text: string;
  className?: string;
}) {
  return <span className={className}>{withHoverTranslate(text)}</span>;
}
