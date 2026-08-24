import { useEffect, useRef, useState } from 'react';
import { useHoldToTalk } from '../hooks/useHoldToTalk';
import { useOcr } from '../hooks/useOcr';
import {
  CameraIcon,
  CameraShutterIcon,
  CloseIcon,
  CopyIcon,
  GalleryIcon,
  ListenIcon,
  MicIcon,
} from './Icons';

function outputClassName(status) {
  if (status === 'empty') return 'script placeholder';
  if (status === 'no-match' || status === 'unsupported') return 'script err';
  return 'script';
}

function outputText(output, phrasebookNames) {
  switch (output.status) {
    case 'empty':
      return 'Your translation will appear here.';
    case 'ok':
      return output.text;
    case 'no-match':
      return "That phrase isn't in Bhasha's offline phrasebook yet — try one of the phrases below.";
    case 'unsupported':
      return `Bhasha's phrasebook currently only translates between ${phrasebookNames}.`;
    default:
      return '';
  }
}

export default function TranslatorPanel({
  sourceText,
  onSourceTextChange,
  output,
  phrasebookNames,
  fromBcp47,
  toBcp47,
  fromLanguageName,
  onTranslate,
  onSpeak,
  isSpeaking,
  promptListen,
  onCopy,
  onBanner,
}) {
  const [image, setImage] = useState(null);
  const [ocrStatus, setOcrStatus] = useState('idle');
  const [camPopOpen, setCamPopOpen] = useState(false);
  const cameraInputRef = useRef(null);
  const galleryInputRef = useRef(null);
  const camWrapRef = useRef(null);
  const { recognizeText } = useOcr();

  const { isRecording, handlers: micHandlers } = useHoldToTalk({
    bcp47: fromBcp47,
    onResult: (transcript) => {
      onSourceTextChange(transcript);
      onTranslate(transcript, true);
    },
    onError: onBanner,
  });

  function handleKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onTranslate();
    }
  }

  function handleFile(fileList) {
    const file = fileList && fileList[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => setImage(reader.result);
    reader.onerror = () => onBanner("Couldn't read that photo — try another one.");
    reader.readAsDataURL(file);
  }

  // Re-runs whenever the "Speak / type in" language changes, since OCR needs to know which
  // script to read — otherwise switching languages after attaching a photo leaves stale,
  // wrong-language garbage in the text box.
  useEffect(() => {
    if (!image) return;
    let cancelled = false;
    setOcrStatus('reading');
    recognizeText(image, fromBcp47)
      .then((text) => {
        if (cancelled) return;
        if (text) {
          onSourceTextChange(text);
          setOcrStatus('done');
        } else {
          setOcrStatus('error');
          onBanner("Couldn't find any readable text in that photo — type it manually below.");
        }
      })
      .catch(() => {
        if (cancelled) return;
        setOcrStatus('error');
        onBanner("Couldn't read text from that photo — type it manually below.");
      });
    return () => {
      cancelled = true;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [image, fromBcp47]);

  function removeImage() {
    setImage(null);
    setOcrStatus('idle');
  }

  const canOutputAct = output.status === 'ok';

  return (
    <div className="panel">
      <div className="pane">
        <div className="paneLabel">
          <span className="dot"></span>You write or speak
        </div>
        <div className="writeArea">
          <textarea
            id="sourceInput"
            className="script"
            placeholder="Type a phrase, or click the mic and speak…"
            value={sourceText}
            onChange={(e) => onSourceTextChange(e.target.value)}
            onKeyDown={handleKeyDown}
          />
        </div>

        {image && (
          <div className="imgpreview show">
            <img src={image} alt="Captured photo" />
            <button className="rm" aria-label="Remove photo" onClick={removeImage}>
              <CloseIcon />
            </button>
          </div>
        )}
        {image && (
          <p className="imghint show">
            {ocrStatus === 'reading' && 'Reading text from the photo…'}
            {ocrStatus === 'done' &&
              "Detected text from your photo below — edit it if needed, then tap Translate."}
            {ocrStatus === 'error' && "Couldn't find readable text in that photo — type it manually below."}
          </p>
        )}

        <div className="paneRow">
          <div className="paneTools">
            <button
              id="micBtn"
              className={`iconbtn${isRecording ? ' recording' : ''}`}
              title={isRecording ? 'Click to stop' : `Click to talk in ${fromLanguageName}`}
              aria-label={isRecording ? 'Click to stop recording' : `Click to talk in ${fromLanguageName}`}
              {...micHandlers}
            >
              <MicIcon />
              <span className="bars" aria-hidden="true">
                <span></span>
                <span></span>
                <span></span>
              </span>
            </button>
            <div className="camwrap" ref={camWrapRef}>
              <button
                className="iconbtn"
                title="Add a photo"
                aria-label="Add a photo"
                onClick={() => setCamPopOpen((open) => !open)}
              >
                <CameraIcon />
              </button>
              <div className={`campop${camPopOpen ? ' open' : ''}`}>
                <button
                  onClick={() => {
                    cameraInputRef.current?.click();
                    setCamPopOpen(false);
                  }}
                >
                  <CameraShutterIcon />
                  Take a photo
                </button>
                <button
                  onClick={() => {
                    galleryInputRef.current?.click();
                    setCamPopOpen(false);
                  }}
                >
                  <GalleryIcon />
                  Choose from gallery
                </button>
              </div>
            </div>
          </div>
          <button className="primary-btn" onClick={() => onTranslate()}>
            Translate
          </button>
        </div>
      </div>

      <div className="pane">
        <div className="paneLabel">
          <span className="dot"></span>Translation
        </div>
        <div className="readoutPlate">
          <div className="readoutHead">
            <span className="dot"></span>Output
          </div>
          <div id="outputBox" className={outputClassName(output.status)}>
            {outputText(output, phrasebookNames)}
          </div>
        </div>
        {output.status === 'ok' && output.source === 'machine_translation' && (
          <p className="mtNote">
            Auto-translated — not from Bhasha&apos;s curated phrasebook, so quality may vary.
          </p>
        )}
        {promptListen && <p className="listenPrompt">🔊 Tap to hear it</p>}
        <div className="paneRow">
          <div className="paneTools">
            <button
              id="listenBtn"
              className={`iconbtn${isSpeaking ? ' speaking' : ''}${promptListen ? ' prompt' : ''}`}
              title="Listen"
              aria-label="Listen to translation"
              disabled={!canOutputAct}
              onClick={() => canOutputAct && onSpeak(output.text, toBcp47)}
            >
              <ListenIcon />
            </button>
            <button
              id="copyBtn"
              className="iconbtn"
              title="Copy"
              aria-label="Copy translation"
              disabled={!canOutputAct}
              onClick={() => canOutputAct && onCopy(output.text)}
            >
              <CopyIcon />
            </button>
          </div>
        </div>
      </div>

      <input
        type="file"
        accept="image/*"
        capture="environment"
        hidden
        ref={cameraInputRef}
        onChange={(e) => {
          handleFile(e.target.files);
          e.target.value = '';
        }}
      />
      <input
        type="file"
        accept="image/*"
        hidden
        ref={galleryInputRef}
        onChange={(e) => {
          handleFile(e.target.files);
          e.target.value = '';
        }}
      />
    </div>
  );
}
