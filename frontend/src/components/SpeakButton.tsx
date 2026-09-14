import { Pause, Play, Volume2 } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { onConsentChange } from "../lib/consent";
import {
  toggleSpeakEnglish,
  toggleSpeakDialogue,
  speakableEnglish,
  primeSpeech,
  type Accent,
  type SpeechRate,
  type SpeakPlaybackState,
  type VoiceGender,
  type DialogueSpeakLine,
  getAccent,
  setAccent,
  getRate,
  getRatePreset,
  setRatePreset,
  getSpeakPlaybackState,
  getActiveSpokenText,
  onSpeakPlaybackChange,
} from "../lib/speech";

export function SpeakButton({
  text,
  speak,
  label,
  rate,
  voiceGender,
  dialogueLines,
  className = "",
}: {
  text: string;
  speak?: string;
  label?: string;
  rate?: number;
  /** Single-line dialogue role (female = 1st speaker, male = 2nd). */
  voiceGender?: VoiceGender;
  /** Full dialogue: sequential lines with per-speaker voices. */
  dialogueLines?: DialogueSpeakLine[];
  className?: string;
}) {
  const [ready, setReady] = useState(false);
  const [playback, setPlayback] = useState<SpeakPlaybackState>("idle");
  const spoken = useMemo(() => {
    if (dialogueLines?.length) {
      return dialogueLines
        .map((line) => speakableEnglish(line.text))
        .filter(Boolean)
        .join("\n");
    }
    return (speak ?? speakableEnglish(text)).trim();
  }, [dialogueLines, speak, text]);

  useEffect(() => {
    if (!window.speechSynthesis) return;
    const unlock = () => setReady(true);
    unlock();
    window.speechSynthesis.addEventListener("voiceschanged", unlock);
    return () => window.speechSynthesis.removeEventListener("voiceschanged", unlock);
  }, []);

  useEffect(() => {
    const sync = () => {
      const active = getActiveSpokenText() === spoken;
      setPlayback(active ? getSpeakPlaybackState() : "idle");
    };
    sync();
    return onSpeakPlaybackChange(sync);
  }, [spoken]);

  if (!spoken) return null;

  const isSpeaking = playback === "speaking";
  const isPaused = playback === "paused";
  const aria =
    isSpeaking ? `Пауза: ${spoken}` : isPaused ? `Продолжить: ${spoken}` : label || `Прослушать: ${spoken}`;
  const title = isSpeaking ? "Пауза" : isPaused ? "Продолжить" : label || "Прослушать";
  const Icon = isSpeaking ? Pause : isPaused ? Play : Volume2;

  return (
    <button
      type="button"
      className={`speak-btn ${isSpeaking ? "speak-btn--speaking" : ""} ${isPaused ? "speak-btn--paused" : ""} ${className}`}
      aria-label={aria}
      aria-pressed={isSpeaking || isPaused}
      title={title}
      disabled={!ready}
      onPointerDown={() => primeSpeech()}
      onClick={(event) => {
        event.preventDefault();
        event.stopPropagation();
        const opts = { rate: rate ?? getRate() };
        if (dialogueLines?.length) {
          toggleSpeakDialogue(dialogueLines, opts);
        } else {
          toggleSpeakEnglish(spoken, { ...opts, voiceGender });
        }
      }}
    >
      <Icon size={16} />
      {label ? <span>{label}</span> : null}
    </button>
  );
}

export function AccentSwitch() {
  const [accent, setValue] = useState<Accent>("en-GB");

  useEffect(() => {
    const sync = () => setValue(getAccent());
    sync();
    return onConsentChange(sync);
  }, []);

  return (
    <div className="flex rounded-full bg-paper-2 p-1 text-xs font-semibold">
      {(
        [
          ["en-GB", "UK"],
          ["en-US", "US"],
        ] as const
      ).map(([code, name]) => (
        <button
          key={code}
          type="button"
          className={`rounded-full px-3 py-1 ${accent === code ? "bg-card text-terra" : "text-ink-soft"}`}
          onClick={() => {
            setAccent(code);
            setValue(code);
          }}
        >
          {name}
        </button>
      ))}
    </div>
  );
}

const RATE_LABELS: { value: SpeechRate; label: string; title: string }[] = [
  { value: "slow", label: "медленно", title: "Медленнее обычного (0.65×)" },
  { value: "normal", label: "обычно", title: "Обычный темп" },
  { value: "fast", label: "быстро", title: "Быстрее обычного (1.15×)" },
];

export function RateSwitch() {
  const [rate, setValue] = useState<SpeechRate>("normal");

  useEffect(() => {
    const sync = () => setValue(getRatePreset());
    sync();
    return onConsentChange(sync);
  }, []);

  return (
    <div className="flex items-center gap-2">
      <span className="text-xs text-ink-soft">Темп</span>
      <div className="flex rounded-full bg-paper-2 p-1 text-xs font-semibold">
        {RATE_LABELS.map((item) => (
          <button
            key={item.value}
            type="button"
            title={item.title}
            className={`rounded-full px-3 py-1 ${rate === item.value ? "bg-card text-terra" : "text-ink-soft"}`}
            onClick={() => {
              setRatePreset(item.value);
              setValue(item.value);
            }}
          >
            {item.label}
          </button>
        ))}
      </div>
    </div>
  );
}

export function VoiceControls({ className = "" }: { className?: string }) {
  return (
    <div className={`flex flex-wrap items-center gap-3 ${className}`}>
      <span className="text-xs font-semibold uppercase tracking-[0.12em] text-ink-soft">Озвучка</span>
      <AccentSwitch />
      <RateSwitch />
    </div>
  );
}
