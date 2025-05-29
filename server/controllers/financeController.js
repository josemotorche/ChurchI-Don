const fs = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '../data/finances.json');

function load() {
  if (!fs.existsSync(dataPath)) return [];
  return JSON.parse(fs.readFileSync(dataPath));
}

function save(items) {
  fs.writeFileSync(dataPath, JSON.stringify(items, null, 2));
}

function createFinance(req, res) {
  const finances = load();
  const { memberId, amount, type, category, description, date } = req.body;
  if (!amount || !type) {
    return res.status(400).json({ message: 'amount and type required' });
  }
  const finance = {
    id: Date.now().toString(),
    churchId: req.user.churchId,
    memberId: memberId || null,
    amount,
    type,
    category: category || '',
    description: description || '',
    date: date || new Date().toISOString(),
  };
  finances.push(finance);
  save(finances);
  res.status(201).json(finance);
}

function getFinances(req, res) {
  const finances = load();
  const filtered = finances.filter(f => f.churchId === req.user.churchId);
  res.json(filtered);
}

function getFinance(req, res) {
  const finances = load();
  const finance = finances.find(f => f.id === req.params.id && f.churchId === req.user.churchId);
  if (!finance) return res.status(404).json({ message: 'Not found' });
  res.json(finance);
}

function updateFinance(req, res) {
  const finances = load();
  const idx = finances.findIndex(f => f.id === req.params.id && f.churchId === req.user.churchId);
  if (idx === -1) return res.status(404).json({ message: 'Not found' });
  const item = finances[idx];
  const { memberId, amount, type, category, description, date } = req.body;
  if (amount !== undefined) item.amount = amount;
  if (type !== undefined) item.type = type;
  if (category !== undefined) item.category = category;
  if (description !== undefined) item.description = description;
  if (date !== undefined) item.date = date;
  if (memberId !== undefined) item.memberId = memberId;
  finances[idx] = item;
  save(finances);
  res.json(item);
}

function deleteFinance(req, res) {
  let finances = load();
  const initialLength = finances.length;
  finances = finances.filter(f => !(f.id === req.params.id && f.churchId === req.user.churchId));
  if (finances.length === initialLength) {
    return res.status(404).json({ message: 'Not found' });
  }
  save(finances);
  res.status(204).end();
}

module.exports = {
  createFinance,
  getFinances,
  getFinance,
  updateFinance,
  deleteFinance,
};
