import './RegistrationPage.css';
import { Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';

import { register } from '../../entities/user/api/auth';

function RegistrationPage() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: '',
    surname: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    console.log(form);
    setForm((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const data = await register(form);

      localStorage.setItem(
        'token',
        data.token
      );

      navigate('/');
    } catch (err) {
      console.error(err);
      alert('Помилка реєстрації');
    }
  };

  return (
    <div className="register-page">
      <nav className="navigation">
        <Link to="/">← На головну</Link>
      </nav>

      <div className="register-container">
        <div className="register-card">
          <h1>Реєстрація</h1>

          <form
            className="register-form"
            onSubmit={handleSubmit}
          >
            <div className="form-group">
              <label>Ім'я</label>
              <input
                name="name"
                value={form.name}
                onChange={handleChange}
              />
            </div>

            <div className="form-group">
              <label>Прізвище</label>
              <input
                name="surname"
                value={form.surname}
                onChange={handleChange}
              />
            </div>

            <div className="form-group">
              <label>Email</label>
              <input
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
              />
            </div>

            <div className="form-group">
              <label>Пароль</label>
              <input
                type="password"
                name="password"
                value={form.password}
                onChange={handleChange}
              />
            </div>

            <button
              type="submit"
              className="register-btn"
            >
              Зареєструватися
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default RegistrationPage;