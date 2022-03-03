import numpy as np
import matplotlib as plt
class Network(object):

    def __init__(self, sizes, X_train, Y_train, learning_rate, iterations):
        # One input layer, Two hidden layers, One output layer
        self.num_layers = 4
        self.sizes = sizes
        
        self.learning_rate = learning_rate
        self.iterations = iterations
        
        self.parameters = {
            "w1" : np.random.randn(self.sizes[1], self.sizes[0]),
            "b1" : np.zeros((self.sizes[1], 1)),
            "w2" : np.random.randn(self.sizes[2], self.sizes[1]),
            "b2" : np.zeros((self.sizes[2], 1)),
            "w3" : np.random.randn(self.sizes[3], self.sizes[2]),
            "b3" : np.zeros((self.sizes[3], 1)),
        }

        self.X_train = X_train
        self.Y_train = Y_train


    # Activation Functions
    def tanh(self, x):
        return np.tanh(x)

    def softmax(self, x):
        expX = np.exp(x)
        return expX/np.sum(expX, axis = 0)

    def sigmoid(self, z):
        return (1/(1+np.exp(-z)))

    
    # Derivative Activation Functions
    def derivative_sigmoid(self, z):
        return self.sigmoid(z) * (1-self.sigmoid(z))

    def derivative_tanh(self, x):
        return (1 - np.power(np.tanh(x), 2))

    def forward_propagation(self, x):        
        z1 = np.dot(self.parameters["w1"], x) + self.parameters["b1"]
        a1 = self.tanh(z1)

        z2 = np.dot(self.parameters["w2"], a1) + self.parameters["b2"]
        a2 = self.tanh(z2)
        
        z3 = np.dot(self.parameters["w3"], a2) + self.parameters["b3"]
        a3 = self.tanh(z3)
        
        forward_memory = {
            "z1" : z1,
            "a1" : a1,
            "z2" : z2,
            "a2" : a2,
            "z3" : z3,
            "a3" : a3
        }
        
        return forward_memory

    def forward_propagation_static(self, x, parameters):        
        z1 = np.dot(parameters["w1"], x) + parameters["b1"]
        a1 = self.tanh(z1)

        z2 = np.dot(parameters["w2"], a1) + parameters["b2"]
        a2 = self.tanh(z2)
        
        z3 = np.dot(parameters["w3"], a2) + parameters["b3"]
        a3 = self.softmax(z3)
        
        forward_memory = {
            "z1" : z1,
            "a1" : a1,
            "z2" : z2,
            "a2" : a2,
            "z3" : z3,
            "a3" : a3
        }
        
        return forward_memory

        

    # Cost Function: Mean squared error
    def cost_function(self, a3):
        
        n = len(self.Y_train)
        cost = (1/n)*np.sum(np.square(self.Y_train-a3))
        
        return cost

    # Backwards Propagation
    def backward_propagation(self, forward_memory):
        n = self.X_train.shape[1]
        
        dz3 = (forward_memory['a3'] - self.Y_train)
        dw3 = (1/n)*np.dot(dz3, forward_memory['a2'].T)
        db3 = (1/n)*np.sum(dz3, axis = 1, keepdims = True)
        
        dz2 = np.dot(self.parameters['w3'].T, dz3)*self.derivative_tanh(forward_memory['a2'])
        dw2 = (1/n)*np.dot(dz2, forward_memory['a1'].T)
        db2 = (1/n)*np.sum(dz2, axis = 1, keepdims = True)

        dz1 = np.dot(self.parameters['w2'].T, dz2)*self.derivative_tanh(forward_memory['a1'])
        dw1 = (1/n)*np.dot(dz1, self.X_train.T)
        db1 = (1/n)*np.sum(dz1, axis = 1, keepdims = True)
        
        gradients = {
            "dw1" : dw1,
            "db1" : db1,
            "dw2" : dw2,
            "db2" : db2,
            "dw3" : dw3,
            "db3" : db3
        }
        
        return gradients

    # Update Parameters
    def update_parameters(self, gradients):
        self.parameters = {
            "w1" : (self.parameters['w1'] - self.learning_rate*gradients['dw1']),
            "b1" : (self.parameters['b1'] - self.learning_rate*gradients['db1']),
            "w2" : (self.parameters['w2'] - self.learning_rate*gradients['dw2']),
            "b2" : (self.parameters['b2'] - self.learning_rate*gradients['db2']),
            "w3" : (self.parameters['w3'] - self.learning_rate*gradients['dw3']),
            "b3" : (self.parameters['b3'] - self.learning_rate*gradients['db3'])
        }

    # Complete Model
    def model(self):
        cost_list = []
        
        for i in range(self.iterations):
            
            forward_memory = self.forward_propagation(self.X_train)
            
            cost = self.cost_function(forward_memory['a3'])
            
            gradients = self.backward_propagation(forward_memory)
            
            self.update_parameters(gradients)
            
            cost_list.append(cost)
            
        return self.parameters, cost_list

    def accuracy(self, input, target):
        forward_memory = self.forward_propagation(input)
        y_prediction = forward_memory['a3']   
        
        # Get highest probabolity
        y_prediction = np.argmax(y_prediction, 0)
        
        # Get target class
        target = np.argmax(target, 0)
        
        acc = np.mean(y_prediction == target)*100
        
        return acc
