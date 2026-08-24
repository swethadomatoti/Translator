import { useRef } from 'react';

const TESSERACT_LANG = {
  en: 'eng',
  hi: 'hin',
  te: 'tel',
  ta: 'tam',
  kn: 'kan',
  ml: 'mal',
  bn: 'ben',
  mr: 'mar',
  gu: 'guj',
  pa: 'pan',
  ur: 'urd',
  or: 'ori',
  as: 'asm',
  ne: 'nep',
  si: 'sin',
  zh: 'chi_sim',
  ja: 'jpn',
  ko: 'kor',
  th: 'tha',
  vi: 'vie',
  id: 'ind',
  ms: 'msa',
  fil: 'fil',
  my: 'mya',
  mn: 'mon',
  es: 'spa',
  fr: 'fra',
  de: 'deu',
  it: 'ita',
  pt: 'por',
  nl: 'nld',
  ru: 'rus',
  uk: 'ukr',
  pl: 'pol',
  sv: 'swe',
  nb: 'nor',
  da: 'dan',
  fi: 'fin',
  el: 'ell',
  cs: 'ces',
  hu: 'hun',
  ro: 'ron',
  ar: 'ara',
  he: 'heb',
  fa: 'fas',
  tr: 'tur',
  sw: 'swa',
  zu: 'zul',
  am: 'amh',
};

export function ocrLangFor(bcp47) {
  const base = (bcp47 || 'en').split('-')[0].toLowerCase();
  return TESSERACT_LANG[base] || 'eng';
}

export function useOcr() {
  const workerRef = useRef(null);
  const workerLangRef = useRef(null);

  async function recognizeText(imageDataUrl, bcp47) {
    const { createWorker } = await import('tesseract.js');
    const lang = ocrLangFor(bcp47);

    if (!workerRef.current) {
      workerRef.current = await createWorker(lang);
      workerLangRef.current = lang;
    } else if (workerLangRef.current !== lang) {
      await workerRef.current.reinitialize(lang);
      workerLangRef.current = lang;
    }

    const {
      data: { text },
    } = await workerRef.current.recognize(imageDataUrl);
    return text.trim();
  }

  return { recognizeText };
}
