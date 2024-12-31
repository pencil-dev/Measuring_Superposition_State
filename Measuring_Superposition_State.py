import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt

# Create quantum device
dev = qml.device('default.qubit', wires=1, shots=1)

@qml.qnode(dev)
def superposition_circuit():
    # Create superposition with Hadamard
    qml.Hadamard(wires=0)
    return qml.sample(qml.PauliZ(0))

# Collect measurements
n_measurements = 1000
results = []
for _ in range(n_measurements):
    measurement = superposition_circuit()
    results.append(measurement)

# Convert measurements to binary outcomes (0 or 1)
# PauliZ eigenvalues are +1 (|0⟩) and -1 (|1⟩)
binary_results = [(1 - x) // 2 for x in results]

# Count occurrences
counts = {0: binary_results.count(0), 1: binary_results.count(1)}

# Plot results
plt.figure(figsize=(8, 6))
plt.bar(['|0⟩', '|1⟩'], [counts[0], counts[1]])
plt.title('Measurement Results of Superposition State')
plt.xlabel('Basis State')
plt.ylabel('Count (out of 1000)')
plt.savefig('superposition_measurements.png')
plt.close()

print(f"Measurements in |0⟩: {counts[0]}")
print(f"Measurements in |1⟩: {counts[1]}")