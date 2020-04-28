import numpy as np

def hyperbolicFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

print(hyperbolicFunction(2.1))
print(hyperbolicFunction(-1))