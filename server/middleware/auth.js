const { verify } = require('../utils/jwt');

const SECRET = 'secret123';

function auth(req, res, next) {
  const authHeader = req.headers['authorization'] || '';
  const token = authHeader.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'No token' });
  const payload = verify(token, SECRET);
  if (!payload) return res.status(401).json({ message: 'Invalid token' });
  req.user = payload;
  next();
}

module.exports = { auth, SECRET };
