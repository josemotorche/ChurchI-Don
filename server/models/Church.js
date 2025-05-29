
import mongoose from 'mongoose';

const churchSchema = new mongoose.Schema({
  name: { type: String, required: true }
});

export default mongoose.model('Church', churchSchema);
=======
const mongoose = require('mongoose');

const ChurchSchema = new mongoose.Schema({
  name: { type: String, required: true },
  address: String
});

module.exports = mongoose.model('Church', ChurchSchema);

