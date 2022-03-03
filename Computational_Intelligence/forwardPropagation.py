import numpy as np
import activation as activ

def forwardOneLayer(prevA, currW, currB) :
    currZ = np.dot(currW, prevA) + currB
        
    return activ.activationFunction(currZ), currZ

def forwardAllLayers(X, paramValues, neuralNetWorkArchitecture):
    memory = {}
    A_curr = X
    
    for idx, layer in enumerate(neuralNetWorkArchitecture):
        layer_idx = idx + 1
        A_prev = A_curr
        
        print(layer)
        activ_function_curr = layer["activation"]
        W_curr = paramValues["W" + str(layer_idx)]
        b_curr = paramValues["b" + str(layer_idx)]
        A_curr, Z_curr = forwardOneLayer(A_prev, W_curr, b_curr)
        
        memory["A" + str(idx)] = A_prev
        memory["Z" + str(layer_idx)] = Z_curr
       
    return A_curr, memory
