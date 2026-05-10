export default function Search({
  value,
  setValue
}) {
  return (
    <input
      type="text"
      placeholder="Пошук користувачів"
      className="search"
      value={value}
      onChange={(e) =>
        setValue(e.target.value)
      }
    />
  );
}