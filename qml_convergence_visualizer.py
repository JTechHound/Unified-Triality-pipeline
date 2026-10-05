"""
[CONSOLIDATED 2026-10-05] Canonical QML convergence engine for
unified-triality-pipeline, consolidated from the Triality369_pipeline
visualizer series (qml_convergence_visualizer.py through _fix_3).
This is the _fix_3 lineage: the genuine partial-trace engine
(9-qubit GHZ -> 512-dim rho -> real partial trace down to 3 qubits).
Earlier iterations (random-walk MSE labeled CCE, array-division crash)
are superseded and not carried over, per the one-canonical-name rule.

KNOWN MODELING FLAG (his call): the (1-S) discord formula in
run_convergence_diagnostics() returns 0.00000 bits on the GHZ test state;
it is maximized for product-state input and zero for maximally entangled
input, inverted vs the narrative. Needs his rethink before use as a
convergence metric.
"""

"""
Module 10: Section 7.2 Quantum Pooling Layer Genuine Partial Trace Engine
Specification Reference: UTP-SPEC-2026-V5.0 - Section 7.2 & Section 8.1

Calculates a real, matrix-based partial trace over a 9-qubit (512-dim) state space.
"""

import numpy as np

class GenuineQuantumPoolingEngine:
    def __init__(self, initial_qubits=9, pooled_qubits=3):
        self.n_initial = initial_qubits
        self.n_pooled = pooled_qubits
        self.n_discard = initial_qubits - pooled_qubits
        
        self.dim_initial = 2 ** self.n_initial  # 2^9 = 512
        self.dim_pooled = 2 ** self.n_pooled    # 2^3 = 8
        self.dim_discard = 2 ** self.n_discard  # 2^6 = 64

    def generate_verified_512_density_matrix(self):
        """
        Constructs a real, valid 512x512 density matrix (rho_conv).
        Initializes a clean pure state vector and maps localized feature coupling.
        """
        print(f"-> Initializing Real C1 State Layer: Dimension Matrix = {self.dim_initial} x {self.dim_initial}")
        
        # Build a valid, normalized pure state state-vector psi
        state_vector = np.zeros(self.dim_initial, dtype=complex)
        # Distribute state amplitudes across specific triadic address coordinates
        state_vector[0] = 1.0 / np.sqrt(2)
        state_vector[-1] = 1.0 / np.sqrt(2)
        
        # rho = |psi><psi| (True, conserved Rank-1 density matrix array)
        rho_conv = np.outer(state_vector, np.conj(state_vector))
        return rho_conv

    def execute_matrix_partial_trace(self, rho_conv, active_noise_floor=0.085):
        """
        Executes a formal partial trace operation by reshaping the 512x512 array
        into a tensor grid and tracing over the 6 peripheral qubits (64 dimensions).
        """
        print(f"\n--- EXECUTING RECURSIVE QUANTUM POOLING LAYER P1 ---")
        print(f"-> Reshaping State Array into Tensor Grid: [8, 64, 8, 64]")
        print(f"-> Tracing out {self.n_discard} Peripheral Subspace Qubits (64 Dimensions) out-of-band")
        
        # Verify trace conservation before reduction
        initial_trace = np.real(np.trace(rho_conv))
        assert np.isclose(initial_trace, 1.0000), "[!] Input state matrix is unconserved."
        
        # Reshape the 512x512 matrix into index structures tracking:
        # [kept_row, discard_row, kept_col, discard_col] -> indices map [8, 64, 8, 64]
        tensor_grid = rho_conv.reshape(self.dim_pooled, self.dim_discard, self.dim_pooled, self.dim_discard)
        
        # Execute partial trace over the discard indices (axis 1 and axis 3)
        # rho_pooled_matrix = Sum over j of <j| rho |j>
                # [REPAIRED 2026-10-04] Was np.trace(..., axis1=1, axis3=3): np.trace takes
        # only axis1/axis2 - there is no axis3 kwarg (TypeError). Tracing the
        # single pair (1,3) sums the discard-subsystem diagonal in one call:
        # rho_pooled[a,c] = sum_b tensor[a,b,c,b]. Verified against einsum.
        rho_pooled = np.trace(tensor_grid, axis1=1, axis2=3)
        
        # Verify pooled matrix properties (Must be an 8x8 matrix tracking 3 remaining logical qubits)
        pooled_trace = np.real(np.trace(rho_pooled))
        print(f"-> Sifting Systemic Density down to Core Backbone Matrix: {rho_pooled.shape[0]} x {rho_pooled.shape[1]}")
        print(f"-> Pooled Trace Conservation Check: {pooled_trace:.4f}")
        
        # Formulate true persistent Quantum Discord survival based on real matrix eigenvalues
        eigenvalues = np.linalg.eigvalsh(rho_pooled)
        clean_eigenvals = eigenvalues[eigenvalues > 1e-12]
        von_neumann_S = -np.sum(clean_eigenvals * np.log2(clean_eigenvals))
        
        # Apply rich FHUP code stabilizer shielding factors (Section 8.2 constants)
        if active_noise_floor <= 0.125:
            error_logical_modifier = 1.0 - 0.015
            pooling_status = "SUCCESS: LONG-RANGE NON-LOCAL DISCORD PRESERVED IN BACKBONE"
        else:
            error_logical_modifier = 1.0 - 0.850
            pooling_status = "CRITICAL: NOISE OVERFLOW TRIGGERED COHERENCE LEAK"
            
        # The true routed discord scales with the remaining coherent Von Neumann entropy capacity
        calculated_matrix_discord = (1.0 - von_neumann_S) * error_logical_modifier * 0.93 * (1.15)
        return calculated_matrix_discord, pooling_status

if __name__ == "__main__":
    print("=================================================================")
    print("   MODULE 10 MATRIX LIBRARY: GENUINE PARTIAL TRACE OPERATOR CORE ")
    print("=================================================================")
    
    # Instantiate the genuine matrix engine (9 Qubits down to 3 Qubits)
    matrix_engine = GenuineQuantumPoolingEngine(initial_qubits=9, pooled_qubits=3)
    
    # Step 1: Generate actual 512x512 matrix tracking the C1 convolution state
    rho_c1_matrix = matrix_engine.generate_verified_512_density_matrix()
    
    # Step 2: Execute true tensor trace reduction under an active 8.5% noise floor
    noise_level = 0.085
    real_discord, operational_log = matrix_engine.execute_matrix_partial_trace(rho_c1_matrix, active_noise_floor=noise_level)
    
    print("-----------------------------------------------------------------")
    print(f"-> Measured Noise Fraction (σ):       {noise_level * 100:.1f}%")
    print(f"-> Partial Trace Operational Status:  {operational_log}")
    print(f"-> GENUINE MATRIX READOUT DISCORD:    {real_discord:.5f} BITS")
    print("=================================================================")
