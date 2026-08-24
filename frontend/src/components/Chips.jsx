export default function Chips({ chips, onPick }) {
  return (
    <div className="chipsWrap">
      <div className="chipsLabel">Try a phrase</div>
      <div className="chips">
        {chips.length === 0 && <span className="chip">No sample phrases for this language yet</span>}
        {chips.map((chip) => (
          <button key={chip.slug} className="chip script" onClick={() => onPick(chip.text)}>
            {chip.text}
          </button>
        ))}
      </div>
    </div>
  );
}
