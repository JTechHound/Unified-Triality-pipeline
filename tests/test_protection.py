import unittest
from src.protection_driver import RotatedSurfaceCodeSimulator


class TestProtectionWrapperHorizons(unittest.TestCase):
    def setUp(self):
        self.simulator = RotatedSurfaceCodeSimulator()

    def test_unprotected_sigmoidal_collapse(self):
        self.assertGreater(self.simulator.evaluate_unprotected_decay(0.02), 0.50)
        self.assertLess(self.simulator.evaluate_unprotected_decay(0.08), 0.10)

    def test_qec_fault_horizon_extension(self):
        raw_val = self.simulator.evaluate_unprotected_decay(0.09)
        qec_val = self.simulator.evaluate_protected_qec_layer(0.09)
        self.assertLess(raw_val, 0.10)
        self.assertGreater(qec_val, 0.70)
