import { api } from '../../../shared/api/client';

export const getPosts = () =>
  api('/posts');

export const getPost = (id) =>
  api(`/posts/${id}`);

export const createPost = (data) =>
  api('/posts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

export const deletePost = (id) =>
  api(`/posts/${id}`, {
    method: 'DELETE',
  });

export const updatePost = (id, data) =>
  api(`/posts/${id}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });