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

/** Collapse spaces / punctuation the way scoring tolerates shortened left keys. */
function normMatchKey(value: string): string {
  return (value || "")
    .trim()
    .toLowerCase()
    .replace(/[\s+/→\-]+/g, "");
}

function bestLeftSlot(key: string, left: string[], used: Set<string>): string | null {
  if (left.includes(key) && !used.has(key)) return key;
  const kn = normMatchKey(key);
  const ranked: { score: number; opt: string }[] = [];
  for (const opt of left) {
    if (used.has(opt)) continue;
    if (opt === key) return opt;
    const on = normMatchKey(opt);
    if (kn && on && kn === on) ranked.push({ score: 0, opt });
    else if (kn && on && (kn.includes(on) || on.includes(kn))) {
      ranked.push({ score: 1 + Math.abs(on.length - kn.length), opt });
    } else if (key.includes(opt) || opt.includes(key)) {
      ranked.push({ score: 2 + Math.abs(opt.length - key.length), opt });
    }
  }
  ranked.sort((a, b) => a.score - b.score);
  return ranked[0]?.opt ?? null;
}

/**
 * Rewrite pair keys onto the current left slot labels.
 * Needed when a restored / scored answer used shortened keys (e.g. `book=a`
 * vs slot `___ book`) — scoring accepts that, exact UI lookup does not.
 */
export function alignMatchPairs(left: string[], pairs: Record<string, string>): Record<string, string> {
  if (!left.length) return { ...pairs };
  const used = new Set<string>();
  const aligned: Record<string, string> = {};
  for (const [key, right] of Object.entries(pairs)) {
    if (!right) continue;
    const slot = bestLeftSlot(key, left, used) ?? key;
    used.add(slot);
    aligned[slot] = right;
  }
  return aligned;
}

/** Prefer user pairs; if they do not fill every slot and `fallback` can, use fallback. */
export function resolveMatchPairs(
  left: string[],
  value: string,
  fallback?: string | null,
): Record<string, string> {
  const fromValue = alignMatchPairs(left, parseMatchAnswer(value));
  const fills = left.length > 0 && left.every((slot) => Boolean(fromValue[slot]));
  if (fills || !fallback?.trim()) return fromValue;
  const fromFallback = alignMatchPairs(left, parseMatchAnswer(fallback));
  if (left.every((slot) => Boolean(fromFallback[slot]))) return fromFallback;
  return fromValue;
}

export function shuffleList<T>(items: T[]): T[] {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}
