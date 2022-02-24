import numpy as np
import matplotlib.pyplot as plt

features = [[0, 0], [1, 0], [0, 1], [1, 1]]
label_and = [0, 0, 0, 1]
label_or = [0, 1, 1, 1]
label_xor = [0, 1, 1, 0]

weights = [1, 1]
threshold = 0.5
learning_rate = 0.1


def sum(data, weights):
    x0 = data[0]
    x1 = data[1]

    return x0 * weights[0] + x1 * weights[1]

def activate(z, threshold):
    if(z > threshold):
        return 1 
    else:
        return 0


def training(epoch, features, weights, threshold, labels, learning_rate):
    w = weights
    for j in range(epoch):
        for i in range(features.shape[0]):
            actual = labels[i]
            data = features[i]

            z = sum(data, weights)

            a = activate(z, threshold)
            
            lose = actual - a

            w = weights + learning_rate * lose * data
    return w


def predict(features, weights, threshold):
    n = features.shape[0]
    result = np.zeros(n)

    for i in range(n):
        data = features[i]
        z = sum(data, weights)
        
        result[i] = activate(z, threshold)

def error(predicts, labels):
    return np.sum(np.square(labels- predicts)) / len(predict) 


def plot(max_epoch, labels):
    errors = []
    epoches = np.linspace(0, 1, max_epoch)

    for i in max_epoch:
        weights = training(i, features, weights, threshold, labels, learning_rate)
        e = error(predict(features, weights, threshold), labels)
        errors.append(e)

    _, axis = plt.subplots()
    axis.plot(epoches, errors)
    
    axis.legend()
    axis.set_xlabel('epoch')
    axis.set_ylabel('errors')
    plt.title('errors for different epoch')
    plt.grid()
    plt.show()

