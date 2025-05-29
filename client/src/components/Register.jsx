import React, { useState } from 'react';
import api from '../api';

function Register() {
  const [churchName, setChurchName] = useState('');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post('/auth/register', { churchName, name, email, password });
      localStorage.setItem('token', res.token);
      setMessage('Registered!');
    } catch (err) {
      setMessage('Register failed');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-2">
      <input type="text" placeholder="Church" value={churchName} onChange={(e) => setChurchName(e.target.value)} className="border p-1 block w-full" />
      <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} className="border p-1 block w-full" />
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="border p-1 block w-full" />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="border p-1 block w-full" />
      <button type="submit" className="bg-green-500 text-white px-4 py-1">Register</button>
      {message && <p>{message}</p>}
    </form>
  );
}

export default Register;
