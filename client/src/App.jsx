import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  return (
    <div className="container mx-auto p-4">
      <nav className="mb-4">
        <Link to="/login" className="mr-4">Login</Link>
        <Link to="/register">Register</Link>
      </nav>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </div>
  );
}

export default App;
