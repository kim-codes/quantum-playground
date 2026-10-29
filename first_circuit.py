import pennylane as qml

# create simulator with one qubit
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def circuit():
    # put qubit into an equal superposition
    qml.Hadamard(wires=0)

    # return probabilities of measuring 0 or 1
    return qml.probs(wires=0)

print("Measurement probabilities:", circuit())
