import Member from '../models/Member.js';

export async function createMember(req, res) {
  try {
    const member = await Member.create({ ...req.body, iglesiaId: req.churchId });
    res.json(member);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
}

export async function getMembers(req, res) {
  const members = await Member.find({ iglesiaId: req.churchId });
  res.json(members);
}

export async function getMember(req, res) {
  const member = await Member.findOne({ _id: req.params.id, iglesiaId: req.churchId });
  if (!member) return res.status(404).json({ message: 'Not found' });
  res.json(member);
}

export async function updateMember(req, res) {
  try {
    const member = await Member.findOneAndUpdate(
      { _id: req.params.id, iglesiaId: req.churchId },
      req.body,
      { new: true }
    );
    if (!member) return res.status(404).json({ message: 'Not found' });
    res.json(member);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
}

export async function deleteMember(req, res) {
  const member = await Member.findOneAndDelete({ _id: req.params.id, iglesiaId: req.churchId });
  if (!member) return res.status(404).json({ message: 'Not found' });
  res.json({ message: 'Deleted' });
}
