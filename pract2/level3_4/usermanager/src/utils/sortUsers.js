export default function sortUsers(
  users,
  sortField,
  sortOrder
) {

  return [...users].sort((a, b) => {

    if (!sortField) return 0;

    const aValue =
      a[sortField]
        .toString()
        .toLowerCase();

    const bValue =
      b[sortField]
        .toString()
        .toLowerCase();

    if (aValue < bValue) {
      return sortOrder === "asc"
        ? -1
        : 1;
    }

    if (aValue > bValue) {
      return sortOrder === "asc"
        ? 1
        : -1;
    }

    return 0;
  });
}