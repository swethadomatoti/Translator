import { CloseIcon } from './Icons';

export default function Banner({ message, onDismiss }) {
  return (
    <div id="banner" className={message ? 'show' : ''} role="status" aria-live="polite">
      <span id="bannerText">{message}</span>
      <button onClick={onDismiss} aria-label="Dismiss">
        <CloseIcon />
      </button>
    </div>
  );
}
