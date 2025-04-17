# TetraCodex

A zero-knowledge cryptographic framework for decentralized trust systems, built with post-quantum security principles.

## Core Modules

- `generate_credential.py` — Generates zero-knowledge voter credentials.
- `post_quantum_crypto.py` — Contains entropy-safe hashing and key generation.
- `simulations/golden_ratio_simulation.py` — Visualizes entropy structures using the Golden Ratio.

## Usage

```bash
python3 generate_credential.py <band_id> <secret>
```

### Example:
```bash
python3 generate_credential.py BlackLake2025 QuantumVision
```

Outputs:
- A unique credential hash
- Timestamp of issuance
