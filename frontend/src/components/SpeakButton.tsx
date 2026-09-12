import { Volume2 } from "lucide-react";
import { useEffect, useState } from "react";
import { onConsentChange } from "../lib/consent";
import {
  speakEnglish,
  speakableEnglish,
  primeSpeech,
  type Accent,
  type SpeechRate,
  getAccent,
  setAccent,
  getRate,
  getRatePreset,
  setRatePreset,
} from "../lib/speech";

export function SpeakButton({
  text,
  speak,
  label,
  rate,
  className = "",
}: {
  text: string;
  speak?: string;
  label?: string;
  rate?: number;
  className?: string;
}) {
  const [ready, setReady] = useState(false);
  const spoken = (speak ?? speakableEnglish(text)).trim();

  useEffect(() => {
    if (!window.speechSynthesis) return;
    const unlock = () => setReady(true);
    unlock();
    window.speechSynthesis.addEventListener("voiceschanged", unlock);
    return () => window.speechSynthesis.removeEventListener("voiceschanged", unlock);
  }, []);

  if (!spoken) return null;

  return (
    <button
      type="button"
      className={`speak-btn ${className}`}
      aria-label={label || `Прослушать: ${spoken}`}
      title={label || "Прослушать"}
      disabled={!ready}
      onPointerDown={() => primeSpeech()}
      onClick={(event) => {
        event.preventDefault();
        event.stopPropagation();
        speakEnglish(spoken, { rate: rate ?? getRate() });
      }}
    >
      <Volume2 size={16} />
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
