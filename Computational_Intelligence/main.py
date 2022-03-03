import Neural_Network
import numpy as np

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
iterations = 450
learning_rate = 0.4
Networks_sample = Neural_Network.Network([data_features.shape[1], 10, 9 , 7], X_train, Y_train, learning_rate, iterations)
Networks_sample.model()

print("Accuracy of Train Dataset", round(Networks_sample.accuracy(X_train, Y_train), 2), "%")
print("Accuracy of Validation Dataset", round(Networks_sample.accuracy(X_validation, Y_validation), 2), "%")
print("Accuracy of Test Dataset", round(Networks_sample.accuracy(X_test, Y_test), 2), "%")