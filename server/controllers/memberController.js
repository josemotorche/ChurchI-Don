import Member from '../models/memberModel.js';

export async function createMember(req, res) {
  try {
    const member = await Member.create(req.body);
    res.status(201).json(member);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
}

export async function getMembers(req, res) {
  try {
    const members = await Member.find({ iglesiaId: req.user.iglesiaId });
    res.json(members);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function getMemberById(req, res) {
  try {
    const member = await Member.findOne({ _id: req.params.id, iglesiaId: req.user.iglesiaId });
    if (!member) return res.status(404).json({ message: 'Miembro no encontrado' });
    res.json(member);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

export async function updateMember(req, res) {
  try {
    const member = await Member.findOneAndUpdate(
      { _id: req.params.id, iglesiaId: req.user.iglesiaId },
      req.body,
      { new: true }
    );
    if (!member) return res.status(404).json({ message: 'Miembro no encontrado' });
    res.json(member);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
}

export async function deleteMember(req, res) {
  try {
    const member = await Member.findOneAndDelete({ _id: req.params.id, iglesiaId: req.user.iglesiaId });
    if (!member) return res.status(404).json({ message: 'Miembro no encontrado' });
    res.json({ message: 'Miembro eliminado' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}
