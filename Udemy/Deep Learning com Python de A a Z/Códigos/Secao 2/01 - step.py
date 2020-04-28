import numpy as np

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

print(stepFunction(30))
print(stepFunction(-1))