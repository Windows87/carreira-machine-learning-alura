import numpy as np

def softmax(x):
    ex = np.exp(x)
    return ex / ex.sum()

valores = [5, 2, 1.3]

print(softmax(valores))