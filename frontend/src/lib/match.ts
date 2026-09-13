export type MatchSides = { left: string[]; right: string[] };

export type QuizOptions = string[] | MatchSides | null | undefined;

export function isMatchSides(options: QuizOptions): options is MatchSides {
  return !!options && !Array.isArray(options) && Array.isArray(options.left) && Array.isArray(options.right);
}

export function parseMatchSides(options: QuizOptions): MatchSides | null {
  if (isMatchSides(options)) {
    const left = options.left.map(String).filter((x) => x.trim());
    const right = options.right.map(String).filter((x) => x.trim());
    if (left.length && right.length) return { left, right };
    return null;
  }
  return null;
}

export function parseMatchAnswer(value: string): Record<string, string> {
  const map: Record<string, string> = {};
  for (const part of (value || "").split(";")) {
    const trimmed = part.trim();
    if (!trimmed.includes("=")) continue;
    const [l, r] = trimmed.split("=", 2);
    if (l.trim() && r.trim()) map[l.trim()] = r.trim();
  }
  return map;
}

export function formatMatchAnswer(pairs: Record<string, string>): string {
  return Object.entries(pairs)
    .filter(([, right]) => right)
    .map(([left, right]) => `${left}=${right}`)
    .join("; ");
}

export function shuffleList<T>(items: T[]): T[] {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}
