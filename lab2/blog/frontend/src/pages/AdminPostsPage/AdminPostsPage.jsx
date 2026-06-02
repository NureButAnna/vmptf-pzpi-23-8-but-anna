import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './AdminPostsPage.css';
import { getPosts, deletePost } from '../../entities/post/api/posts';
 
function AdminPostsPage() {
  const [posts, setPosts] = useState([]);
 
  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const data = await getPosts();
        setPosts(data);
      } catch (err) {
        console.error(err);
      }
    };
 
    fetchPosts();
  }, []);
 
  const handleDelete = async (id) => {
    const confirmed = window.confirm('Видалити цю статтю?');
    if (!confirmed) return;
 
    try {
      await deletePost(id);
      setPosts((prev) => prev.filter((post) => post._id !== id));
    } catch (err) {
      console.error(err);
      alert('Не вдалося видалити статтю');
    }
  };
 
  return (
    <main className="admin-posts-page">
      <div className="page-header">
        <h1>Керування статтями</h1>
 
        <Link to="/createPost" className="add-post-btn">
          + Додати статтю
        </Link>
      </div>
 
      <div className="posts-list">
        {posts.map((post) => (
          <article key={post._id} className="admin-post-card">
            <div className="post-content">
              <span className="post-date">{post.date}</span>
              <h2>{post.title}</h2>
              <p>{post.text}</p>
              <span className="post-author">
                {post.user?.name || 'Автор'}
              </span>
            </div>
 
            <div className="post-controls">
              <Link
                to={`/editPost/${post._id}`}
                className="icon-btn edit-btn"
                title="Редагувати"
              >
                ✏️
              </Link>
 
              <button
                className="icon-btn delete-btn"
                title="Видалити"
                onClick={() => handleDelete(post._id)}
              >
                🗑️
              </button>
            </div>
          </article>
        ))}
      </div>
    </main>
  );
}
 
export default AdminPostsPage;