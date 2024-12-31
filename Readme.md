# Measuring Quantum Superposition

Measures a quantum superposition state 1000 times and visualizes the distribution.

## Requirements
```
pennylane>=0.19.0
numpy>=1.19.0
matplotlib>=3.3.0
```

## Implementation
1. Creates superposition using Hadamard gate
2. Performs 1000 measurements
3. Plots distribution of outcomes
4. Saves plot as 'superposition_measurements.png'

## Expected Output
- Approximately 500 measurements in |0⟩ state
- Approximately 500 measurements in |1⟩ state
- Bar plot showing measurement distribution

## Usage
```python
python measure_superposition.py
```