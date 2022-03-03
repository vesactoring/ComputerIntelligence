import numpy as np
import matplotlib.pyplot as plt
import Neural_Network
from sklearn.neural_network import MLPClassifier

data_features = np.genfromtxt("data/features.txt", delimiter=",")
data_targets = np.genfromtxt("data/targets.txt", delimiter=",")
data_targets_transform = []
n = len(data_features)

for i in range(n):
    label = np.zeros((1,7))
    label[:, int(data_targets[i]) - 1] = 1
    label = label.flatten()
    data_targets_transform.append(label)

def cross_validation(data, targets, neurons1, neurons2):
    folds_features = np.array_split(data, 10)
    folds_targets = np.array_split(targets, 10)
    
    #Our model here instead
    # clf = MLPClassifier(hidden_layer_sizes = (4, neurons), alpha = 0.1, learning_rate_init = 0.10, random_state=1)

    average_accuracy = 0
    for i, test_fold in enumerate(folds_features):
        # All folds except test folds
        training_folds = []
        training_folds_targets = []
        for j, training_fold in enumerate(folds_features):
            if(i == j):
                pass
            else:
                training_folds.extend(training_fold)
                training_folds_targets.extend(folds_targets[j])
        # clf.fit(training_folds, training_folds_targets)
        trainingModel = Neural_Network.Network([10, neurons1, neurons2 , 7], np.transpose(training_folds), np.transpose(training_folds_targets), 0.4, 220)
        trainingModel.model()
        average_accuracy += (trainingModel.accuracy(np.transpose(test_fold), np.transpose(folds_targets[i])))
    return average_accuracy/10

# print(cross_validation(data_features, data_targets, 10, 10))



neurons_amount = np.linspace(start=7, stop=30, num=4, dtype=int)

print(neurons_amount)
accuracies = []

for index, neuron in enumerate(neurons_amount):
    accuracy_neuron = cross_validation(data_features, data_targets_transform, int(0.6*neuron), int(0.4*neuron))
    accuracies.append(accuracy_neuron)
    
_, axis = plt.subplots()
axis.plot(neurons_amount, accuracies)

axis.legend()
axis.set_xlabel('Neurons')
axis.set_ylabel('Accuracy')
plt.title('Accuracy for different amount of neurons')
plt.grid()
plt.show()
