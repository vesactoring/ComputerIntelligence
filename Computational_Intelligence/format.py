import numpy as np

def readFeatures(path):
    return np.genfromtxt(path, delimiter=",")

