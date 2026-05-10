import { useState } from "react";
import { users as initialUsers } from "../data";
import { groups } from "../data";
import TableHeader from "./TableHeader";
import TableRow from "./TableRow";
import Search from "./Search";
import GroupFilter from "./Filter";
import filterUsers from "../utils/filterUsers";
import sortUsers  from "../utils/sortUsers";

export default function Table() {

  const [users, setUsers] = useState(
    JSON.parse(localStorage.getItem('users'))
    || initialUsers
  );

  const [value, setValue] = useState('');
  const [groupFilter, setGroupFilter] =
    useState('All');

  function changeGroup(userId, newGroup) {

    const updatedUsers = users.map((user) =>
      user.id === userId
        ? { ...user, groupId: newGroup }
        : user
    );

    setUsers(updatedUsers);

    localStorage.setItem(
      "users",
      JSON.stringify(updatedUsers)
    );
  }

  const filteredUsers = filterUsers(users, value, groupFilter);

  const [sortField, setSortField] = useState(null);
  const [sortOrder, setSortOrder] = useState("asc");

  function handleSort(field) {

  if (sortField === field) {

    setSortOrder(
      sortOrder === "asc"
        ? "desc"
        : "asc"
    );

  } else {

    setSortField(field);
    setSortOrder("asc");
  }
}

const sortedUsers = sortUsers(filteredUsers, sortField, sortOrder);

  return (
    <section>
      <h2 className="title">Список користувачів</h2>
        <form>

          <Search
            value={value}
            setValue={setValue}
          />

          <GroupFilter
            groupFilter={groupFilter}
            setGroupFilter={setGroupFilter}
            groups={groups}
          />

        </form>

        <table>

          <TableHeader
            sortField={sortField}
            sortOrder={sortOrder}
            handleSort={handleSort}
          />

        <tbody>

          {sortedUsers.map(user => (
            <TableRow
              key={user.id}
              {...user}
              groups={groups}
              changeGroup={changeGroup}
            />
          ))}

        </tbody>

        </table>
    </section>
  );
}