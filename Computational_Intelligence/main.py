import Neural_Network
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axis as axis

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

# Test

iterations = 1000
learning_rate = 0.5
# Networks_sample = Neural_Network.Network([data_features.shape[1], 10, 9 , 7], X_train, Y_train, learning_rate, iterations)
# param_values, cost_weights = Networks_sample.model()

# accuracies = []
# times = np.linspace(1, 10, 10)

# for i in range(10):
Networks_sample = Neural_Network.Network([data_features.shape[1], 10, 9 , 7], X_train, Y_train, learning_rate, iterations)
Networks_sample.model()
# accuracy = round(Networks_sample.accuracy(X_train, Y_train), 2)
# accuracies.append(round(Networks_sample.accuracy(X_train, Y_train), 2))


# plt.plot(times, accuracies)
# plt.xlabel('different weights')
# plt.ylabel('accuracies')
# plt.xlim(0, 10)
# plt.ylim(0, 100)
# plt.title('performance accuracies for different weights')
# plt.grid()
# plt.show()
print("Accuracy of Train Dataset", round(Networks_sample.accuracy(X_train, Y_train), 2), "%")
print("Accuracy of Validation Dataset", round(Networks_sample.accuracy(X_validation, Y_validation), 2), "%")
print("Accuracy of Test Dataset", round(Networks_sample.accuracy(X_test, Y_test), 2), "%")