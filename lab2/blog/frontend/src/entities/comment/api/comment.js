import { api } from '../../../shared/api/client';

export const getComments = (postId) =>
  api(`/posts/${postId}/comments`);

export const getComment = (postId, commentId) =>
  api(`/posts/${postId}/comments/${commentId}`);

export const createComment = (postId, data) =>
  api(`/posts/${postId}/comments`, {
    method: 'POST',
    body: JSON.stringify(data),
  });

export const deleteComment = (postId, commentId) =>
  api(`/posts/${postId}/comments/${commentId}`, {
    method: 'DELETE',
  });