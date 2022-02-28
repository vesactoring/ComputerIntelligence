from forward_propagation import Network
import numpy as np
   
if __name__ == '__main__':

    Networks_sample = Network([10, 9, 8 ,7])
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
    Networks_sample.fit(training_data_features, training_data_labels, 10, largest_prime_factor(len(training_data_features)), 0.01)

    
