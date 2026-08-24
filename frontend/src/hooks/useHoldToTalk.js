import { useRef, useState } from 'react';

const SpeechRecognitionCtor = window.SpeechRecognition || window.webkitSpeechRecognition;

// Speaks a near-silent utterance so browsers (Edge/Chrome) treat speechSynthesis as
// user-activated for a little while afterward. The actual translated playback fires
// later from an async callback (after real speech + a network round trip), where the
// original gesture would otherwise be stale -- called again on each press/release so
// the activation window stays as fresh as possible right up to when it's needed.
function unlockSpeech() {
  if (!('speechSynthesis' in window)) return;
  // Skip if anything (a prior warmup or real speech) is still outstanding -- queuing
  // another one behind it is what let unresolved utterances pile up across presses.
  if (speechSynthesis.speaking || speechSynthesis.pending) return;
  try {
    const warmup = new SpeechSynthesisUtterance(' ');
    warmup.volume = 0;
    warmup.onend = warmup.onerror = () => {};
    speechSynthesis.speak(warmup);
  } catch {
    // Best-effort unlock only -- ignore failures here.
  }
}

// Click-to-start / click-to-stop toggle rather than press-and-hold: holding a mouse
// button down while also speaking is awkward with a cursor (fine on a touchscreen,
// but this app is mouse-driven), so a plain click on/off is far less finicky.
export function useHoldToTalk({ bcp47, onResult, onError }) {
  const [isRecording, setIsRecording] = useState(false);
  const recognizerRef = useRef(null);

  function start() {
    if (!SpeechRecognitionCtor) {
      onError("This browser doesn't support voice input. Try typing instead.");
      return;
    }
    // Stop any leftover playback from a previous auto-spoken translation first --
    // starting a new recording while the browser still considers the tab to be
    // producing audio can make it treat the microphone as busy/suppressed.
    if ('speechSynthesis' in window) {
      try {
        speechSynthesis.cancel();
      } catch {
        // no-op
      }
    }
    unlockSpeech();
    try {
      const recognizer = new SpeechRecognitionCtor();
      recognizer.lang = bcp47;
      recognizer.interimResults = false;
      recognizer.maxAlternatives = 1;

      recognizer.onstart = () => setIsRecording(true);
      recognizer.onresult = (e) => onResult(e.results[0][0].transcript);
      recognizer.onerror = (e) => {
        onError(
          `Voice input needs microphone access it could not get here (${e.error || 'unavailable'}). You can type instead.`
        );
      };
      recognizer.onend = () => setIsRecording(false);

      recognizerRef.current = recognizer;
      recognizer.start();
    } catch {
      onError("Couldn't start voice input in this browser preview. Try typing instead.");
      setIsRecording(false);
    }
  }

  function stop() {
    // Re-unlock right at this click too -- it's the gesture closest in time to when
    // the translated speech will actually need to play, once recognition finishes.
    unlockSpeech();
    if (recognizerRef.current && isRecording) {
      try {
        recognizerRef.current.stop();
      } catch {
        // no-op
      }
    }
  }

  function onClick(e) {
    e.preventDefault();
    if (isRecording) {
      stop();
    } else {
      start();
    }
  }

  return {
    isRecording,
    handlers: {
      onClick,
      onContextMenu: (e) => e.preventDefault(),
    },
  };
}
