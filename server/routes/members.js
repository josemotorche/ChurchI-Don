import { Router } from 'express';
import { authenticate } from '../middleware/auth.js';
import { verifyTenant } from '../middleware/tenant.js';
import {
  createMember,
  getMembers,
  getMember,
  updateMember,
  deleteMember
} from '../controllers/memberController.js';

const router = Router();
router.use(authenticate, verifyTenant);

router.post('/', createMember);
router.get('/', getMembers);
router.get('/:id', getMember);
router.put('/:id', updateMember);
router.delete('/:id', deleteMember);

export default router;
