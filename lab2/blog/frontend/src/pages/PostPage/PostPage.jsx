import './PostPage.css';
import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';

import { getPost } from '../../entities/post/api/posts';
import { addComment, CommentForm } from '../../features/add-comment';

function PostPage() {
  const { id } = useParams();

  const [post, setPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [text, setText] = useState('');

  useEffect(() => {
    async function fetchPost() {
      try {
        const data = await getPost(id);
        setPost(data);
        setComments(data.comments || []);
      } catch (err) {
        console.error('Помилка завантаження поста:', err);
      }
    }

    fetchPost();
  }, [id]);

  if (!post) {
    return <div>Завантаження...</div>;
  }

  const handleAdd = () => {
    setComments((prev) => addComment(prev, text));
    setText('');
  };

  return (
    <article className="post-page">
      <div className="content-wrapper">
        <nav className="post-navigation">
          <Link to="/">← На головну</Link>
        </nav>

        <section className="post">
          <span className="post-date">
            {post.date}
          </span>

          <h1>{post.title}</h1>

          <div className="post-meta">
            By {post.user?.name || 'Автор'}
          </div>

          {post.imageUrl && (
            <img
              src={post.imageUrl}
              alt={post.title}
              className="post-image"
            />
          )}

          <div className="post-text">
            {post.text}
          </div>
        </section>
        <section className="comments-section">
          <h2>Коментарі</h2>

          <CommentForm
            value={text}
            onChange={setText}
            onAdd={handleAdd}
          />

          <div className="comments-list">
            {comments.map((c) => (
              <div key={c.id} className="comment">
                <strong>{c.author}</strong>
                <p>{c.text}</p>
              </div>
            ))}
          </div>
        </section>
      </div>
    </article>
  );
}

export default PostPage;