import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

data_features = np.genfromtxt("Computational_Intelligence/data/features.txt", delimiter=",")
data_targets = np.genfromtxt("Computational_Intelligence/data/targets.txt", delimiter=",")
# data_lines = [line.rstrip('\n') for line in open('data/features.txt')]
# print(np.shape(data_features))
# folds_features = np.array_split(data_features, 10)
# folds_targets = np.array_split(data_targets, 10)
# print(np.shape(folds_features[0]))
# print(np.shape(folds_targets[0]))
# print(np.shape(folds_features))



def cross_validation(data, targets, neurons):
    folds_features = np.array_split(data, 10)
    folds_targets = np.array_split(targets, 10)
    
    #Our model here instead
    clf = MLPClassifier(hidden_layer_sizes = (4, neurons), alpha = 0.1, learning_rate_init = 0.10, random_state=1)

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
        clf.fit(training_folds, training_folds_targets)
        average_accuracy += (clf.predict(test_fold) == folds_targets[i]).mean()
    return average_accuracy/10

# print(cross_validation(data_features, data_targets, 10, 10))



neurons_amount = np.linspace(start=7, stop=30, num=8, dtype=int)
print(neurons_amount)
accuracies = []

for neuron in neurons_amount:
    accuracy_neuron = cross_validation(data_features, data_targets, neuron)
    accuracies.append(accuracy_neuron)
    
_, axis = plt.subplots()
axis.plot(neurons_amount, accuracies)

axis.legend()
axis.set_xlabel('Neurons')
axis.set_ylabel('Accuracy')
plt.title('Accuracy for different amount of neurons')
plt.grid()
plt.show()


# def cross_validation(data, targets, folds_amount, neurons):
#     folds_features = np.array_split(data, folds_amount)
#     folds_targets = np.array_split(targets, folds_amount)
    
#     #Our model here instead
#     clf = MLPClassifier(hidden_layer_sizes = (4, neurons), alpha = 0.1, learning_rate_init = 0.10, random_state=1)
#     sum_training = 0
#     for i in range(10):
#         average_accuracy = 0
#         for i, test_fold in enumerate(folds_features):
#         # All folds except test folds
#         # training_folds = folds_features[:i] + folds_features[i+1:]
#         # training_folds_targets = folds_targets[:i] + folds_targets[i+1:]
#             training_folds = []
#             training_folds_targets = []
#             for j, training_fold in enumerate(folds_features):
#                 if(i == j):
#                     pass
#                 else:
#                     training_folds.extend(training_fold)
#                     training_folds_targets.extend(folds_targets[j])
#             clf.fit(training_folds, training_folds_targets)
#             average_accuracy += (clf.predict(test_fold) == folds_targets[i]).mean()
#         sum_training += average_accuracy/folds_amount
#     return sum_training/10
    



