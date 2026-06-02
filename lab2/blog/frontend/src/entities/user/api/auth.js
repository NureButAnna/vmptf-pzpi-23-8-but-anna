import { api } from '../../../shared/api/client';

export const register = (data) =>
  api('/register', {
    method: 'POST',
    body: JSON.stringify(data),
  });

export const login = (data) =>
  api('/login', {
    method: 'POST',
    body: JSON.stringify(data),
  });

export const getMe = () =>
  api('/me');