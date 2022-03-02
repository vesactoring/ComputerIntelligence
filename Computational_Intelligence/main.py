from forward_propagation import Network
import numpy as np
import new_forward_propagation as nfp
   
if __name__ == '__main__':

    # Networks_sample = Network([10, 9, 8 ,7])
    # test = NeuralNetwork(10, 17, 7)
    # for i, value in enumerate(Networks_sample.weights):
    #     print(i, " value", np.shape(value))

    data_features = np.genfromtxt("data/features.txt", delimiter=",")
    data_targets = np.genfromtxt("data/targets.txt", delimiter=",")

    training = int(len(data_features) * 0.65)
    validation = training + int(len(data_features) * 0.20)

    training_data_features = data_features[:training, :]
    training_data_labels = data_targets[:training]
    validation_data_features = data_features[training:validation, :]
    validation_data_labels = data_targets[training:validation]

    test_data_features = data_features[validation:len(data_features), :]
    test_data_labels = data_targets[validation:len(data_targets)]
    def largest_prime_factor(n):
            i = 2
            while i * i <= n:
                if n % i:
                    i+=1
                else:
                    n //=i
            return n
    # example = data_features[0]
    # print("EXAMPLE, ", example)
    # print("RESULT,", Networks_sample.feedforward(example))
    # print(Networks_sample.evaluate(test_data_features, test_data_labels))
    # Networks_sample.fit(training_data_features, training_data_labels, 10, largest_prime_factor(len(training_data_features)), 0.5)    
    # print(np.shape(test_data_features))
    # print(Networks_sample.evaluate(test_data_features, test_data_labels))

    # XOR example:
    # training_sets = []
    # for i, x in enumerate(training_data_features):
    #     training_sets.append([x, [training_data_labels[i]]])

# training_sets = [
#     [[0, 0], [0]],
#     [[0, 1], [1]],
#     [[1, 0], [1]],
#     [[1, 1], [0]]
# ]

# nn = NeuralNetwork(len(training_sets[0][0]), 5, len(training_sets[0][1]))
# for i in range(100):
#     nn.train(training_data_features, training_data_labels)
#     print(i, nn.calculate_total_error(training_sets))
weights = nfp.training(training_data_features, training_data_labels, 200, 0.2, nfp.init_layers([11, 10, 9, 7]))
print(weights)
nfp.evaluate(test_data_features, test_data_labels, weights)