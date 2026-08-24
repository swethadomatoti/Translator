import { useCallback, useEffect, useRef, useState } from 'react';
import Banner from './components/Banner';
import Chips from './components/Chips';
import Footer from './components/Footer';
import HeroBand from './components/HeroBand';
import LanguageBar from './components/LanguageBar';
import TranslatorPanel from './components/TranslatorPanel';
import { fetchLanguages, fetchPhraseChips, translate } from './api';
import { useSpeech } from './hooks/useSpeech';

const LANG_FALLBACK = { code: 'en', name: 'English', native: 'English', bcp47: 'en-US' };

export default function App() {
  const [languages, setLanguages] = useState([]);
  const [fromCode, setFromCode] = useState('te');
  const [toCode, setToCode] = useState('en');
  const [sourceText, setSourceText] = useState('');
  const [output, setOutput] = useState({ status: 'empty' });
  const [chips, setChips] = useState([]);
  const [swapping, setSwapping] = useState(false);
  const [bannerMessage, setBannerMessage] = useState('');
  const [promptListen, setPromptListen] = useState(false);
  const bannerTimerRef = useRef(null);
  const { speak, isSpeaking } = useSpeech();

  useEffect(() => {
    fetchLanguages()
      .then(setLanguages)
      .catch(() => showBanner("Couldn't reach the Bhasha backend — make sure the Django server is running."));
  }, []);

  useEffect(() => {
    fetchPhraseChips(fromCode)
      .then(setChips)
      .catch(() => setChips([]));
  }, [fromCode]);

  const showBanner = useCallback((message) => {
    setBannerMessage(message);
    clearTimeout(bannerTimerRef.current);
    bannerTimerRef.current = setTimeout(() => setBannerMessage(''), 6000);
  }, []);

  const langByCode = (code) => languages.find((l) => l.code === code) || LANG_FALLBACK;

  const runTranslate = useCallback(
    async (overrideText, autoSpeak = false) => {
      const text = overrideText ?? sourceText;
      setPromptListen(false);
      if (!text.trim()) {
        setOutput({ status: 'empty' });
        return;
      }
      try {
        const result = await translate({ text, from: fromCode, to: toCode });
        if (result.status === 'ok') {
          setOutput({ status: 'ok', text: result.translation, source: result.source });
          // Try auto-play from the mic; if the browser never actually starts it (a
          // real gesture-policy quirk on some setups), fall back to a hard-to-miss
          // manual prompt instead of leaving the user with silence and no cue.
          if (autoSpeak) {
            speak(result.translation, langByCode(toCode).bcp47, showBanner, () => setPromptListen(true));
          }
        } else if (result.status === 'unsupported') {
          setOutput({ status: 'unsupported', languages: result.phrasebook_languages });
        } else {
          setOutput({ status: 'no-match' });
        }
      } catch {
        showBanner("Couldn't reach the Bhasha backend — make sure the Django server is running.");
      }
    },
    [sourceText, fromCode, toCode, showBanner, speak, languages]
  );

  function handleSwap() {
    const nextFrom = toCode;
    const nextTo = fromCode;
    setFromCode(nextFrom);
    setToCode(nextTo);
    setSwapping((s) => !s);

    const carriedText = output.status === 'ok' ? output.text : '';
    setSourceText(carriedText);
    if (carriedText.trim()) {
      translate({ text: carriedText, from: nextFrom, to: nextTo })
        .then((result) => {
          if (result.status === 'ok') setOutput({ status: 'ok', text: result.translation });
          else if (result.status === 'unsupported') setOutput({ status: 'unsupported', languages: result.phrasebook_languages });
          else setOutput({ status: 'no-match' });
        })
        .catch(() => showBanner("Couldn't reach the Bhasha backend — make sure the Django server is running."));
    } else {
      setOutput({ status: 'empty' });
    }
  }

  function handleChipPick(text) {
    setSourceText(text);
    runTranslate(text);
  }

  async function handleCopy(text) {
    try {
      await navigator.clipboard.writeText(text);
      showBanner('Copied to clipboard.');
    } catch {
      showBanner("Couldn't copy — your browser may be blocking clipboard access here.");
    }
  }

  const phrasebookNames = languages
    .filter((l) => l.is_phrasebook)
    .map((l) => l.name)
    .join(', ');

  return (
    <>
      <HeroBand />
      <div className="content">
        <Banner message={bannerMessage} onDismiss={() => setBannerMessage('')} />

        <LanguageBar
          languages={languages}
          fromCode={fromCode}
          toCode={toCode}
          onFromChange={setFromCode}
          onToChange={setToCode}
          onSwap={handleSwap}
          swapping={swapping}
        />

        <TranslatorPanel
          sourceText={sourceText}
          onSourceTextChange={setSourceText}
          output={output.status === 'unsupported' ? { ...output } : output}
          phrasebookNames={
            output.status === 'unsupported' ? output.languages.join(', ') : phrasebookNames
          }
          fromBcp47={langByCode(fromCode).bcp47}
          toBcp47={langByCode(toCode).bcp47}
          fromLanguageName={langByCode(fromCode).name}
          onTranslate={runTranslate}
          onSpeak={(text, bcp47) => {
            setPromptListen(false);
            speak(text, bcp47, showBanner);
          }}
          isSpeaking={isSpeaking}
          promptListen={promptListen}
          onCopy={handleCopy}
          onBanner={showBanner}
        />

        <Chips chips={chips} onPick={handleChipPick} />

        <Footer />
      </div>
    </>
  );
}
