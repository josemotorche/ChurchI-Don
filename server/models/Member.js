import mongoose from 'mongoose';

const memberSchema = new mongoose.Schema({
  nombre: { type: String, required: true },
  email: { type: String },
  direccion: { type: String },
  fechaNacimiento: { type: Date },
  iglesiaId: { type: mongoose.Schema.Types.ObjectId, ref: 'Church', required: true }
});

export default mongoose.model('Member', memberSchema);
