import numpy as np

"""
This function is used to define where the input of the current layer goes to next.
We have aggreed to choose sigmoid function for this purpose. But we can change to softmax in the near future
"""
def activationFunction(Z) :
    return 1 / (1 + np.exp(-Z)) # 1 / (1 + e^(-Z))