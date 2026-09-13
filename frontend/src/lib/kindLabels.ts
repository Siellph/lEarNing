/** Shared Russian labels for exercise kinds (Quiz + assessments). */
export const KIND_LABELS: Record<string, string> = {
  multiple_choice: "Выбор",
  fill_blank: "Пропуск",
  transform: "Преобразование",
  error_correction: "Исправление",
  order: "Порядок слов",
  match: "Соотнесение",
};

export function kindLabel(kind: string): string {
  return KIND_LABELS[kind] || "Задание";
}

/** Shown under the prompt when the learner must type a full rewritten sentence. */
export function fullSentenceInstruction(kind: string, hasBlanks: boolean): string | null {
  if (hasBlanks) return null;
  if (kind === "error_correction") {
    return "Перепишите предложение правильно целиком (не только глагол или исправленный фрагмент).";
  }
  if (kind === "transform") {
    return "Перепишите предложение целиком в нужной форме.";
  }
  return null;
}
