import { Pause, Play, RotateCcw, Volume2 } from "lucide-react";
import { useEffect, useMemo, useState, type MouseEvent } from "react";
import { onConsentChange } from "../lib/consent";
import {
  toggleSpeakEnglish,
  toggleSpeakDialogue,
  restartSpeakEnglish,
  restartSpeakDialogue,
  speakableEnglish,
  primeSpeech,
  type Accent,
  type SpeechRate,
  type SpeakPlaybackState,
  type VoiceGender,
  type DialogueSpeakLine,
  getAccent,
  setAccent,
  getRatePreset,
  setRatePreset,
  getSpeakPlaybackState,
  getActiveSpokenText,
  onSpeakPlaybackChange,
  stopSpeech,
} from "../lib/speech";

export function SpeakButton({
  text,
  speak,
  label,
  ratePreset,
  voiceGender,
  dialogueLines,
  compact = false,
  showRestart = false,
  className = "",
}: {
  text: string;
  speak?: string;
  label?: string;
  /** Override tempo preset; default = user VoiceControls setting. */
  ratePreset?: SpeechRate;
  /** Single-line dialogue role (female = 1st speaker, male = 2nd). */
  voiceGender?: VoiceGender;
  /** Full dialogue: sequential lines with per-speaker voices. */
  dialogueLines?: DialogueSpeakLine[];
  /** Hide label text on small screens (icon-only; aria-label kept). */
  compact?: boolean;
  /** Second control: stop and play the same unit from the beginning. */
  showRestart?: boolean;
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
    setReady(true);
    if (!window.speechSynthesis) return;
    const unlock = () => setReady(true);
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

  // If this control started playback, silence it when the control leaves the tree
  // (in-page remounts / quiz step changes). Route changes are handled globally.
  useEffect(() => {
    return () => {
      if (getActiveSpokenText() === spoken) stopSpeech();
    };
  }, [spoken]);

  if (!spoken) return null;

  const isSpeaking = playback === "speaking";
  const isPaused = playback === "paused";
  const aria =
    isSpeaking ? `Пауза: ${spoken}` : isPaused ? `Продолжить: ${spoken}` : label || `Прослушать: ${spoken}`;
  const title = isSpeaking ? "Пауза" : isPaused ? "Продолжить" : label || "Прослушать";
  const Icon = isSpeaking ? Pause : isPaused ? Play : Volume2;

  const speakOpts = { ratePreset: ratePreset ?? getRatePreset() };
  const btnClass = `speak-btn ${compact ? "speak-btn--compact" : ""} ${isSpeaking ? "speak-btn--speaking" : ""} ${isPaused ? "speak-btn--paused" : ""}`;

  const onToggle = (event: MouseEvent) => {
    event.preventDefault();
    event.stopPropagation();
    if (dialogueLines?.length) {
      toggleSpeakDialogue(dialogueLines, speakOpts);
    } else {
      toggleSpeakEnglish(spoken, { ...speakOpts, voiceGender });
    }
  };

  const onRestart = (event: MouseEvent) => {
    event.preventDefault();
    event.stopPropagation();
    if (dialogueLines?.length) {
      restartSpeakDialogue(dialogueLines, speakOpts);
    } else {
      restartSpeakEnglish(spoken, { ...speakOpts, voiceGender });
    }
  };

  const mainButton = (extraClass = "") => (
    <button
      type="button"
      className={`${btnClass} ${extraClass}`.trim()}
      aria-label={aria}
      aria-pressed={isSpeaking || isPaused}
      title={title}
      disabled={!ready}
      onPointerDown={() => primeSpeech()}
      onClick={onToggle}
    >
      <Icon size={16} />
      {label ? <span className={compact ? "speak-btn__label" : undefined}>{label}</span> : null}
    </button>
  );

  if (!showRestart) {
    return mainButton(className);
  }

  return (
    <span className={`speak-btn-group ${className}`.trim()}>
      {mainButton()}
      <button
        type="button"
        className={`speak-btn speak-btn--restart ${compact ? "speak-btn--compact" : ""}`}
        aria-label={`Сначала: ${spoken}`}
        title="Сначала"
        disabled={!ready}
        onPointerDown={() => primeSpeech()}
        onClick={onRestart}
      >
        <RotateCcw size={16} />
        <span className={compact ? "speak-btn__label" : undefined}>Сначала</span>
      </button>
    </span>
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
