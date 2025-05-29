import jwt from 'jsonwebtoken';

export function authenticate(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) return res.status(401).json({ message: 'Token requerido' });
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET || 'secret');
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(403).json({ message: 'Token inválido' });
  }
}

export function verifyChurch(req, res, next) {
  const churchId = req.user && req.user.iglesiaId;
  if (!churchId) return res.status(403).json({ message: 'Iglesia no válida' });
  // If body or params specify iglesiaId, ensure they match
  const requested = req.body.iglesiaId || req.params.iglesiaId;
  if (requested && requested !== churchId) {
    return res.status(403).json({ message: 'No autorizado para esta iglesia' });
  }
  // attach churchId to body for convenience
  if (!req.body.iglesiaId) req.body.iglesiaId = churchId;
  next();
}
