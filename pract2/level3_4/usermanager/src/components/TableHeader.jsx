export default function TableHeader({
  sortField,
  sortOrder,
  handleSort
}) {
  return (
    <thead>
      <tr>

        <th
          className="click"
          onClick={() => handleSort("name")}
        >
          Ім'я

          {sortField === "name" &&
            (sortOrder === "asc"
              ? " ↑"
              : " ↓")}
        </th>

        <th
          className="click"
          onClick={() => handleSort("email")}
        >
          Email

          {sortField === "email" &&
            (sortOrder === "asc"
              ? " ↑"
              : " ↓")}
        </th>

        <th>Група</th>

      </tr>
    </thead>
  );
}