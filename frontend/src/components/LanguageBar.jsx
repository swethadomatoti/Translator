import { SwapIcon } from './Icons';

function groupLanguages(languages) {
  const groups = [];
  const byName = new Map();
  for (const lang of languages) {
    if (!byName.has(lang.group)) {
      const group = { name: lang.group, languages: [] };
      byName.set(lang.group, group);
      groups.push(group);
    }
    byName.get(lang.group).languages.push(lang);
  }
  return groups;
}

function LanguageSelect({ id, label, languages, value, onChange }) {
  const groups = groupLanguages(languages);
  return (
    <div className="langfield">
      <label htmlFor={id}>{label}</label>
      <select id={id} className="langselect" value={value} onChange={(e) => onChange(e.target.value)}>
        {groups.map((group) => (
          <optgroup key={group.name} label={group.name}>
            {group.languages.map((lang) => (
              <option key={lang.code} value={lang.code}>
                {lang.native === lang.name ? lang.name : `${lang.name} — ${lang.native}`}
              </option>
            ))}
          </optgroup>
        ))}
      </select>
    </div>
  );
}

export default function LanguageBar({ languages, fromCode, toCode, onFromChange, onToChange, onSwap, swapping }) {
  return (
    <div className="card langbar">
      <div className="routeRow">
        <span className="routeTag">Route</span>
        <span className="routeCodes" id="routeBadge">
          {fromCode.toUpperCase()} → {toCode.toUpperCase()}
        </span>
      </div>
      <div className="langrow">
        <LanguageSelect
          id="fromSelect"
          label="Speak / type in"
          languages={languages}
          value={fromCode}
          onChange={onFromChange}
        />
        <button
          id="swapBtn"
          className={`iconbtn${swapping ? ' spin' : ''}`}
          title="Swap languages"
          aria-label="Swap languages"
          onClick={onSwap}
        >
          <SwapIcon />
        </button>
        <LanguageSelect
          id="toSelect"
          label="Translate to"
          languages={languages}
          value={toCode}
          onChange={onToChange}
        />
      </div>
    </div>
  );
}
