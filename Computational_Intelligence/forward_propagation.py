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

   

    def fit(self, mini_batch, mini_batch_y, epochs, mini_batch_size, eta):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        n = len(mini_batch)
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        delta_nabla_b, delta_nabla_w = self.backprop(mini_batch, mini_batch_y)
        nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
        nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)] 
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
        for i in range(1, self.num_layers):
            sizu = np.shape(self.biases[-i])[1]
            sum = self.biases[-i].sum(axis = 1)
            average = sum / sizu
            self.biases[-i] = average.reshape(len(sum), 1)
    # def update_mini_batch(self, mini_batch, mini_batch_y, eta):
    #     """Update the network's weights and biases by applying
    #     gradient descent using backpropagation to a single mini batch.
    #     The ``mini_batch`` is a list of tuples ``(x, y)``, and ``eta``
    #     is the learning rate."""
    #     nabla_b = [np.zeros(b.shape) for b in self.biases]
    #     nabla_w = [np.zeros(w.shape) for w in self.weights]
    #     delta_nabla_b, delta_nabla_w = self.backprop(mini_batch, mini_batch_y)
    #     nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
    #     nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)] 
    #     self.weights = [w-(eta/len(mini_batch))*nw
    #                     for w, nw in zip(self.weights, nabla_w)]
    #     self.biases = [b-(eta/len(mini_batch))*nb
    #                    for b, nb in zip(self.biases, nabla_b)]
    #     for i in range(1, self.num_layers):
    #         n = np.shape(self.biases[-i])[0]
    #         sum = self.biases[-i].sum(axis = 1)
    #         average = sum / n
    #         self.biases[-i] = average.reshape(len(sum), 1)


    # x: mini batch datas with feataures, y: mini batch datas with labels.
    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        x = x.T
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for index, (b, w) in enumerate(zip(self.biases, self.weights)):
            z = np.dot(w, activation)+b
            
            zs.append(z)

            if(index == self.num_layers):
                activation = self.softmax(z)
            else:
                activation = self.sigmoid(z)
            activations.append(activation)
        # backward pass
        
        
        delta = self.cost_derivative(activations[-1], y) * \
            self.sigmoid_prime(zs[-1])
        #sizu = len(delta.T)
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].T) #/ sizu
        
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        sizes_w = []
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = self.sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            sizes_w.append(len(delta.T))
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].T) #/ sizu

        for i in range(1, len(nabla_w)):
            nabla_w[i] = nabla_w[i] / sizes_w[i-1]

        return (nabla_b, nabla_w)

    def feedforward(self, a):
        a = np.reshape(a, (len(a), 1))
        # print(self.weights[0])
        # print(a)
        # print(self.biases[0])
        # print(np.dot(self.weights[0], a) + self.biases[0])
        for b, w in zip(self.biases, self.weights):
            array = np.dot(w, a) + b
            a = self.softmax(array)
            
        return a

    def evaluate(self, test_features, test_labels):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        sum = 0
        for i, data in enumerate(test_features):
            output = self.feedforward(data)
            prediction = np.argmax(output)
            print(np.shape(output))
            print(output)
            print(np.argmax(output))
            print(test_labels[i])
            print("nexttttttttttttttttt")
            if(prediction == test_labels[i]):
                
                sum = sum + 1
        print("amount correct:")
        print(sum)
        print("test size:")
        print(len(test_features))
        print("kill meh:")
        return sum/len(test_features)


    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)