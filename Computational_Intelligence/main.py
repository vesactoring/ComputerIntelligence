import numpy as np
import format as format

def numPyPlay():
    print(np.array([0,2,3,4]))

# def testReader():
#     print(format.readFeatures("./data/features.txt"))
# testReader()

param_values = {}
param_values["W" + str(2)] = "Khoa"

def testDictionary():
    print(param_values["W" + "2"])

testDictionary()


"""
This function is used to define where the input of the current layer goes to next.
We have aggreed to choose sigmoid function for this purpose. But we can change to softmax in the near future
"""
def activationFunction(Z) :
    return 1 / (1 + np.exp(-Z)) # 1 / (1 + e^(-Z))


def forwardOneLayer(prevA, currW, currB) :
    currZ = np.dot(currW, prevA) + currB
        
    return activationFunction(currZ), currZ

def forwardAllLayers(X, params_values, nn_architecture):
    memory = {}
    A_curr = X
    
    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        A_prev = A_curr
        
        print(layer)
        activ_function_curr = layer["activation"]
        W_curr = params_values["W" + str(layer_idx)]
        b_curr = params_values["b" + str(layer_idx)]
        A_curr, Z_curr = forwardOneLayer(A_prev, W_curr, b_curr)
        
        memory["A" + str(idx)] = A_prev
        memory["Z" + str(layer_idx)] = Z_curr
       
    return A_curr, memory

nn_architecture = [
    {"input_dim": 10, "output_dim": 9, "activation": "sigmoid"},
    {"input_dim": 9, "output_dim": 8, "activation": "sigmoid"},
    {"input_dim": 8, "output_dim": 7, "activation": "sigmoid"},
]

def init_layers(nn_architecture, seed = 99):
    np.random.seed(seed)
    number_of_layers = len(nn_architecture)
    params_values = {}

    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        layer_input_size = layer["input_dim"]
        layer_output_size = layer["output_dim"]
        
        params_values['W' + str(layer_idx)] = np.random.randn(
            layer_output_size, layer_input_size) * 0.1
        params_values['b' + str(layer_idx)] = np.random.randn(
            layer_output_size, 1) * 0.1
        
    return params_values
    
def testForward():
    param_values = init_layers(nn_architecture, 99)
    for i in format.readFeatures("./data/features.txt"):
        print(forwardAllLayers(i, param_values, nn_architecture))

testForward()
