import { useState } from 'react';
import { Routes, Route } from 'react-router-dom';

import Header from '../widgets/Header';
import PostPage from '../pages/PostPage';
import PostsPage from '../pages/PostsPage';
import RegistrationPage from '../pages/RegistrationPage';
import LoginPage from '../pages/LoginPage';
import CreatePostPage from '../pages/CreatePostPage';
import AdminPostsPage from '../pages/AdminPostsPage';

import './styles/App.css';

function App() {
  const [search, setSearch] = useState('');
  const [isAuth, setIsAuth] = useState(
    Boolean(localStorage.getItem('token'))
  );

  return (
    <>
      <Header
        search={search}
        setSearch={setSearch}
        isAuth={isAuth}
        setIsAuth={setIsAuth}
      />

      <Routes>
        <Route
          path="/"
          element={<PostsPage search={search} />}
        />
        <Route path="/posts/:id" element={<PostPage />} />
        <Route path="/register" element={<RegistrationPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/createPost" element={<CreatePostPage />} />
        <Route path="/editPost/:id" element={<CreatePostPage />} />
        <Route path="/adminPosts" element={<AdminPostsPage />} />
      </Routes>
    </>
  );
}

export default App;