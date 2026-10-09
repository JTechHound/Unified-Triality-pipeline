# Unified-Triality-pipeline

Public build of the **Unified Triality Pipeline** (v2 spec reconstruction):
quantum-coherence simulation modules, the Abby Davis Manifold calculator,
ML and physics layers, protection and verification drivers, plus the
computed D4 triality theory and the guard mechanisms.

# Authors - Arthur Leroy Jones
# Author UCT Theory - Mikey-506
# Independent Researcher - Abby Davis

- **Classification:** Advanced Non-Equilibrium Open Quantum Systems
- **License:** Apache 2.0 (see LICENSE)
- **Status:** v2 build validated (4/5 test files pass; see Validation note)

## What this is

The v2 spec reconstruction of the Unified Triality Pipeline: executable
modules for manifold math, machine-learning and physics layers, hardware
protection, and verification — assembled from the v2 source documents with
every transmission repair tagged inline. Ships with `setup.py` for install
and a hardware-calibration config block.

## Repository structure

```
Unified-Triality-pipeline/
├── triality_unification_core.py  # Unification core entry point
├── qml_convergence_visualizer.py # QML convergence visualization
├── TRIALITY_3_WRITEUP.md         # The computed "3" of 3-6-9 (D4 triality write-up)
├── GUARDS_WRITEUP.md             # CoherenceGuard + GoodhartGuard write-up
├── requirements.txt
├── setup.py
├── config/                       # Hardware-calibration config
├── tests/                        # Test suite (incl. test_manifold.py)
└── src/
    ├── __init__.py
    ├── manifold_math.py          # Abby Davis Manifold calculator: Minkowski
    │                             # check, spherical vs flat-faced mass
    │                             # optimization, rim tension
    ├── ml_layer.py               # Machine-learning layer
    ├── physics_layer.py          # Physics layer
    ├── protection_driver.py      # Hardware protection driver
    ├── verification_driver.py    # Verification driver
    ├── triality_automorphism.py  # S3 outer automorphism of D4, computed:
    │                             # 8v/8s/8c permuted 8v → 8c → 8s → 8v
    ├── visualize_triality.py     # Renders the triality figure
    └── guards.py                 # CoherenceGuard + GoodhartGuard
```

## The triality theory

`triality_automorphism.py` makes the "3" of 3-6-9 explicit and computable:
the three phases are the three 8-dimensional representations of Spin(8) —
vector (8v), spinor (8s), conjugate spinor (8c) — permuted by the S3 outer
automorphism of D4. All checks pass; see `TRIALITY_3_WRITEUP.md`.

## The guards

`guards.py` implements two watchers for self-optimizing systems (concepts
from Mikey's Sophia stack, implementations new):

- **CoherenceGuard** — phase-lock integrity: phase deviation, lock erosion,
  winding-number check (discrete DμC = 0)
- **GoodhartGuard** — rejects optimizer actions that improve the primary
  metric by degrading guard metrics ("when a measure becomes a target, it
  ceases to be a good measure," enforced in code)

## Quickstart

```bash
git clone https://github.com/JTechHound/Unified-Triality-pipeline.git
cd Unified-Triality-pipeline
pip install -r requirements.txt
python3 -m pytest tests/ -x -q
python3 src/triality_automorphism.py
python3 src/guards.py
```

## Validation note

4 of 5 test files pass, including the manifold tests. One known
spec/test mismatch is left open rather than papered over:
`test_unprotected_sigmoidal_collapse` expects collapse below 0.10 at 8%
noise; the code produces 0.10525. The discrepancy is recorded, not hidden.
