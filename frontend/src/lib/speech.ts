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

export type VoiceGender = "female" | "male";

/** Heuristic name cues — Web Speech has no reliable gender field on most engines. */
const FEMALE_VOICE_HINT =
  /\b(samantha|victoria|karen|moira|fiona|tessa|veena|zira|hazel|susan|allison|ava|serena|kate|kathy|emily|martha|linda|heather|nancy|salli|joanna|ivy|kimberly|kendra|amy|emma|olivia|michelle|jenny|aria|sonia|lesley|lisa|laura|helen|catherine|nicky|princess|google uk english female|google us english female|microsoft.*(zira|hazel|susan|aria|jenny)|#female|female[_-]?\d*|female)\b/i;
const MALE_VOICE_HINT =
  /\b(daniel|alex|david|fred|tom|james|oliver|mark|ravi|arthur|aaron|bruce|gordon|lee|nathan|thomas|diego|jorge|guy|ryan|brian|matthew|justin|kevin|eric|paul|richard|george|ralph|albert|ed|google uk english male|google us english male|microsoft.*(david|mark|guy|ryan|brian|george)|#male|male[_-]?\d*|male)\b/i;

/** Android TTS voice-name fragments (often appear in voiceURI / name). */
const ANDROID_FEMALE_VOICE =
  /(?:#female|female[_-]?\d+)|en-[a-z]{2}-x-(?:sfg|tpc|tpf|cfg|dfg|efg|hfg|ifg|jfg|lfg|nfg|ofg|rfg)(?:-|[.#]|$)/i;
const ANDROID_MALE_VOICE =
  /(?:#male|male[_-]?\d+)|en-[a-z]{2}-x-(?:iom|iol|tpd|aub|aud|gbb|gbd|rjs|end|ene)(?:-|[.#]|$)/i;

/** Slight pitch split when only one ENG voice is available (esp. Chrome Android). */
const PITCH_FEMALE_FALLBACK = 1.12;
const PITCH_MALE_FALLBACK = 0.88;

type VoiceWithGender = SpeechSynthesisVoice & { gender?: string };

function normalizeVoiceLang(lang: string): string {
  return lang.replace(/_/g, "-").toLowerCase();
}

function isEnglishVoice(voice: SpeechSynthesisVoice): boolean {
  return normalizeVoiceLang(voice.lang).startsWith("en");
}

function voiceGenderHint(voice: SpeechSynthesisVoice): VoiceGender | null {
  const tagged = (voice as VoiceWithGender).gender?.toLowerCase();
  if (tagged === "female" || tagged === "male") return tagged;

  const label = `${voice.name} ${voice.voiceURI}`;
  const female =
    FEMALE_VOICE_HINT.test(label) || ANDROID_FEMALE_VOICE.test(label);
  const male = MALE_VOICE_HINT.test(label) || ANDROID_MALE_VOICE.test(label);
  if (female && !male) return "female";
  if (male && !female) return "male";
  return null;
}

function voiceMatchesAccent(voice: SpeechSynthesisVoice, accent: Accent): boolean {
  const lang = normalizeVoiceLang(voice.lang);
  const name = voice.name;
  if (accent === "en-GB") {
    return (
      lang.includes("gb") ||
      lang.includes("uk") ||
      /british|uk english|en-gb/i.test(name)
    );
  }
  return lang.includes("us") || /american|us english|en-us/i.test(name);
}

function scoreGenderedVoice(
  voice: SpeechSynthesisVoice,
  gender: VoiceGender,
  accent: Accent,
): number {
  if (!isEnglishVoice(voice)) return -1;
  let score = 10;
  if (voiceMatchesAccent(voice, accent)) score += 50;
  const hinted = voiceGenderHint(voice);
  if (hinted === gender) score += 100;
  else if (hinted && hinted !== gender) score -= 80;
  if (voice.localService) score += 5;
  return score;
}

function pickVoice(lang: Accent): SpeechSynthesisVoice | undefined {
  const voices = window.speechSynthesis.getVoices();
  const exact = voices.find((voice) => voice.lang === lang || voice.lang.replace("_", "-") === lang);
  if (exact) return exact;
  const prefix = voices.find((voice) => voice.lang.startsWith(lang.slice(0, 2)));
  return prefix;
}

/**
 * Pick an EN voice for a dialogue gender role.
 * Prefers name / voiceURI heuristics + optional `voice.gender` + user accent (UK/US).
 * If only one EN voice exists, returns it (caller may apply pitch fallback).
 */
export function pickVoiceForGender(
  gender: VoiceGender,
  accent: Accent = getAccent(),
): SpeechSynthesisVoice | undefined {
  const english = window.speechSynthesis.getVoices().filter(isEnglishVoice);
  if (!english.length) return pickVoice(accent);
  if (english.length === 1) return english[0];

  let best: SpeechSynthesisVoice | undefined;
  let bestScore = -Infinity;
  for (const voice of english) {
    const score = scoreGenderedVoice(voice, gender, accent);
    if (score > bestScore) {
      bestScore = score;
      best = voice;
    }
  }
  return best ?? english[0];
}

/**
 * Female + male pair for a dialogue. Tries to keep them distinct when ≥2 EN voices exist.
 * Mapping convention: first unique speaker → female, second → male (then alternate).
 */
export function pickDialogueVoices(accent: Accent = getAccent()): {
  female: SpeechSynthesisVoice | undefined;
  male: SpeechSynthesisVoice | undefined;
} {
  const female = pickVoiceForGender("female", accent);
  let male = pickVoiceForGender("male", accent);
  if (female && male && female.voiceURI === male.voiceURI) {
    const english = window.speechSynthesis.getVoices().filter(isEnglishVoice);
    const other =
      english
        .filter((voice) => voice.voiceURI !== female.voiceURI)
        .sort((a, b) => scoreGenderedVoice(b, "male", accent) - scoreGenderedVoice(a, "male", accent))[0] ??
      undefined;
    if (other) male = other;
  }
  return { female, male };
}

/** True when female/male resolve to the same engine voice — use pitch to differentiate. */
export function needsGenderPitchFallback(accent: Accent = getAccent()): boolean {
  const { female, male } = pickDialogueVoices(accent);
  if (!female || !male) return true;
  return female.voiceURI === male.voiceURI;
}

export function pitchForGender(
  gender: VoiceGender,
  useFallback: boolean,
): number {
  if (!useFallback) return 1;
  return gender === "female" ? PITCH_FEMALE_FALLBACK : PITCH_MALE_FALLBACK;
}

/** First unique speaker → female, second → male, then alternate. Stable within one dialogue. */
export function mapSpeakersToGender(speakers: Iterable<string>): Map<string, VoiceGender> {
  const map = new Map<string, VoiceGender>();
  for (const raw of speakers) {
    const name = raw.trim();
    if (!name || map.has(name)) continue;
    map.set(name, map.size % 2 === 0 ? "female" : "male");
  }
  return map;
}

export type DialogueSpeakLine = {
  text: string;
  voiceGender: VoiceGender;
};

function dialogueFingerprint(spokenLines: string[]): string {
  return spokenLines.join("\n");
}

const SEGMENT_CONNECTOR = /^(vs\.?|versus|v\.)$/i;

let voicesReady: Promise<void> | null = null;
let speakGeneration = 0;
let primed = false;
let priming = false;

export type SpeakPlaybackState = "idle" | "speaking" | "paused";

let playbackState: SpeakPlaybackState = "idle";
let activeSpokenText: string | null = null;
const playbackListeners = new Set<() => void>();

function notifyPlayback() {
  playbackListeners.forEach((listener) => listener());
}

function setPlayback(state: SpeakPlaybackState, spoken: string | null = activeSpokenText) {
  playbackState = state;
  activeSpokenText = state === "idle" ? null : spoken;
  notifyPlayback();
}

export function getSpeakPlaybackState(): SpeakPlaybackState {
  return playbackState;
}

export function getActiveSpokenText(): string | null {
  return activeSpokenText;
}

export function onSpeakPlaybackChange(listener: () => void): () => void {
  playbackListeners.add(listener);
  return () => playbackListeners.delete(listener);
}

/**
 * Safari / iOS WebKit: pause()/resume() often no-op while speaking stays true.
 * Prefer cancel so a second click can interrupt; third click plays from the start.
 */
function speechPauseUnreliable(): boolean {
  if (typeof navigator === "undefined") return false;
  const ua = navigator.userAgent;
  return /iP(ad|hone|od)/.test(ua) || (/Safari/.test(ua) && !/Chrome|CriOS|Chromium|Edg|Android/.test(ua));
}

function flushSynth() {
  const synth = window.speechSynthesis;
  synth.cancel();
  // Chromium can stick in paused after cancel; clear it so the next speak() runs.
  if (synth.paused) synth.resume();
}

export function stopSpeech() {
  if (typeof window === "undefined" || !window.speechSynthesis) return;
  speakGeneration += 1;
  flushSynth();
  setPlayback("idle");
}

export function pauseSpeech() {
  if (typeof window === "undefined" || !window.speechSynthesis) return;
  const synth = window.speechSynthesis;

  // Pending kick/start: speaking flag may still be false — cancel the queued utterance.
  if (playbackState === "speaking" && !synth.speaking) {
    stopSpeech();
    return;
  }
  if (!synth.speaking || synth.paused) return;

  if (speechPauseUnreliable()) {
    stopSpeech();
    return;
  }

  synth.pause();
  if (synth.paused) {
    setPlayback("paused");
    return;
  }
  // Pause did not take (some WebKit builds) — interrupt via cancel instead.
  stopSpeech();
}

export function resumeSpeech() {
  if (typeof window === "undefined" || !window.speechSynthesis) return;
  const synth = window.speechSynthesis;
  if (!synth.paused && playbackState !== "paused") return;
  synth.resume();
  setPlayback("speaking");
}

export type SpeakOptions = {
  rate?: number;
  accent?: Accent;
  /** Dialogue role voice; ignored when omitted (uses default accent voice). */
  voiceGender?: VoiceGender;
};

/** Speak, or pause/resume the same active phrase (SpeakButton toggle). */
export function toggleSpeakEnglish(text: string, options?: SpeakOptions) {
  const spoken = speakableEnglish(text);
  if (!spoken || typeof window === "undefined" || !window.speechSynthesis) return;

  const synth = window.speechSynthesis;
  const same = activeSpokenText === spoken;

  if (same && (playbackState === "speaking" || (synth.speaking && !synth.paused))) {
    pauseSpeech();
    return;
  }
  if (same && (playbackState === "paused" || synth.paused)) {
    resumeSpeech();
    return;
  }

  speakEnglish(text, options);
}

/** Speak a multi-speaker script, or pause/resume the same active dialogue. */
export function toggleSpeakDialogue(lines: DialogueSpeakLine[], options?: SpeakOptions) {
  const prepared = lines
    .map((line) => ({ spoken: speakableEnglish(line.text), voiceGender: line.voiceGender }))
    .filter((line) => line.spoken);
  if (!prepared.length || typeof window === "undefined" || !window.speechSynthesis) return;

  const fingerprint = dialogueFingerprint(prepared.map((line) => line.spoken));
  const synth = window.speechSynthesis;
  const same = activeSpokenText === fingerprint;

  if (same && (playbackState === "speaking" || (synth.speaking && !synth.paused))) {
    pauseSpeech();
    return;
  }
  if (same && (playbackState === "paused" || synth.paused)) {
    resumeSpeech();
    return;
  }

  speakDialogue(lines, options);
}

function whenVoicesReady(): Promise<void> {
  if (typeof window === "undefined" || !window.speechSynthesis) return Promise.resolve();
  if (!voicesReady) {
    voicesReady = new Promise((resolve) => {
      let settled = false;
      const finish = () => {
        if (settled) return;
        settled = true;
        window.speechSynthesis.removeEventListener("voiceschanged", onChange);
        resolve();
      };
      const onChange = () => {
        // Chrome Android often fires voiceschanged after an empty/stub list.
        if (window.speechSynthesis.getVoices().length) finish();
      };
      window.speechSynthesis.addEventListener("voiceschanged", onChange);
      // Kick load; may be empty until voiceschanged.
      window.speechSynthesis.getVoices();
      if (window.speechSynthesis.getVoices().length) {
        // Still give voiceschanged a moment — Android may replace the list.
        window.setTimeout(() => {
          if (window.speechSynthesis.getVoices().length) finish();
        }, 50);
      }
      window.setTimeout(finish, 1500);
    });
  }
  return voicesReady;
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

const RU_TASK_VERB =
  /\b(вставьте|выберите|напишите|исправьте|перепишите|добавьте|укажите|соберите|переведите|сопоставьте|отметьте|заполните)\b/i;
const EN_TASK_VERB =
  /^(choose|select|fill|insert|complete|put|write|use|rewrite|correct|translate|make|form|type)\b/i;
const GRAMMAR_LABEL_LEAD =
  /^(?:Present|Past|Future|First|Second|Third|Zero)\b[\w\s/-]{0,40}$/i;

function segmentIsInstruction(segment: string): boolean {
  const t = segment.trim();
  if (!t) return false;
  // Long Latin-only chunks are not task prefixes; long RU lead-ins still count.
  if (t.length > 140 && !/[А-Яа-яЁё]/.test(t)) return false;
  if (/[А-Яа-яЁё]/.test(t)) return true;
  if (RU_TASK_VERB.test(t)) return true;
  if (EN_TASK_VERB.test(t)) return true;
  if (GRAMMAR_LABEL_LEAD.test(t)) return true;
  return false;
}

function rightLooksLikeExercise(right: string): boolean {
  const t = right.trimStart();
  if (!t) return false;
  if (/^(?:_{2,}|[A-Za-z«"“'‘])/.test(t)) return true;
  return /[A-Za-z]/.test(t) && !/^[А-Яа-яЁё]/.test(t);
}

/**
 * Index where the learner-facing English exercise begins.
 * Skips Russian / task prefixes like `Вставьте форму to be: …`.
 */
export function findExerciseStart(text: string): number {
  if (!text) return 0;

  let best = 0;
  let from = 0;
  let prevColon = -1;

  while (from < text.length) {
    const idx = text.indexOf(":", from);
    if (idx < 0) break;
    const segment = text.slice(prevColon + 1, idx);
    const after = text.slice(idx + 1);
    const right = after.replace(/^\s*/, "");
    if (segmentIsInstruction(segment) && rightLooksLikeExercise(right)) {
      best = idx + 1 + (after.length - right.length);
    }
    prevColon = idx;
    from = idx + 1;
  }

  if (best > 0) return best;

  // Leading Cyrillic-only clause before a capitalised English sentence
  const splitEn = text.match(/^([^A-Za-z«"“]*[А-Яа-яЁё][^A-Za-z«"“]*)([A-Za-z«"“].*)$/);
  if (splitEn?.[1] && splitEn[2] && /[A-Za-z]/.test(splitEn[2])) {
    return splitEn[1].length;
  }

  return 0;
}

/** Drop leading Russian / UI instructions before the English example sentence. */
export function stripLeadingInstruction(text: string): string {
  const out = text.replace(/\s+/g, " ").trim();
  if (!out) return "";
  return out.slice(findExerciseStart(out)).trim();
}

/**
 * Display split aligned with TTS (`speakableEnglish` / `extractEnglish`):
 * RU/task prefix and meta hints stay plain; only `english` is spoken.
 */
export function splitSpeakablePrompt(text: string): {
  prefix: string;
  english: string;
  suffix: string;
} {
  if (!text) return { prefix: "", english: "", suffix: "" };
  const start = findExerciseStart(text);
  const prefix = text.slice(0, start);
  let english = text.slice(start);
  let suffix = "";

  // Same trailing peel as stripMetaParentheticals, without collapsing display spaces.
  for (;;) {
    const match = english.match(/^(.*)(\s*\(([^)]+)\))\s*$/);
    if (!match || !isMetaParenthetical(match[3])) break;
    suffix = match[2] + suffix;
    english = match[1];
  }

  return { prefix, english, suffix };
}

/** True when `(…)` is a grammar/lemma hint — not learner English to gloss or speak. */
export function isMetaParenHint(inner: string): boolean {
  return isMetaParenthetical(inner);
}

/** Gaps → short pause for TTS; do not speak underscore runs. */
function blanksForSpeech(text: string): string {
  return text.replace(/_{2,}/g, " … ").replace(/\s+/g, " ").trim();
}

/**
 * Web Speech API does not reliably parse SSML. Engines (esp. iOS/Safari) often
 * read tags like `<speak>` / `<prosody rate="88%">` aloud as plain English.
 * Never wrap utterance text in SSML — set tempo via `utterance.rate` only.
 */
export function stripSsmlMarkup(text: string): string {
  if (!text) return "";
  return text
    .replace(/<\/?speak\b[^>]*>/gi, " ")
    .replace(/<\/?prosody\b[^>]*>/gi, " ")
    .replace(
      /<\/?(?:break|emphasis|say-as|phoneme|sub|p|s|voice|audio|mark|desc|w|lang|token|bookmark)\b[^>]*>/gi,
      " ",
    )
    .replace(/\s+/g, " ")
    .trim();
}

/** Plain English for TTS: drop instructions, meta parens, /ipa/; keep example sentence. */
export function speakableEnglish(text: string): string {
  const prepared = blanksForSpeech(
    stripLeadingInstruction(
      stripMetaParentheticals(stripSsmlMarkup(text.replace(/\s+/g, " ").trim())),
    ),
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

export function speakEnglish(text: string, options?: SpeakOptions) {
  // Plain text only — never SSML. Rate/accent are utterance properties.
  const spoken = speakableEnglish(text);
  if (!spoken || typeof window === "undefined" || !window.speechSynthesis) return;

  const generation = ++speakGeneration;
  const synth = window.speechSynthesis;
  flushSynth();
  setPlayback("speaking", spoken);

  const utterance = new SpeechSynthesisUtterance(spoken);
  const accent = options?.accent || getAccent();
  utterance.lang = accent;
  utterance.rate = options?.rate ?? getRate();

  const clearIfCurrent = () => {
    if (generation !== speakGeneration) return;
    setPlayback("idle");
  };
  utterance.onend = clearIfCurrent;
  utterance.onerror = clearIfCurrent;

  const start = () => {
    if (generation !== speakGeneration) return;
    const voice = options?.voiceGender
      ? pickVoiceForGender(options.voiceGender, accent)
      : pickVoice(accent);
    if (voice) utterance.voice = voice;
    if (options?.voiceGender) {
      utterance.pitch = pitchForGender(
        options.voiceGender,
        needsGenderPitchFallback(accent),
      );
    }
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

  // Always wait for voiceschanged when possible — Android often lists voices late.
  void whenVoicesReady().then(kick);
}

/**
 * Speak dialogue lines in order; each line uses its speaker gender voice.
 * Sequential (onend → next) rather than bulk-queue — more reliable on iOS/Safari.
 */
export function speakDialogue(lines: DialogueSpeakLine[], options?: SpeakOptions) {
  const prepared = lines
    .map((line) => ({ spoken: speakableEnglish(line.text), voiceGender: line.voiceGender }))
    .filter((line) => line.spoken);
  if (!prepared.length || typeof window === "undefined" || !window.speechSynthesis) return;

  const fingerprint = dialogueFingerprint(prepared.map((line) => line.spoken));
  const generation = ++speakGeneration;
  const synth = window.speechSynthesis;
  flushSynth();
  setPlayback("speaking", fingerprint);

  const accent = options?.accent || getAccent();
  const rate = options?.rate ?? getRate();

  const start = () => {
    if (generation !== speakGeneration) return;
    const voices = pickDialogueVoices(accent);
    const pitchFallback = needsGenderPitchFallback(accent);

    const speakAt = (index: number) => {
      if (generation !== speakGeneration) return;
      if (index >= prepared.length) {
        setPlayback("idle");
        return;
      }

      const line = prepared[index];
      const utterance = new SpeechSynthesisUtterance(line.spoken);
      utterance.lang = accent;
      utterance.rate = rate;
      const voice = line.voiceGender === "male" ? voices.male : voices.female;
      if (voice) utterance.voice = voice;
      utterance.pitch = pitchForGender(line.voiceGender, pitchFallback);

      utterance.onend = () => speakAt(index + 1);
      utterance.onerror = () => {
        if (generation !== speakGeneration) return;
        setPlayback("idle");
      };

      if (index === 0) flushSynth();
      synth.speak(utterance);
      primed = true;
      priming = false;
    };

    speakAt(0);
  };

  const kick = () => {
    if (generation !== speakGeneration) return;
    window.setTimeout(start, 0);
  };

  void whenVoicesReady().then(kick);
}

/** Irregular verbs: speak V1, V2, V3 with pauses; expand slash alts; no gloss. */
export function verbFormsSpeakText(card: {
  primary_text: string;
  secondary_text?: string;
  tertiary_text?: string;
}): string {
  const fields = [
    card.primary_text.split("→")[0].trim(),
    (card.secondary_text || "").trim(),
    (card.tertiary_text || "").trim(),
  ];
  const parts: string[] = [];
  for (const field of fields) {
    if (!field) continue;
    for (const piece of field.split("/")) {
      const word = piece.trim();
      if (word) parts.push(word);
    }
  }
  return parts.join(". ");
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
