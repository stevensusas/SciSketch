// MotionPageTransition.tsx
import { FC, ReactNode } from 'react';
import { motion, Variants } from 'framer-motion';

interface MotionPageTransitionProps {
  children: ReactNode; // This type accepts any valid React child (string, number, JSX, array of elements, etc.)
}

const pageTransitionVariants: Variants = {
  initial: {
    opacity: 0,
    // x: '-100vw',
  },
  in: {
    opacity: 1,
    x: 0,
  },
  out: {
    opacity: 0,
    // x: '100vw',
  },
};

const transition = {
  type: 'tween',
  ease: 'anticipate',
  duration: 0.5,
};

const MotionPageTransition: FC<MotionPageTransitionProps> = ({ children }) => (
  <motion.div
    initial="initial"
    animate="in"
    exit="out"
    variants={pageTransitionVariants}
    transition={transition}
  >
    {children}
  </motion.div>
);

export default MotionPageTransition;
