# [REPAIRED 2026-10-04] joined import lines split in source.
import unittest
import numpy as np
from src.physics_layer import CayleyTreeLindbladSolver
from src.ml_layer import generate_input_state, quantum_convolution_layer, quantum_pooling_layer


class TestPhysicsAndMLLayers(unittest.TestCase):
    def test_lindblad_trace_unity(self):
        solver = CayleyTreeLindbladSolver(generations=1, coordination_number=3)
        ness_state = solver.solve_steady_state_attractor()
        self.assertAlmostEqual(ness_state.tr(), 1.0, places=4)

    def test_qcnn_scale_reduction(self):
        rho_0 = generate_input_state()
        rho_c1 = quantum_convolution_layer(rho_0, 0.35*np.pi, 0.12*np.pi)
        # [REPAIRED 2026-10-04] keep_indices arrived empty; restored to [0, 1].
        rho_p1 = quantum_pooling_layer(rho_c1, keep_indices=[0, 1])
        self.assertEqual(rho_p1.shape, (4, 4))
        self.assertAlmostEqual(rho_p1.tr(), 1.0, places=5)
