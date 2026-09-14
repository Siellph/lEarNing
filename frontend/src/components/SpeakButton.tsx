import { Pause, Play, RotateCcw, Volume2 } from "lucide-react";
import { useEffect, useMemo, useRef, useState, type MouseEvent } from "react";
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
  compact: _compact = false,
  showRestart = false,
  className = "",
}: {
  text: string;
  speak?: string;
  /** Accessible name / tooltip when idle (icon-only UI). */
  label?: string;
  /** Override tempo preset; default = user VoiceControls setting. */
  ratePreset?: SpeechRate;
  /** Single-line dialogue role (female = 1st speaker, male = 2nd). */
  voiceGender?: VoiceGender;
  /** Full dialogue: sequential lines with per-speaker voices. */
  dialogueLines?: DialogueSpeakLine[];
  /** @deprecated Icon-only; kept for call-site compatibility. */
  compact?: boolean;
  /** Second control: stop and play the same unit from the beginning. */
  showRestart?: boolean;
  className?: string;
}) {
  const [ready, setReady] = useState(false);
  const [playback, setPlayback] = useState<SpeakPlaybackState>("idle");
  const mainRef = useRef<HTMLButtonElement>(null);
  const restartRef = useRef<HTMLButtonElement>(null);
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

  // Drop mouse focus highlight when this clip finishes (or another clip takes over).
  useEffect(() => {
    if (playback !== "idle") return;
    mainRef.current?.blur();
    restartRef.current?.blur();
  }, [playback]);

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
  const idleName = label || "Прослушать";
  const aria = isSpeaking ? `Пауза: ${spoken}` : isPaused ? `Продолжить: ${spoken}` : `${idleName}: ${spoken}`;
  const title = isSpeaking ? "Пауза" : isPaused ? "Продолжить" : idleName;
  const Icon = isSpeaking ? Pause : isPaused ? Play : Volume2;

  const speakOpts = { ratePreset: ratePreset ?? getRatePreset() };
  const btnClass = `speak-btn ${isSpeaking ? "speak-btn--speaking" : ""} ${isPaused ? "speak-btn--paused" : ""}`;

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
      ref={mainRef}
      type="button"
      className={`${btnClass} ${extraClass}`.trim()}
      aria-label={aria}
      aria-pressed={isSpeaking || isPaused}
      title={title}
      disabled={!ready}
      onPointerDown={() => primeSpeech()}
      onClick={onToggle}
    >
      <Icon size={16} aria-hidden />
    </button>
  );

  if (!showRestart) {
    return mainButton(className);
  }

  return (
    <span className={`speak-btn-group ${className}`.trim()}>
      {mainButton()}
      <button
        ref={restartRef}
        type="button"
        className="speak-btn speak-btn--restart"
        aria-label={`Сначала: ${spoken}`}
        title="Сначала"
        disabled={!ready}
        onPointerDown={() => primeSpeech()}
        onClick={onRestart}
      >
        <RotateCcw size={16} aria-hidden />
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
  );
}

export function VoiceControls({ className = "" }: { className?: string }) {
  return (
    <div className={`flex flex-col gap-3 ${className}`}>
      <div className="flex flex-col gap-1.5">
        <span className="text-xs font-semibold uppercase tracking-[0.12em] text-ink-soft">Акцент</span>
        <AccentSwitch />
      </div>
      <div className="flex flex-col gap-1.5">
        <span className="text-xs font-semibold uppercase tracking-[0.12em] text-ink-soft">Темп</span>
        <RateSwitch />
      </div>
    </div>
  );
}

/** Global header control: speaker icon → accent + rate dropdown. */
export function VoiceSettingsMenu({ className = "" }: { className?: string }) {
  const [open, setOpen] = useState(false);
  const rootRef = useRef<HTMLDivElement>(null);
  const btnRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (!open) return;
    const onPointer = (event: globalThis.MouseEvent) => {
      if (!rootRef.current?.contains(event.target as Node)) setOpen(false);
    };
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setOpen(false);
        btnRef.current?.blur();
      }
    };
    document.addEventListener("mousedown", onPointer);
    window.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("mousedown", onPointer);
      window.removeEventListener("keydown", onKey);
    };
  }, [open]);

  return (
    <div ref={rootRef} className={`relative shrink-0 ${className}`}>
      <button
        ref={btnRef}
        type="button"
        className={`inline-flex size-9 items-center justify-center rounded-full border border-line/80 bg-card text-ink shadow-sm transition-colors hover:border-terra hover:bg-paper-2 hover:text-terra ${
          open ? "border-terra text-terra" : ""
        }`}
        aria-label="Настройки озвучки"
        aria-expanded={open}
        aria-haspopup="dialog"
        title="Озвучка"
        onClick={() => setOpen((v) => !v)}
      >
        <Volume2 size={18} aria-hidden />
      </button>
      {open ? (
        <div
          role="dialog"
          aria-label="Настройки озвучки"
          className="absolute right-0 top-[calc(100%+0.4rem)] z-50 w-[min(17.5rem,calc(100vw-1.5rem))] rounded-2xl border border-line/80 bg-card p-4 shadow-[0_12px_40px_rgba(18,32,51,0.12)]"
        >
          <p className="mb-3 text-xs font-semibold uppercase tracking-[0.12em] text-ink-soft">Озвучка</p>
          <VoiceControls />
        </div>
      ) : null}
    </div>
  );
}
