# [REPAIRED 2026-10-04] joined import line split in source.
import numpy as np
import qutip as qt


def generate_input_state():
    """Generates a 3-qubit density matrix representing a local triadic data block."""
    ghz_state = (qt.tensor(qt.basis(2, 0), qt.basis(2, 0), qt.basis(2, 0)) +
                 qt.tensor(qt.basis(2, 1), qt.basis(2, 1), qt.basis(2, 1))).unit()
    return qt.ket2dm(ghz_state)


def quantum_convolution_layer(rho, theta, phi):
    """Applies shift-invariant multi-qubit entangling filters: U = exp(-i*[theta*XXI + phi*ZZI])."""
    XXI = qt.tensor(qt.sigmax(), qt.sigmax(), qt.identity(2))
    ZZI = qt.tensor(qt.sigmaz(), qt.sigmaz(), qt.identity(2))

    H_local = theta * XXI + phi * ZZI
    U_local = (-1j * H_local).expm()
    return U_local * rho * U_local.dag()


# [REPAIRED 2026-10-04] keep_indices arrived as a bare "keep_indices=" (SyntaxError);
# restored to [0, 1]: 3 qubits -> keep 2 -> 4x4 output, matching test_physics.
def quantum_pooling_layer(rho_conv, keep_indices=[0, 1]):
    """Executes scale reduction via partial trace over peripheral nodes."""
    return rho_conv.ptrace(keep_indices)
