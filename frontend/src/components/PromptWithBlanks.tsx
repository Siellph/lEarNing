import type { KeyboardEvent, ReactNode } from "react";
import { withHoverTranslate } from "./HoverTranslate";

const BLANK_RE = /___+/g;

export function countBlanks(text: string): number {
  return (text.match(BLANK_RE) || []).length;
}

/** Join multi-gap answers the way seed keys expect (`a / b`); scoring also accepts space forms. */
export function joinGapAnswers(parts: string[]): string {
  const trimmed = parts.map((p) => p.trim());
  if (trimmed.length <= 1) return trimmed[0] || "";
  return trimmed.join(" / ");
}

type PromptWithBlanksProps = {
  text: string;
  className?: string;
  /** When set, each `___` becomes an inline input (gap-fill). */
  values?: string[];
  onChange?: (values: string[]) => void;
  onSubmit?: () => void;
  disabled?: boolean;
  /** Hover RU gloss on English words (default on). */
  translate?: boolean;
};

/** Renders prompt text, replacing ___ with a dashed blank (read-only) or inline input. */
export function PromptWithBlanks({
  text,
  className = "",
  values,
  onChange,
  onSubmit,
  disabled = false,
  translate = true,
}: PromptWithBlanksProps) {
  const editable = Array.isArray(values) && typeof onChange === "function";
  const renderText = (chunk: string, key: string): ReactNode =>
    translate ? <span key={key}>{withHoverTranslate(chunk)}</span> : <span key={key}>{chunk}</span>;

  if (!text.includes("___")) {
    return <span className={className}>{translate ? withHoverTranslate(text) : text}</span>;
  }

  const parts = text.split(BLANK_RE);
  const nodes: ReactNode[] = [];

  parts.forEach((part, index) => {
    nodes.push(renderText(part, `t-${index}`));
    if (index >= parts.length - 1) return;

    if (editable) {
      const raw = values[index] ?? "";
      nodes.push(
        <input
          key={`b-${index}`}
          type="text"
          className="gap-blank gap-blank-input"
          value={raw}
          disabled={disabled}
          autoComplete="off"
          autoCorrect="off"
          autoCapitalize="off"
          spellCheck={false}
          aria-label={`Пропуск ${index + 1}`}
          size={Math.max(4, Math.min(18, raw.length + 2))}
          onChange={(e) => {
            const next = values.slice();
            while (next.length < parts.length - 1) next.push("");
            next[index] = e.target.value;
            onChange(next);
          }}
          onKeyDown={(e: KeyboardEvent<HTMLInputElement>) => {
            if (e.key === "Enter") {
              e.preventDefault();
              onSubmit?.();
            }
          }}
        />,
      );
      return;
    }

    nodes.push(
      <span key={`b-${index}`} className="gap-blank" aria-hidden="true">
        &nbsp;&nbsp;&nbsp;&nbsp;
      </span>,
    );
  });

  return <span className={className}>{nodes}</span>;
}
