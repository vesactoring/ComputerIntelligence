import numpy as np


def feedforward(input, weight_layers):
    layer_number = len(weight_layers)
    # input sample data adds bias (one dimentional array)
    input = np.append(input, 1)

    # Each layer, feed-forward
    for layer, weight in enumerate(weight_layers):
        z = sum_up(input, weight)
        input = sigmoid(z)
        if(layer != layer_number - 1):
            input = np.append(input, 1)
    return input

def feedForwardAll(input, weight_layers):
    layer_number = len(weight_layers)
    predictions = []
    for data in input:
        input = np.append(data, 1)
        for layer, weight in enumerate(weight_layers):
            z = sum_up(input, weight)
            input = sigmoid(z)
            if(layer != layer_number - 1):
                input = np.append(input, 1)
        predictions.append(input)
    return predictions




# def cost_function(a2, y):
#     m = y
#     cost = -(1/m)*np.sum(y*np.log(a2))
    
#     return cost

# weights_layer: last layer should not have the bias (one entry less)
def training(train_x, train_y, epoch, learning_rate, weight_layers):
    # each epoch
    for e in range(epoch):
        # each sample data 
        for i, data in enumerate(train_x):
            layer_number = len(weight_layers)
            # input sample data adds bias (one dimentional array)
            input = np.append(data, 1)
            # label for the sample data
            label = train_y[i]
            # layer by layer, wx + b for each neuron in the layer (two dimentional array)
            zs = []
            # layer by layer, the activation value for neurons in the layer (two dimentional array)
            activations = [input]
            

            # Each layer, feed-forward
            for layer, weight in enumerate(weight_layers):
                z = sum_up(input, weight)
                zs.append(z)
                input = sigmoid(z)
                if(layer != layer_number - 1):
                    input = np.append(input, 1)
                activations.append(input)
            # print("THE COST FUNCTION IS: " + str(cost_function(activations, train_y)))

            # backward
            weights_gradients = [np.zeros(w.shape) for w in weight_layers]

            # The last layer
            delta = cost(activations[-1], label) * sigmoid_prime(zs[-1])
            # print(np.shape(activations[-2].reshape(len(activations[-2]),1)))
            weights_gradients[-1] = np.dot(delta.reshape(len(delta), 1), activations[-2].reshape(len(activations[-2]), 1).T)

            # Starting from the last second layer and ,oving forward
            for l in range(2, layer_number):
                # print(np.shape(delta))
                # print(np.shape(weight_layers[-l + 1].transpose()))
                product = np.dot(weight_layers[-l + 1].transpose(), delta)
                delta = product[:-1] * sigmoid_prime(zs[-l])
                weights_gradients[-l] = np.dot(delta.reshape(len(delta), 1), activations[-l-1].reshape(len(activations[-l-1]), 1).transpose())
            
            # print(type(weights_gradients))
            # print(weight_layers)
            weight_layers -= learning_rate * np.array(weights_gradients)

            return weight_layers

def evaluate(test_features, test_labels, weights):
    """Return the number of test inputs for which the neural
    network outputs the correct result. Note that the neural
    network's output is assumed to be the index of whichever
    neuron in the final layer has the highest activation."""
    sum = 0
    for i, data in enumerate(test_features):
        output = feedforward(data, weights)
        prediction = np.argmax(output) + 1
        # print(test_labels[i])
        if(prediction == test_labels[i]):
            sum = sum + 1
    print(sum)
            
        

def sigmoid(z):
    """The sigmoid function."""

    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

def cost(output_activations, y):
    """Return the vector of partial derivatives \partial C_x /
    \partial a for the output activations."""
    return (output_activations-y)

# inputs : a vector (last entry 1 representing the bias)
# weights: a vector
# z = wx + b
# for single neuron
def sum_up(inputs, weights):
    return np.dot(weights, inputs)

def init_layers(sizes):
    num_layers = len(sizes)
    weights = []
    for i, input in enumerate(sizes[:-1]):
        output = sizes[i+1]
        if(i + 1 != num_layers - 1):
            weight = np.random.randn(output-1, input)
        else:
            weight = np.random.randn(output, input)
        weights.append(weight)
    return weights

    def init_weights_from_inputs_to_hidden_layer_neurons(self, hidden_layer_weights):
        weight_num = 0
        for h in range(len(self.hidden_layer.neurons)):
            for i in range(self.num_inputs):
                if not hidden_layer_weights:
                    self.hidden_layer.neurons[h].weights.append(random.random())
                else:
                    self.hidden_layer.neurons[h].weights.append(hidden_layer_weights[weight_num])
                weight_num += 1

    def init_weights_from_hidden_layer_neurons_to_output_layer_neurons(self, output_layer_weights):
        weight_num = 0
        for o in range(len(self.output_layer.neurons)):
            for h in range(len(self.hidden_layer.neurons)):
                if not output_layer_weights:
                    self.output_layer.neurons[o].weights.append(random.random())
                else:
                    self.output_layer.neurons[o].weights.append(output_layer_weights[weight_num])
                weight_num += 1

# layers = init_layers([11,10,9,7])
# # print(layers)
# print(np.shape(layers[2]))

# print(np.random.rand())