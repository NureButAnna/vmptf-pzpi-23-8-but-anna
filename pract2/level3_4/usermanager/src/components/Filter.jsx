export default function GroupFilter({
  groupFilter,
  setGroupFilter,
  groups
}) {
  return (
    <select
      value={groupFilter}
      onChange={(e) =>
        setGroupFilter(e.target.value)
      }
    >
      <option value="All">
        Усі групи
      </option>

      {groups.map(group => (
        <option
          key={group.id}
          value={group.id}
        >
          {group.name}
        </option>
      ))}
    </select>
  );
}