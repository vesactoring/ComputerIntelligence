import numpy as np

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        # Bias for each neuron, excluding the input neurons
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) 
                        for x, y in zip(sizes[:-1], sizes[1:])]
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))
    
    def softmax(self, z):
        eZi = np.exp(z - np.max(z))
        return eZi / eZi.sum()

    def sigmoid_prime(self, z):
        return self.sigmoid(z)*(1-self.sigmoid(z))

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            # print(np.shape(w))
            # print(np.shape(b))
            array = np.add(np.dot(w, a), b)
            a = self.sigmoid(array)
        return a

    def fit(self, training_data, target, epochs, mini_batch_size, eta):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        n = len(training_data)
        for j in range(epochs):
            mini_batches_data = np.array_split(training_data, n/mini_batch_size)
            mini_batches_y = np.array_split(target, n/mini_batch_size)
            for mini_batch in mini_batches_data:
                self.update_mini_batch(mini_batches_data, mini_batches_y, eta)
    
    def update_mini_batch(self, mini_batch_data, mini_batches_y, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``mini_batch`` is a list of tuples ``(x, y)``, and ``eta``
        is the learning rate."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for i, x in enumerate(mini_batch_data):
            delta_nabla_b, delta_nabla_w = self.backprop(x, mini_batches_y[i])
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)] 
        self.weights = [w-(eta/len(mini_batch_data))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        # print(np.shape(self.biases[0]))
        print(" before change")
        # print(np.shape(nabla_b[0]))
        self.biases = [b-(eta/len(mini_batch_data))*nb
                       for b, nb in zip(self.biases, nabla_b)]
        # print(np.shape(self.biases[0]))
        print("change after")


    # x: mini batch datas with feataures, y: mini batch datas with labels.
    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        # print(np.shape(x))
        # print(np.shape(x.T))
        print(np.shape(activations[0]))
        activations[0] = activations[0].T
        print("djksbk")
        print(np.shape(activations[0]))
        for index, (b, w) in enumerate(zip(self.biases, self.weights)):
            z = np.dot(w, activation[0])+b
            zs.append(z)
            if(index == self.num_layers):
                activation = self.softmax(z)
            else:
                activation = self.sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * \
            self.sigmoid_prime(zs[-1])
        print(np.shape(activations[-1]))
        print(np.shape(zs[-1]))
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].T)

        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = self.sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].T)
        return (nabla_b, nabla_w)

    def evaluate(self, test_features, test_labels):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        sum = 0
        for i, data in enumerate(test_features):
            # print(np.shape(data))
            output = self.feedforward(data)
            prediction = np.argmax(output) + 1
            if(prediction == test_labels[i]):
                sum = sum + 1
        return sum/len(test_features)


    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)