import { Router } from 'express';
import { authenticate, verifyChurch } from '../middleware/auth.js';
import { createMember, getMembers, getMemberById, updateMember, deleteMember } from '../controllers/memberController.js';

const router = Router();

router.use(authenticate, verifyChurch);

router.post('/', createMember);
router.get('/', getMembers);
router.get('/:id', getMemberById);
router.put('/:id', updateMember);
router.delete('/:id', deleteMember);

export default router;
