import express from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv';

import memberRoutes from './routes/memberRoutes.js';

dotenv.config();

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;
const MONGO_URL = process.env.MONGO_URL || 'mongodb://localhost:27017/chms';

mongoose.connect(MONGO_URL)
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('Mongo connection error', err));

app.use('/api/members', memberRoutes);

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
