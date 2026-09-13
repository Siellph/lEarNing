import { ACCENT_KEY, RATE_KEY, canPersistPrefs, onConsentChange } from "./consent";

export type Accent = "en-GB" | "en-US";
export type SpeechRate = "slow" | "normal" | "fast";

export const SPEECH_RATES: Record<SpeechRate, number> = {
  slow: 0.65,
  normal: 0.88,
  fast: 1.15,
};

const DEFAULT_ACCENT: Accent = "en-GB";
const DEFAULT_RATE: SpeechRate = "normal";

let memoryAccent: Accent = DEFAULT_ACCENT;
let memoryRate: SpeechRate = DEFAULT_RATE;

function readStoredAccent(): Accent {
  try {
    return localStorage.getItem(ACCENT_KEY) === "en-US" ? "en-US" : DEFAULT_ACCENT;
  } catch {
    return DEFAULT_ACCENT;
  }
}

function readStoredRate(): SpeechRate {
  try {
    const stored = localStorage.getItem(RATE_KEY);
    if (stored === "slow" || stored === "fast" || stored === "normal") return stored;
  } catch {
    /* ignore */
  }
  return DEFAULT_RATE;
}

hydrateFromStorage();
onConsentChange(() => {
  if (canPersistPrefs()) {
    localStorage.setItem(ACCENT_KEY, memoryAccent);
    localStorage.setItem(RATE_KEY, memoryRate);
    return;
  }
  memoryAccent = DEFAULT_ACCENT;
  memoryRate = DEFAULT_RATE;
});

function hydrateFromStorage() {
  memoryAccent = readStoredAccent();
  memoryRate = readStoredRate();
}

export function getAccent(): Accent {
  return canPersistPrefs() ? readStoredAccent() : memoryAccent;
}

export function setAccent(accent: Accent) {
  memoryAccent = accent;
  if (canPersistPrefs()) localStorage.setItem(ACCENT_KEY, accent);
}

export function getRatePreset(): SpeechRate {
  return canPersistPrefs() ? readStoredRate() : memoryRate;
}

export function setRatePreset(preset: SpeechRate) {
  memoryRate = preset;
  if (canPersistPrefs()) localStorage.setItem(RATE_KEY, preset);
}

export function getRate(): number {
  return SPEECH_RATES[getRatePreset()];
}

function pickVoice(lang: Accent): SpeechSynthesisVoice | undefined {
  const voices = window.speechSynthesis.getVoices();
  const exact = voices.find((voice) => voice.lang === lang || voice.lang.replace("_", "-") === lang);
  if (exact) return exact;
  const prefix = voices.find((voice) => voice.lang.startsWith(lang.slice(0, 2)));
  return prefix;
}

const SEGMENT_CONNECTOR = /^(vs\.?|versus|v\.)$/i;

let voicesReady: Promise<void> | null = null;
let speakGeneration = 0;
let primed = false;
let priming = false;

function whenVoicesReady(): Promise<void> {
  if (typeof window === "undefined" || !window.speechSynthesis) return Promise.resolve();
  if (!voicesReady) {
    voicesReady = new Promise((resolve) => {
      const finish = () => resolve();
      if (window.speechSynthesis.getVoices().length) {
        finish();
        return;
      }
      const onChange = () => {
        window.speechSynthesis.removeEventListener("voiceschanged", onChange);
        finish();
      };
      window.speechSynthesis.addEventListener("voiceschanged", onChange);
      window.speechSynthesis.getVoices();
      window.setTimeout(finish, 400);
    });
  }
  return voicesReady;
}

function flushSynth() {
  const synth = window.speechSynthesis;
  synth.cancel();
  if (synth.paused) synth.resume();
}

/** One-time silent warmup. Never chained onto a real speak() — cancel() will drop it. */
export function primeSpeech() {
  if (typeof window === "undefined" || !window.speechSynthesis) return;
  if (primed || priming) return;

  const synth = window.speechSynthesis;
  if (synth.paused) synth.resume();
  if (synth.speaking) {
    primed = true;
    return;
  }

  priming = true;
  const prime = new SpeechSynthesisUtterance("\u00A0");
  prime.volume = 0;
  prime.rate = 2;
  prime.lang = getAccent();
  const done = () => {
    primed = true;
    priming = false;
  };
  prime.onend = done;
  prime.onerror = done;
  try {
    synth.speak(prime);
  } catch {
    done();
  }
}

function installGesturePrime() {
  if (typeof window === "undefined") return;
  const onGesture = () => primeSpeech();
  window.addEventListener("pointerdown", onGesture, { capture: true, once: true, passive: true });
  window.addEventListener("keydown", onGesture, { capture: true, once: true, passive: true });
}

if (typeof window !== "undefined" && window.speechSynthesis) {
  void whenVoicesReady();
  installGesturePrime();
}

const CONTRACTION_EXPAND: [RegExp, string][] = [
  [/\bI'm\b/gi, "I am"],
  [/\bI've\b/gi, "I have"],
  [/\bI'd\b/gi, "I would"],
  [/\bI'll\b/gi, "I will"],
  [/\byou're\b/gi, "you are"],
  [/\byou've\b/gi, "you have"],
  [/\byou'd\b/gi, "you would"],
  [/\byou'll\b/gi, "you will"],
  [/\bhe's\b/gi, "he is"],
  [/\bshe's\b/gi, "she is"],
  [/\bit's\b/gi, "it is"],
  [/\bwe're\b/gi, "we are"],
  [/\bwe've\b/gi, "we have"],
  [/\bwe'd\b/gi, "we would"],
  [/\bwe'll\b/gi, "we will"],
  [/\bthey're\b/gi, "they are"],
  [/\bthey've\b/gi, "they have"],
  [/\bthey'd\b/gi, "they would"],
  [/\bthey'll\b/gi, "they will"],
  [/\bisn't\b/gi, "is not"],
  [/\baren't\b/gi, "are not"],
  [/\bwasn't\b/gi, "was not"],
  [/\bweren't\b/gi, "were not"],
  [/\bdon't\b/gi, "do not"],
  [/\bdoesn't\b/gi, "does not"],
  [/\bdidn't\b/gi, "did not"],
  [/\bcan't\b/gi, "cannot"],
  [/\bwon't\b/gi, "will not"],
  [/\bshouldn't\b/gi, "should not"],
  [/\bwouldn't\b/gi, "would not"],
  [/\bcouldn't\b/gi, "could not"],
  [/\bhaven't\b/gi, "have not"],
  [/\bhasn't\b/gi, "has not"],
  [/\bhadn't\b/gi, "had not"],
  [/\blet's\b/gi, "let us"],
  [/\bthat's\b/gi, "that is"],
  [/\bwhat's\b/gi, "what is"],
  [/\bwhere's\b/gi, "where is"],
  [/\bwho's\b/gi, "who is"],
  [/\bthere's\b/gi, "there is"],
  [/\bhere's\b/gi, "here is"],
];

function expandContractions(text: string): string {
  let out = text;
  for (const [pattern, full] of CONTRACTION_EXPAND) {
    out = out.replace(pattern, full);
  }
  return out;
}

function spokenFingerprint(text: string): string {
  return expandContractions(text)
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

/** "I am a student. / I'm a student." → one phrase (same on the ear). */
export function collapseSpokenVariants(text: string): string {
  const chunks = text
    .split(/\s+\/\s+/)
    .map((part) => part.trim())
    .filter(Boolean);
  if (chunks.length < 2) return text;

  const kept: string[] = [];
  const seen = new Set<string>();
  for (const chunk of chunks) {
    const key = spokenFingerprint(chunk);
    if (!key || seen.has(key)) continue;
    seen.add(key);
    kept.push(chunk);
  }
  return kept.join(". ");
}

function cleanSpeakSegment(part: string): string {
  return part
    .trim()
    .replace(/^(vs\.?|versus)\s+/i, "")
    .replace(/^[\s,.;:!?—–−-]+/, "")
    .replace(/[\s,.;:!?—–−]+$/, "")
    .trim();
}

/** Grammar / CEFR / Russian seed tags in parentheses — speak sentence only. */
const KNOWN_META_PAREN =
  /^(be|to be|being|been|am|is|are|was|were|do|does|did|have|has|had|will|can|must|go|get|got|make|made|take|took|come|came|say|said|open|opened|live|lived|play|played|work|worked|knock|write|written|see|seen|eat|eaten|hear|heard|watch|pay|clear|try|tell|miss|know|finish|leave|solve|heat|boil|cycle|listen|inf|infinitive|gerund|passive|active|v-?ing|v[123]|ed|ing|am\/is\/are|was\/were|do\/does|have\/has|go\/goes|is\/are|a1|a2|b1|b2|c1|c2|present simple|past simple|future simple|present continuous|past continuous|present perfect|past perfect|present perfect continuous|future continuous|future perfect)$/i;

/** Lemma / form hints: (open), (live), (not do), (be / never), (in / on). */
const LEMMA_HINT_PAREN =
  /^(?:not\s+)?[a-z][a-z'-]{0,18}(?:\s*\/\s*(?:not\s+)?[a-z][a-z'-]{0,18}){0,4}(?:\s+[a-z][a-z'-]{0,12}){0,3}$/i;

function isMetaParenthetical(inner: string): boolean {
  const t = inner.trim();
  if (!t || t.length > 40) return false;
  if (/[А-Яа-яЁё]/.test(t)) return true;
  if (KNOWN_META_PAREN.test(t)) return true;
  // Short slash alternatives: am/is/are, do/does/did
  if (/^[a-z][a-z']*(?:\/[a-z][a-z']*){1,4}$/i.test(t) && t.length <= 28) return true;
  // Verb / preposition lemma hints in exercises: (open), (play), (in / on)
  if (LEMMA_HINT_PAREN.test(t) && !/[.!?]$/.test(t) && t.length <= 28) return true;
  // Trailing Title-Case tense / topic labels
  if (
    /^(Present|Past|Future|Present Perfect|Past Perfect|Future Perfect)\b[\w\s-]{0,28}$/i.test(t) &&
    !/[.!?]$/.test(t)
  ) {
    return true;
  }
  return false;
}

/** Strip meta tags like "(be)", "(open)", "(Present Simple)", "(русский хинт)" from spoken text only. */
export function stripMetaParentheticals(text: string): string {
  let out = text.replace(/\s+/g, " ").trim();
  if (!out) return "";

  // Trailing tags (may stack): "I am a student. (be)" / "... ago. (open)" → sentence only
  for (;;) {
    const match = out.match(/^(.*)\s*\(([^)]+)\)\s*$/);
    if (!match || !isMetaParenthetical(match[2])) break;
    out = match[1].trim();
  }

  // Inline known short meta tags only (keep rare legitimate parentheses)
  out = out.replace(/\(([^)]+)\)/g, (full, inner: string) => (isMetaParenthetical(inner) ? " " : full));

  return out.replace(/\s+/g, " ").trim();
}

/** Drop leading Russian / UI instructions before the English example sentence. */
export function stripLeadingInstruction(text: string): string {
  let out = text.replace(/\s+/g, " ").trim();
  if (!out) return "";

  for (let i = 0; i < 4; i += 1) {
    const idx = out.indexOf(":");
    if (idx <= 0 || idx > 140) break;
    const left = out.slice(0, idx).trim();
    const right = out.slice(idx + 1).trim();
    if (!right) break;
    const leftIsInstruction =
      /[А-Яа-яЁё]/.test(left) ||
      /\b(вставьте|выберите|напишите|исправьте|перепишите|добавьте|укажите|соберите|переведите)\b/i.test(left) ||
      /^(choose|select|fill|insert|complete|put|write|use|rewrite|correct|translate|make|form|type)\b/i.test(left);
    if (!leftIsInstruction) break;
    out = right;
  }

  // Leading Cyrillic-only clause before a capitalised English sentence
  const splitEn = out.match(/^([^A-Za-z«"“]*[А-Яа-яЁё][^A-Za-z«"“]*)([A-Za-z«"“].*)$/);
  if (splitEn?.[2] && /[A-Za-z]/.test(splitEn[2])) {
    out = splitEn[2].trim();
  }

  return out.replace(/\s+/g, " ").trim();
}

/** Gaps → short pause for TTS; do not speak underscore runs. */
function blanksForSpeech(text: string): string {
  return text.replace(/_{2,}/g, " … ").replace(/\s+/g, " ").trim();
}

/** Plain English for TTS: drop instructions, meta parens, /ipa/; keep example sentence. */
export function speakableEnglish(text: string): string {
  const prepared = blanksForSpeech(
    stripLeadingInstruction(stripMetaParentheticals(text.replace(/\s+/g, " ").trim())),
  );
  if (!prepared) return "";

  // Prefer the English example when mixed leftovers remain
  const extracted = extractEnglishCore(prepared);
  const raw = extracted || prepared;
  if (!raw) return "";
  if (!/\/[^/\n]+\//.test(raw)) return collapseSpokenVariants(raw);

  const parts = raw.split(/\/[^/\n]+\//);
  const phrases: string[] = [];

  for (let i = 0; i < parts.length; i += 1) {
    const cleaned = cleanSpeakSegment(parts[i]);
    if (cleaned && !SEGMENT_CONNECTOR.test(cleaned)) {
      phrases.push(cleaned);
      continue;
    }

    const restHasEnglish = parts.slice(i + 1).some((part) => {
      const next = cleanSpeakSegment(part);
      return Boolean(next) && !SEGMENT_CONNECTOR.test(next);
    });
    const connector = SEGMENT_CONNECTOR.test(cleanSpeakSegment(parts[i]) || parts[i].trim());
    if (!restHasEnglish && connector && phrases.length) {
      phrases.push(phrases[phrases.length - 1]);
    }
  }

  if (phrases.length) return collapseSpokenVariants(phrases.join(". "));
  return collapseSpokenVariants(raw.replace(/\/[^/\n]+\//g, " ").replace(/\s+/g, " ").trim());
}

function extractEnglishCore(source: string): string | null {
  const quoted = source.match(/[«"“]([^»"”]+)[»"”]/);
  if (quoted?.[1] && /[A-Za-z]/.test(quoted[1])) return quoted[1].trim();

  const latin = source
    .replace(/[А-Яа-яЁё]+/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    // Drop leftover tense labels glued before the sentence
    .replace(/^(?:Present|Past|Future)(?:\s+(?:Simple|Continuous|Perfect))?\s*:?\s*/i, "")
    .trim();
  const words = latin.split(" ").filter((word) => /[A-Za-z…]/.test(word));
  if (words.length >= 2) return latin;
  if (words.length === 1 && words[0].replace(/[^A-Za-z]/g, "").length > 1) return words[0];
  return null;
}

export function speakEnglish(text: string, options?: { rate?: number; accent?: Accent }) {
  const spoken = speakableEnglish(text);
  if (!spoken || typeof window === "undefined" || !window.speechSynthesis) return;

  const generation = ++speakGeneration;
  const synth = window.speechSynthesis;
  flushSynth();

  const utterance = new SpeechSynthesisUtterance(spoken);
  const accent = options?.accent || getAccent();
  utterance.lang = accent;
  utterance.rate = options?.rate ?? getRate();

  const start = () => {
    if (generation !== speakGeneration) return;
    const voice = pickVoice(accent);
    if (voice) utterance.voice = voice;
    flushSynth();
    synth.speak(utterance);
    primed = true;
    priming = false;
  };

  const kick = () => {
    if (generation !== speakGeneration) return;
    // Next macrotask so Chromium cancel() cannot swallow this speak().
    window.setTimeout(start, 0);
  };

  if (synth.getVoices().length) {
    kick();
    return;
  }
  void whenVoicesReady().then(kick);
}

export function extractEnglish(text: string): string | null {
  const spoken = speakableEnglish(text);
  if (!spoken) return null;
  return extractEnglishCore(spoken) || (/[A-Za-z]/.test(spoken) ? spoken : null);
}

export function looksEnglish(text: string): boolean {
  const letters = text.replace(/[^A-Za-zА-Яа-яЁё]/g, "");
  if (!letters) return false;
  const latin = (text.match(/[A-Za-z]/g) || []).length;
  return latin / letters.length >= 0.6;
}
