import './CreatePostPage.css';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
 
import { createPost, updatePost, getPost } from '../../entities/post/api/posts';
 
const TOPICS = [
  'Битви',
  'Політика',
  'Культура',
  'Наука',
  'Україна',
  'Античність',
  'Середньовіччя',
];
 
function CreatePostPage() {
  const navigate = useNavigate();
  // ✅ Якщо є id в URL — режим редагування
  const { id } = useParams();
  const isEdit = Boolean(id);
 
  const [form, setForm] = useState({
    title: '',
    date: '',
    tag: 'Битви',
    text: '',
    imageUrl: '',
  });
 
  const [loading, setLoading] = useState(false);
 
  // ✅ Завантажуємо дані поста якщо це режим редагування
  useEffect(() => {
    if (!isEdit) return;
 
    const fetchPost = async () => {
      try {
        const data = await getPost(id);
        setForm({
          title: data.title || '',
          date: data.date || '',
          tag: data.tags?.[0] || 'Битви',
          text: data.text || '',
          imageUrl: data.imageUrl || '',
        });
      } catch (err) {
        console.error(err);
        alert('Не вдалося завантажити статтю');
      }
    };
 
    fetchPost();
  }, [id, isEdit]);
 
  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };
 
  const handleSubmit = async (e) => {
    e.preventDefault();
 
    if (!form.title.trim() || !form.text.trim()) {
      alert('Заповніть назву та текст');
      return;
    }
 
    const payload = {
      title: form.title,
      text: form.text,
      imageUrl: form.imageUrl,
      date: form.date,
      tags: [form.tag],
    };
 
    try {
      setLoading(true);
 
      if (isEdit) {
        // ✅ Режим редагування
        await updatePost(id, payload);
        navigate('/adminPosts');
      } else {
        // ✅ Режим створення
        const post = await createPost(payload);
        navigate(`/posts/${post._id}`);
      }
    } catch (err) {
      console.error(err);
      alert(isEdit ? 'Не вдалося оновити статтю' : 'Не вдалося створити статтю');
    } finally {
      setLoading(false);
    }
  };
 
  return (
    <main className="create-post-page">
      <nav className="navigation">
        <Link to={isEdit ? '/adminPosts' : '/'}>← Назад</Link>
      </nav>
 
      <div className="create-post-container">
        <div className="create-post-card">
          {/* ✅ Заголовок залежить від режиму */}
          <h1>{isEdit ? 'Редагування публікації' : 'Створення публікації'}</h1>
 
          <form className="create-post-form" onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="title">Назва події</label>
              <input
                id="title"
                name="title"
                value={form.title}
                onChange={handleChange}
                placeholder="Введіть назву"
              />
            </div>
 
            <div className="form-group">
              <label htmlFor="date">Дата події</label>
              <input
                id="date"
                name="date"
                type="date"
                value={form.date}
                onChange={handleChange}
              />
            </div>
 
            <div className="form-group">
              <label htmlFor="tag">Топік</label>
              <select
                id="tag"
                name="tag"
                value={form.tag}
                onChange={handleChange}
              >
                {TOPICS.map((topic) => (
                  <option key={topic} value={topic}>
                    {topic}
                  </option>
                ))}
              </select>
            </div>
 
            <div className="form-group">
              <label htmlFor="text">Опис події</label>
              <textarea
                id="text"
                name="text"
                rows="10"
                value={form.text}
                onChange={handleChange}
                placeholder="Введіть текст статті..."
              />
            </div>
 
            <div className="form-group">
              <label htmlFor="imageUrl">Посилання на зображення</label>
              <input
                id="imageUrl"
                name="imageUrl"
                value={form.imageUrl}
                onChange={handleChange}
                placeholder="https://..."
              />
            </div>
 
            <button
              type="submit"
              className="publish-btn"
              disabled={loading}
            >
              {loading
                ? 'Збереження...'
                : isEdit
                  ? 'Зберегти зміни'
                  : 'Опублікувати'}
            </button>
          </form>
        </div>
      </div>
    </main>
  );
}
 
export default CreatePostPage;