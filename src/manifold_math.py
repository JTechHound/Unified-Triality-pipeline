import numpy as np


class AbbyDavisManifoldCalculator:
    """
    Calculates the topological boundary conditions, geometric mass-energy optimizations,
    and line densities of the Abby Davis Flat-Faced Manifold Node compared to standard
    spherical topologies using Minkowski's inequality limits.
    """
    def __init__(self, c=299792458.0, G=6.67430e-11):
        self.c = c
        self.G = G

    def verify_minkowski_inequality(self, area, total_mean_curvature_M):
        """Validates the strict Minkowski bounding condition: M^2 >= 4 * pi * A"""
        minkowski_lhs = total_mean_curvature_M ** 2
        minkowski_rhs = 4.0 * np.pi * area
        is_compliant = minkowski_lhs >= minkowski_rhs
        margin = minkowski_lhs - minkowski_rhs

        return {
            "M_squared": minkowski_lhs,
            "four_pi_A": minkowski_rhs,
            "is_compliant": bool(is_compliant),
            "inequality_margin": margin
        }

    def compute_geometric_mass_optimization(self, aperture_radius_R):
        """Calculates mass-energy requirements comparing spherical vs flat-faced shapes."""
        mass_spherical = (2.0 * aperture_radius_R * (self.c ** 2)) / self.G
        mass_flat_faced = (np.pi * (self.c ** 2) * aperture_radius_R) / (2.0 * self.G)

        efficiency_factor = mass_flat_faced / mass_spherical
        mass_reduction_percentage = (1.0 - efficiency_factor) * 100.0

        return {
            "aperture_radius_meters": aperture_radius_R,
            "spherical_mass_kg": mass_spherical,
            "flat_faced_mass_kg": mass_flat_faced,
            "efficiency_ratio": efficiency_factor,
            "energy_reduction_percent": mass_reduction_percentage
        }

    def calculate_distributional_rim_tension(self):
        """Calculates critical cosmic string line tension concentrated along the rim: lambda = -c^4 / 4G"""
        return - (self.c ** 4) / (4.0 * self.G)
