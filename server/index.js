const express = require('express');
const bodyParser = require('body-parser');
const financeRoutes = require('./routes/financeRoutes');
const { auth, SECRET } = require('./middleware/auth');
const { sign } = require('./utils/jwt');

const app = express();
app.use(bodyParser.json());

// Fake user for demo
const demoUser = { id: '1', username: 'admin', password: 'password', churchId: '1' };

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  if (username !== demoUser.username || password !== demoUser.password) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }
  const token = sign({ userId: demoUser.id, churchId: demoUser.churchId }, SECRET, { expiresIn: 60 * 60 });
  res.json({ token });
});

app.use('/api/finances', auth, financeRoutes);

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server listening on ${port}`));
