import { useRef } from "react";
import { useLocation } from "react-router-dom";
import { stopSpeech } from "../lib/speech";

/**
 * Stop edge-tts / Web Speech when the route changes.
 * Runs during render (not useEffect) so a new page's auto-speak can start afterward.
 */
export function StopSpeechOnNavigate() {
  const { pathname } = useLocation();
  const prevPathname = useRef(pathname);
  if (prevPathname.current !== pathname) {
    prevPathname.current = pathname;
    stopSpeech();
  }
  return null;
}
