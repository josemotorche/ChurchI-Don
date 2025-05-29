import mongoose from 'mongoose';

const memberSchema = new mongoose.Schema({
  nombre: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  direccion: String,
  fechaNacimiento: Date,
  iglesiaId: { type: mongoose.Schema.Types.ObjectId, ref: 'Church', required: true }
}, { timestamps: true });

export default mongoose.model('Member', memberSchema);
