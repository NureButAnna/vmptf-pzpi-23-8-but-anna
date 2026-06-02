const API_URL = 'http://localhost:7000';
 
export async function api(url, options = {}) {
  const token = localStorage.getItem('token');
 
  const response = await fetch(`${API_URL}${url}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });
 
  if (!response.ok) {
    throw new Error('API Error');
  }
 
  return response.json();
}
 