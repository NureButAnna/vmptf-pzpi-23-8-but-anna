import './LoginPage.css';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import { login } from '../../entities/user/api/auth';

function Modal({ type, onClose }) {
  const isSuccess = type === 'success';

  return (
    <div
      style={{
        position: 'fixed', inset: 0,
        background: 'rgba(0,0,0,0.45)',
        display: 'flex', alignItems: 'center',
        justifyContent: 'center', zIndex: 1000,
      }}
      onClick={onClose}
    >
      <div
        style={{
          background: 'var(--color-background-primary)',
          borderRadius: '12px',
          border: '0.5px solid var(--color-border-tertiary)',
          padding: '1.5rem',
          width: '320px',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '8px' }}>
          <div style={{
            width: '40px', height: '40px', borderRadius: '50%',
            background: isSuccess
              ? 'var(--color-background-success)'
              : 'var(--color-background-danger)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}>
            <span style={{
              fontSize: '20px',
              color: isSuccess
                ? 'var(--color-text-success)'
                : 'var(--color-text-danger)',
            }}>
              {isSuccess ? '✓' : '✕'}
            </span>
          </div>
          <p style={{ fontWeight: 500, fontSize: '16px', margin: 0 }}>
            {isSuccess ? 'Вхід успішний' : 'Помилка входу'}
          </p>
        </div>

        <p style={{ fontSize: '14px', color: 'var(--color-text-secondary)', margin: '0 0 16px' }}>
          {isSuccess
            ? 'Вас буде перенаправлено на сторінку керування статтями.'
            : 'Невірний логін або пароль. Спробуйте ще раз.'}
        </p>

        <button
          className="login-btn"
          style={{ width: '100%' }}
          onClick={onClose}
        >
          {isSuccess ? 'Продовжити' : 'Спробувати знову'}
        </button>
      </div>
    </div>
  );
}

function LoginPage() {
  const navigate = useNavigate();

  const [form, setForm] = useState({ email: '', password: '' });
  const [modal, setModal] = useState(null); // 'success' | 'error' | null

  const handleChange = (e) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const data = await login(form);
      localStorage.setItem('token', data.token);
      setModal('success');
    } catch (err) {
      console.error(err);
      setModal('error');
    }
  };

  const handleClose = () => {
    if (modal === 'success') {
      navigate('/adminPosts');
    }
    setModal(null);
  };

  return (
    <div className="login-page">
      {modal && <Modal type={modal} onClose={handleClose} />}

      <nav className="navigation">
        <Link to="/">← На головну</Link>
      </nav>

      <div className="login-container">
        <div className="login-card">
          <h1>Вхід</h1>

          <form className="login-form" onSubmit={handleSubmit}>
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

            <button type="submit" className="login-btn">
              Увійти
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;