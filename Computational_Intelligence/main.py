import numpy as np
from single_perceptron import plot

if __name__ == '__main__':
    label_and = np.array([0, 0, 0, 1])
    label_or = np.array([0, 1, 1, 1])
    label_xor = np.array([0, 1, 1, 0])

    max_epoch = 10
    
    plot = plot(max_epoch, label_xor)
    