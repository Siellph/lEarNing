/** Shared Russian labels for exercise kinds (Quiz + assessments). */
export const KIND_LABELS: Record<string, string> = {
  multiple_choice: "Выбор",
  fill_blank: "Пропуск",
  transform: "Перепишите предложение",
  error_correction: "Исправление",
  order: "Порядок слов",
  match: "Соотнесение",
};

export function kindLabel(kind: string): string {
  return KIND_LABELS[kind] || "Задание";
}
