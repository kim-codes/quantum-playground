
import pennylane as qml

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=0)  # add a second Hamard gate to the same qubit

    return qml.probs(wires=0)

print("Measurement probabilities:", circuit())
