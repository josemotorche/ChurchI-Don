import mongoose from 'mongoose';

const churchSchema = new mongoose.Schema({
  name: { type: String, required: true }
});

export default mongoose.model('Church', churchSchema);
