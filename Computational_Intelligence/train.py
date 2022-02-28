import numpy as np
import forward_propagation as fp
import backward_propagation as bp
import architecture as arch

def update(params_values, grads_values, nn_architecture, learning_rate):
    for layer_idx, layer in enumerate(nn_architecture):
        params_values["W" + str(layer_idx)] -= learning_rate * grads_values["dW" + str(layer_idx)]        
        params_values["b" + str(layer_idx)] -= learning_rate * grads_values["db" + str(layer_idx)]

    return params_values;


def train(X, Y, nn_architecture, epochs, learning_rate, params_values):
    
    for i in range(epochs):
        Y_hat, cashe = fp.forwardAllLayers(X, params_values, nn_architecture)
        
        grads_values = bp.backwardAllLayers(Y_hat, Y, cashe, params_values, nn_architecture)
        params_values = update(params_values, grads_values, nn_architecture, learning_rate)
        
    return params_values