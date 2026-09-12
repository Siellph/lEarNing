export const CONSENT_KEY = "learning_cookie_consent";
export const ACCENT_KEY = "lumina_accent";
export const RATE_KEY = "lumina_speech_rate";

export type ConsentChoice = "accepted" | "rejected";

const listeners = new Set<() => void>();

export function getConsent(): ConsentChoice | null {
  try {
    const value = localStorage.getItem(CONSENT_KEY);
    if (value === "accepted" || value === "rejected") return value;
  } catch {
    /* private mode */
  }
  return null;
}

export function canPersistPrefs(): boolean {
  return getConsent() === "accepted";
}

export function onConsentChange(listener: () => void) {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

export function setConsent(choice: ConsentChoice) {
  localStorage.setItem(CONSENT_KEY, choice);
  if (choice === "rejected") {
    localStorage.removeItem(ACCENT_KEY);
    localStorage.removeItem(RATE_KEY);
  }
  listeners.forEach((listener) => listener());
}
