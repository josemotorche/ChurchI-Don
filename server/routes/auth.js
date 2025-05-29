
import { Router } from 'express';
import { register, login } from '../controllers/authController.js';

const router = Router();

router.post('/register', register);
router.post('/login', login);

export default router;

const express = require('express');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const Church = require('../models/Church');

const router = express.Router();

// Register new user
router.post('/register', async (req, res) => {
  const { churchName, name, email, password, role } = req.body;
  try {
    let church = await Church.findOne({ name: churchName });
    if (!church) {
      church = await Church.create({ name: churchName });
    }

    let user = await User.findOne({ email });
    if (user) return res.status(400).json({ msg: 'User already exists' });

    user = new User({ churchId: church._id, name, email, password, role });
    await user.save();

    const payload = { userId: user._id, churchId: church._id, role: user.role };
    const token = jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1d' });
    res.json({ token });
  } catch (err) {
    res.status(500).json({ msg: 'Server error' });
  }
});

// Login user
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ email });
    if (!user) return res.status(400).json({ msg: 'Invalid credentials' });
    const isMatch = await user.comparePassword(password);
    if (!isMatch) return res.status(400).json({ msg: 'Invalid credentials' });

    const payload = { userId: user._id, churchId: user.churchId, role: user.role };
    const token = jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1d' });
    res.json({ token });
  } catch (err) {
    res.status(500).json({ msg: 'Server error' });
  }
});

module.exports = router;

