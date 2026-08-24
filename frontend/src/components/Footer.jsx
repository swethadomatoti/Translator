export default function Footer() {
  return (
    <footer>
      <strong>How this works:</strong> Bhasha checks a small curated phrasebook first. For
      English, Hindi, Spanish, and French, anything outside that list falls back to a local
      offline translation engine (open-ended text, marked "auto-translated"). Telugu, Tamil,
      Kannada, and Malayalam are phrasebook-only for now. Photo capture reads text out of the
      image (OCR) into the box for you to check before translating. Click-to-talk and photo
      capture depend on microphone and camera permissions your browser may or may not grant.
    </footer>
  );
}
