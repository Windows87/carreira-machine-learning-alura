import numpy as np

def relu(soma):
    if(soma >= 0):
        return soma
    return 0

print(relu(2.1))
print(relu(-1))