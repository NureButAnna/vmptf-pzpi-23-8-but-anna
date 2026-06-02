import './PostsPage.css';
import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';

import { searchPosts } from '../../features/search-post';
import { getPosts } from '../../entities/post/api/posts';

const tagColors = {
  Битви: '#FDE2E4',
  Війни: '#FFD6A5',
  Політика: '#D8E2DC',
  Культура: '#E4C1F9',
  Наука: '#CDEAC0',
  Відкриття: '#BDE0FE',
  Середньовіччя: '#E2F0CB',
  Античність: '#F8EDEB',
};

function PostsPage({ search = '' }) {
  
  const [posts, setPosts] = useState([]);
  const [selectedTopic, setSelectedTopic] = useState('Усі');

  useEffect(() => {
    async function fetchPosts() {
      try {
        const data = await getPosts();
        setPosts(data);
      } catch (err) {
        console.error('Помилка завантаження постів:', err);
      }
    }

    fetchPosts();
  }, []);

  const topics = [
    'Усі',
    ...new Set(
      posts.flatMap(post => post.tags || [])
    ),
  ];

  const topicFilteredPosts =
    selectedTopic === 'Усі'
      ? posts
      : posts.filter(
          post =>
            post.tags?.includes(selectedTopic)
        );

  const filteredPosts = searchPosts(
    topicFilteredPosts,
    search
  );

  return (
    <main className="posts-page">
      <header className="hero">
        <h1>Події сьогодні</h1>
        <p>{new Date().toLocaleDateString('uk-UA')}</p>
      </header>

      <section className="topics">
        {topics.map(topic => (
          <button
            key={topic}
            className={`topic-btn ${
              selectedTopic === topic ? 'topic-btn--active' : ''
            }`}
            onClick={() => setSelectedTopic(topic)}
          >
            {topic}
          </button>
        ))}
      </section>

      <section className="posts-grid">
        {filteredPosts.map(post => (
          <article key={post._id} className="post-card">
            <span className="post-date">{post.date}</span>

            <div className="post-tags">
              {post.tags?.map(tag => (
                <span
                  key={tag}
                  className="post-tag"
                  style={{
                    backgroundColor: tagColors[tag] || '#f0f0f0',
                  }}
                >
                  {tag}
                </span>
              ))}
            </div>

            <h2>{post.title}</h2>

            <p className="post-text">
              {post.text?.trim()}
            </p>

            <footer className="post-footer">
             <span>{post.user?.name || 'Автор'}</span>

              <Link
                to={`/posts/${post._id}`}
                className="read-more-btn"
              >
                Детальніше
              </Link>
            </footer>
          </article>
        ))}
      </section>
    </main>
  );
}

export default PostsPage;