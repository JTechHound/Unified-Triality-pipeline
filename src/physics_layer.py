# [REPAIRED 2026-10-04] joined import line split ("import numpy as npimport qutip as qt" in source).
import numpy as np
import qutip as qt


class CayleyTreeLindbladSolver:
    """
    Solves the time-dependent driven Lindblad equation across a self-similar,
    hierarchical neural Cayley Tree matrix using collective spin density operators.
    """
    def __init__(self, generations=2, coordination_number=3, omega_0=1.0, omega_drive=2.5, J=0.4, kappa=0.08):
        self.g = generations
        self.z = coordination_number
        self.omega_0 = omega_0
        self.omega_drive = omega_drive
        self.J = J
        self.kappa = kappa

        self.num_nodes = 1 + self.z * sum((self.z - 1)**n for n in range(self.g))
        self.S_dim = 2

    def _build_collective_operators(self):
        self.Sx_list = []
        self.Sz_list = []
        self.Sm_list = []

        for i in range(self.num_nodes):
            op_list = [qt.identity(self.S_dim)] * self.num_nodes

            op_list[i] = 0.5 * qt.sigmax()
            self.Sx_list.append(qt.tensor(op_list))

            op_list[i] = 0.5 * qt.sigmaz()
            self.Sz_list.append(qt.tensor(op_list))

            op_list[i] = qt.sigmam()
            self.Sm_list.append(qt.tensor(op_list))

    def _generate_tree_adjacency(self):
        self.edges = []
        current_node = 0
        # [REPAIRED 2026-10-04] line arrived truncated as bare "nodes_in_gen =";
        # restored to the generation-0 seed [1] (matches v1 spec + tree math).
        nodes_in_gen = [1]

        next_avail = 1
        for gen in range(self.g):
            new_gen_count = 0
            for node in range(current_node, current_node + nodes_in_gen[-1]):
                branches = self.z if node == 0 else (self.z - 1)
                for _ in range(branches):
                    if next_avail < self.num_nodes:
                        self.edges.append((node, next_avail))
                        next_avail += 1
                        new_gen_count += 1
            current_node += nodes_in_gen[-1]
            nodes_in_gen.append(new_gen_count)

    def solve_steady_state_attractor(self, t_max=10, steps=200):
        self._build_collective_operators()
        self._generate_tree_adjacency()

        H_interaction = sum(self.J * self.Sz_list[i] * self.Sz_list[j] for i, j in self.edges)
        H_driving_base = sum(self.omega_0 * sx for sx in self.Sx_list)

        def drive_coeff(t, args):
            return np.cos(args['omega_d'] * t)

        H_total = [H_interaction, [H_driving_base, drive_coeff]]

        S_scale = (3.0 * self.num_nodes) / 2.0
        c_ops = [np.sqrt(self.kappa / S_scale) * self.Sm_list[i] for i in range(self.num_nodes)]

        t_list = np.linspace(0, t_max, steps)
        initial_state = qt.tensor([qt.basis(self.S_dim, 0)] * self.num_nodes)
        rho_initial = qt.ket2dm(initial_state)

        # [REPAIRED 2026-10-04] qt.Options was removed in qutip 5.x (AttributeError
        # under the declared qutip>=4.7.1 range); plain dict works on 4.7 and 5.x.
        result = qt.mesolve(
            H_total, rho_initial, t_list, c_ops,
            args={'omega_d': self.omega_drive},
            options={"store_states": True}
        )
        return result.states[-1]
