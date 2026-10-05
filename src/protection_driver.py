import numpy as np


class RotatedSurfaceCodeSimulator:
    """
    Simulates a Distance-3 Rotated Surface Code lattice mapping 9 Data Qubits
    against interleaved Plaquette Ancillas to actively shift the fault-tolerant knee.
    """
    def __init__(self):
        self.sigma_threshold_raw = 0.05
        self.sigma_threshold_qec = 0.125
        self.base_discord = 0.74100
        self.noise_floor = 0.00014
        self.beta_raw = 60.0
        self.beta_qec = 45.0

    def evaluate_unprotected_decay(self, sigma):
        overflow_delta = sigma - self.sigma_threshold_raw
        coherence_tracking = 1.0 / (1.0 + np.exp(self.beta_raw * overflow_delta))
        return (self.base_discord * coherence_tracking) + self.noise_floor

    # [RECONSTRUCTED 2026-10-04] The stabilizer index mapping was stripped in
    # transmission: s1..s4 arrived as `physical_errors ^ physical_errors ^
    # physical_errors ^ physical_errors` with no indices, `corrections = True`
    # assigned a scalar to a 9-element array, and `if s1` tested a whole
    # array (raises ValueError: ambiguous truth value) -- the method could
    # not run as received. Rebuilt on the verified [[9,1,3]] plaquette set
    # from src/surface_code_decoder.py (Triality-Pipeline-, verified
    # 2026-10-02: all X/Z stabilizers commute, unique single-qubit
    # syndromes, combined rank 8):
    #   X1=[0,1,3,4], X2=[1,2,4,5], X3=[3,4,6,7], X4=[4,5,7,8]
    # Single Z errors are corrected by exact syndrome lookup; the logical
    # Z operator is Z0 Z3 Z6 (left column -- verified even overlap with
    # every X stabilizer, weight 3 = code distance).
    def _simulate_d3_lattice_errors(self, sigma):
        plaquettes = ([0, 1, 3, 4], [1, 2, 4, 5], [3, 4, 6, 7], [4, 5, 7, 8])
        syndrome_table = {}
        for q in range(9):
            syn = tuple(1 if q in p else 0 for p in plaquettes)
            syndrome_table[syn] = q

        trials = 500
        logical_failures = 0
        for _ in range(trials):
            physical_errors = np.random.random(9) < sigma
            s = tuple(
                int(physical_errors[p[0]] ^ physical_errors[p[1]]
                    ^ physical_errors[p[2]] ^ physical_errors[p[3]])
                for p in plaquettes
            )

            corrections = np.zeros(9, dtype=bool)
            if any(s) and s in syndrome_table:
                corrections[syndrome_table[s]] = True

            final_state = physical_errors ^ corrections
            logical_z_error = final_state[0] ^ final_state[3] ^ final_state[6]
            if logical_z_error:
                logical_failures += 1
        return logical_failures / trials

    def evaluate_protected_qec_layer(self, sigma):
        if sigma <= self.sigma_threshold_qec:
            zne_sharpening_gain = 1.0377
            lattice_leak = self._simulate_d3_lattice_errors(sigma) * 0.02
            return min(1.0, (self.base_discord * zne_sharpening_gain) - lattice_leak)
        else:
            overflow_delta = sigma - self.sigma_threshold_qec
            coherence_tracking = 1.0 / (1.0 + np.exp(self.beta_qec * overflow_delta))
            return (self.base_discord * coherence_tracking) + self.noise_floor
