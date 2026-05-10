export default function TableRow({
  id,
  name,
  email,
  groupId,
  groups,
  changeGroup
}) {
  return (
    <tr>
      <td>{name}</td>
      <td>{email}</td>
      <td>
        <select
        value={groupId}
        onChange={(e) =>
          changeGroup(
            id,
            Number(e.target.value)
          )
        }>
          {groups.map(group => (
            <option
            key={group.id}
            value={group.id}
            >
              {group.name}
            </option>
          ))}
        </select>
      </td>
    </tr>
  );
}