export default function filterUsers(
  users,
  value,
  groupFilter
) {
  return users.filter(user => {

    const matchesSearch =
      user.name
        .toLowerCase()
        .includes(value.toLowerCase()) ||

      user.email
        .toLowerCase()
        .includes(value.toLowerCase());

    const matchesGroup =
      groupFilter === 'All' ||
      user.groupId === Number(groupFilter);

    return matchesSearch && matchesGroup;
  });
}