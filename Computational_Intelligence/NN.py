import numpy as np
import matplotlib.pyplot as plt

data_features = np.genfromtxt("data/features.txt", delimiter=",")
data_targets = np.genfromtxt("data/targets.txt", delimiter=",")

X_train = []
Y_train = []

X_validation = []
Y_validation = []

X_test = []
Y_test = []

n = len(data_features)
for i in range(n):
    label = np.zeros((1,7))
    label[:, int(data_targets[i]) - 1] = 1
    label = label.flatten()
    if(i <= n*0.65):
        X_train.append(data_features[i])
        Y_train.append(label)
    elif(i > n*0.65 and i <= n*0.8):
        X_validation.append(data_features[i])
        Y_validation.append(label)
    else:
        X_test.append(data_features[i])
        Y_test.append(label)

X_train = np.transpose(X_train)
Y_train = np.transpose(Y_train)

X_validation = np.transpose(X_validation)
Y_validation = np.transpose(Y_validation)

X_test = np.transpose(X_test)
Y_test = np.transpose(Y_test)


# Activation Functions
def tanh(x):
    return np.tanh(x)

def softmax(x):
    expX = np.exp(x)
    return expX/np.sum(expX, axis = 0)

def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))

# Derivative Activation Functions
def derivative_tanh(x):
    return (1 - np.power(np.tanh(x), 2))

def derivative_sigmoid(z):
    return sigmoid(z)*(1-sigmoid(z))



# Initialize Parameters
# n_x: amount of neurons in input layer
# n_h: amount of neurons in hidden layer
# n_y: amount of neurons in output layer
def initialize_parameters(n_x, n_h, n_y):
    w1 = np.random.randn(n_h, n_x)*0.01
    b1 = np.zeros((n_h, 1))
    
    w2 = np.random.randn(n_y, n_h)*0.01
    b2 = np.zeros((n_y, 1))
    
    parameters = {
        "w1" : w1,
        "b1" : b1,
        "w2" : w2,
        "b2" : b2
    }
    
    return parameters



# Forward Propagation
def forward_propagation(x, parameters):
    
    w1 = parameters['w1']
    b1 = parameters['b1']
    w2 = parameters['w2']
    b2 = parameters['b2']
    
    z1 = np.dot(w1, x) + b1
    a1 = tanh(z1)
    
    z2 = np.dot(w2, a1) + b2
    a2 = softmax(z2)
    
    forward_cache = {
        "z1" : z1,
        "a1" : a1,
        "z2" : z2,
        "a2" : a2
    }
    
    return forward_cache




# Cost Function
def cost_function(a2, y):
    m = y.shape[1]
    cost = -(1/m)*np.sum(y*np.log(a2))
    
    return cost




# Backwards Propagation
def backward_prop(x, y, parameters, forward_cache):
    
    w1 = parameters['w1']
    b1 = parameters['b1']
    w2 = parameters['w2']
    b2 = parameters['b2']
    
    a1 = forward_cache['a1']
    a2 = forward_cache['a2']
    
    m = x.shape[1]
    
    dz2 = (a2 - y)
    dw2 = (1/m)*np.dot(dz2, a1.T)
    db2 = (1/m)*np.sum(dz2, axis = 1, keepdims = True)
    
    dz1 = (1/m)*np.dot(w2.T, dz2)*derivative_tanh(a1)
    dw1 = (1/m)*np.dot(dz1, x.T)
    db1 = (1/m)*np.sum(dz1, axis = 1, keepdims = True)
    
    gradients = {
        "dw1" : dw1,
        "db1" : db1,
        "dw2" : dw2,
        "db2" : db2
    }
    
    return gradients




# Update Parameters
def update_parameters(parameters, gradients, learning_rate):
    
    w1 = parameters['w1']
    b1 = parameters['b1']
    w2 = parameters['w2']
    b2 = parameters['b2']
    
    dw1 = gradients['dw1']
    db1 = gradients['db1']
    dw2 = gradients['dw2']
    db2 = gradients['db2']
    
    w1 = w1 - learning_rate*dw1
    b1 = b1 - learning_rate*db1
    w2 = w2 - learning_rate*dw2
    b2 = b2 - learning_rate*db2
    
    parameters = {
        "w1" : w1,
        "b1" : b1,
        "w2" : w2,
        "b2" : b2
    }
    
    return parameters



# Complete Model
# n_h: amount of neurons in hidden layers
def model(x, y, n_h, learning_rate, iterations):
    
    n_x = x.shape[0]
    n_y = y.shape[0]
    
    cost_list = []
    
    parameters = initialize_parameters(n_x, n_h, n_y)
    
    for i in range(iterations):
        
        forward_cache = forward_propagation(x, parameters)
        
        cost = cost_function(forward_cache['a2'], y)
        
        gradients = backward_prop(x, y, parameters, forward_cache)
        
        parameters = update_parameters(parameters, gradients, learning_rate)
        
        cost_list.append(cost)
        
        if(i%(iterations/10) == 0):
            print("Cost after", i, "iterations is :", cost)
        
    return parameters, cost_list



# Test
iterations = 100
n_h = 1000
learning_rate = 0.5
Parameters, Cost_list = model(X_train, Y_train, n_h = n_h, learning_rate = learning_rate, iterations = iterations)

forward_cache = forward_propagation(X_train, Parameters)
a_out = forward_cache["a2"]
a_out = np.argmax(a_out, axis = 0)
y_out = np.argmax(Y_train, axis = 0)
acc = np.mean(a_out == y_out)*100
print(acc)
