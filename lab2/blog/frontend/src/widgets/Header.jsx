import './Header.css';
import { Link, useNavigate } from 'react-router-dom';
 
function Header({ search, setSearch }) {
  const navigate = useNavigate();
  const isAuth = Boolean(localStorage.getItem('token'));
 
  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };
 
  return (
    <header className="header">
      <Link to="/" className="header__logo">
        Цей день в історії
      </Link>
 
      <div className="header__right">
        <input
          className="header__search-input"
          placeholder="Пошук..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
 
        <div className="header__actions">
          {isAuth ? (
            <button
              className="header__btn"
              onClick={handleLogout}
            >
              Вихід
            </button>
          ) : (
            <>
              <Link to="/login" className="header__btn">
                Вхід
              </Link>
              <Link to="/register" className="header__btn header__btn--primary">
                Реєстрація
              </Link>
            </>
          )}
        </div>
      </div>
    </header>
  );
}
 
export default Header;
 