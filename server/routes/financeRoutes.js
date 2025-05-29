const express = require('express');
const router = express.Router();
const ctrl = require('../controllers/financeController');

router.post('/', ctrl.createFinance);
router.get('/', ctrl.getFinances);
router.get('/:id', ctrl.getFinance);
router.put('/:id', ctrl.updateFinance);
router.delete('/:id', ctrl.deleteFinance);

module.exports = router;
