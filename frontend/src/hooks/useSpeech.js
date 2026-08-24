import { useEffect, useRef, useState } from 'react';

// Chrome/Edge on Windows have a long-standing bug where the speech engine silently
// wedges after the first utterance -- speak() is accepted but never actually starts.
// If playback hasn't started within this window, treat it as stuck and force a reset.
const START_TIMEOUT_MS = 2000;

export function useSpeech() {
  const voicesRef = useRef([]);
  const [isSpeaking, setIsSpeaking] = useState(false);

  useEffect(() => {
    if (!('speechSynthesis' in window)) return;
    const loadVoices = () => {
      voicesRef.current = speechSynthesis.getVoices();
    };
    loadVoices();
    speechSynthesis.onvoiceschanged = loadVoices;

    // Keeps the engine from ever fully idling into the wedged state described above.
    const keepAlive = setInterval(() => {
      if (speechSynthesis.paused) speechSynthesis.resume();
    }, 8000);
    return () => clearInterval(keepAlive);
  }, []);

  function buildUtterance(text, bcp47, onEnded, onError, state) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = bcp47;
    const base = bcp47.split('-')[0].toLowerCase();
    const candidates = voicesRef.current.filter(
      (v) => v.lang.toLowerCase() === bcp47.toLowerCase() || v.lang.toLowerCase().startsWith(base)
    );
    const match = candidates.find((v) => v.localService) || candidates[0];
    if (match) utterance.voice = match;
    utterance.onstart = () => {
      state.started = true;
    };
    utterance.onend = onEnded;
    utterance.onerror = (e) => {
      onEnded();
      if (e.error === 'canceled' || e.error === 'interrupted') {
        // Someone else (e.g. the mic starting a fresh recording) stopped this on
        // purpose -- mark it so the stuck-playback retry below doesn't resurrect it.
        state.cancelled = true;
        return;
      }
      onError?.("Couldn't play voice for this language in this browser.");
    };
    return utterance;
  }

  function speak(text, bcp47, onError, onNoStart) {
    if (!text) return;
    if (!('speechSynthesis' in window)) {
      onError?.("Voice playback isn't available in this browser preview.");
      onNoStart?.();
      return;
    }
    try {
      setIsSpeaking(true);
      const onEnded = () => setIsSpeaking(false);
      speechSynthesis.resume();

      const state = { started: false, cancelled: false };
      const utterance = buildUtterance(text, bcp47, onEnded, onError, state);

      // Only cancel when something's actually active -- calling cancel() on an idle
      // engine is itself a trigger for the wedge bug on some Chrome/Windows builds.
      if (speechSynthesis.speaking || speechSynthesis.pending) {
        speechSynthesis.cancel();
      }
      speechSynthesis.speak(utterance);

      setTimeout(() => {
        if (state.started || state.cancelled) return;
        speechSynthesis.cancel();
        const retryState = { started: false, cancelled: false };
        speechSynthesis.speak(buildUtterance(text, bcp47, onEnded, onError, retryState));

        // Still hasn't actually started after a forced reset -- give up on auto-play
        // for this one and let the caller offer a manual fallback instead.
        setTimeout(() => {
          if (!retryState.started && !retryState.cancelled) onNoStart?.();
        }, START_TIMEOUT_MS);
      }, START_TIMEOUT_MS);
    } catch {
      setIsSpeaking(false);
      onError?.("Voice playback isn't available in this browser preview.");
      onNoStart?.();
    }
  }

  return { speak, isSpeaking };
}
