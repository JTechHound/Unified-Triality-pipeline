# [REPAIRED 2026-10-04] joined import lines split in source.
import unittest
import numpy as np
from src.manifold_math import AbbyDavisManifoldCalculator


class TestManifoldTopologicalConditions(unittest.TestCase):
    def setUp(self):
        self.calc = AbbyDavisManifoldCalculator()

    def test_minkowski_inequality_compliance(self):
        r = 2.0
        area = 4.0 * np.pi * (r ** 2)
        M = 4.0 * np.pi * r
        check = self.calc.verify_minkowski_inequality(area, M)
        self.assertTrue(check['is_compliant'])

    def test_twenty_one_percent_mass_reduction_lock(self):
        results = self.calc.compute_geometric_mass_optimization(1.0)
        self.assertAlmostEqual(results['efficiency_ratio'], np.pi / 4.0, places=5)
        self.assertAlmostEqual(results['energy_reduction_percent'], 21.46018, places=2)
