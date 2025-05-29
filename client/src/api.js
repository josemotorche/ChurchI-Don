const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

async function request(path, options = {}) {
  const token = localStorage.getItem('token');
  const headers = {
    'Content-Type': 'application/json',
    ...(token && { Authorization: `Bearer ${token}` })
  };
  const res = await fetch(`${apiUrl}${path}`, {
    ...options,
    headers,
  });
  if (!res.ok) {
    throw new Error('API error');
  }
  return res.json();
}

export default {
  post: (path, body) => request(path, { method: 'POST', body: JSON.stringify(body) }),
  get: (path) => request(path),
};
