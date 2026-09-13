import type { ReactNode } from "react";

/** Renders prompt text, replacing ___ with a dashed underline blank pill. */
export function PromptWithBlanks({ text, className = "" }: { text: string; className?: string }) {
  if (!text.includes("___")) {
    return <span className={className}>{text}</span>;
  }
  const parts = text.split("___");
  const nodes: ReactNode[] = [];
  parts.forEach((part, index) => {
    nodes.push(<span key={`t-${index}`}>{part}</span>);
    if (index < parts.length - 1) {
      nodes.push(
        <span key={`b-${index}`} className="gap-blank" aria-hidden="true">
          &nbsp;&nbsp;&nbsp;&nbsp;
        </span>,
      );
    }
  });
  return <span className={className}>{nodes}</span>;
}
