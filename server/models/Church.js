const mongoose = require('mongoose');

const ChurchSchema = new mongoose.Schema({
  name: { type: String, required: true },
  address: String
});

module.exports = mongoose.model('Church', ChurchSchema);
