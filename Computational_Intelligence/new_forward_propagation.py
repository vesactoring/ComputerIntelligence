
import numpy as np


def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

# inputs : a vector (last entry 1 representing the bias)
# weights: a vector
def activate(inputs, weights):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    
    return sigmoid(activation)

# weights_hidden_layer: last entry bias
# weights_output_layer: no bias
def training(train_x, train_y, epoch, learning_rate, weights_hidden_layer, weights_output_layer):
    for e in range(epoch):
        for i, data in enumerate(train_x):
            # bias
            input = data.append(1)


            # feedforward



