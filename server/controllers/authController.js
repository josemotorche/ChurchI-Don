import jwt from 'jsonwebtoken';
import User from '../models/User.js';

export async function register(req, res) {
  const { email, password, role, churchId } = req.body;
  try {
    const user = await User.create({ email, password, role, churchId });
    res.json({ id: user._id, email: user.email });
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
}

export async function login(req, res) {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ email });
    if (!user) throw new Error('User not found');
    const match = await user.comparePassword(password);
    if (!match) throw new Error('Bad credentials');
    const token = jwt.sign({ id: user._id, churchId: user.churchId, role: user.role }, process.env.JWT_SECRET || 'secret');
    res.json({ token });
  } catch (err) {
    res.status(401).json({ message: err.message });
  }
}
