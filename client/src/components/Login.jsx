import React, { useState } from 'react';
import api from '../api';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post('/auth/login', { email, password });
      localStorage.setItem('token', res.token);
      setMessage('Logged in!');
    } catch (err) {
      setMessage('Login failed');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-2">
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="border p-1 block w-full" />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="border p-1 block w-full" />
      <button type="submit" className="bg-blue-500 text-white px-4 py-1">Login</button>
      {message && <p>{message}</p>}
    </form>
  );
}

export default Login;
