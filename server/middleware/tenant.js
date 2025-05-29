export function verifyTenant(req, res, next) {
  const churchId = req.user?.churchId;
  if (!churchId) return res.status(403).json({ message: 'Invalid church' });
  req.churchId = churchId;
  next();
}
