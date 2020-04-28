import numpy as np

def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

print(sigmoidFunction(2.1))
print(sigmoidFunction(-1))