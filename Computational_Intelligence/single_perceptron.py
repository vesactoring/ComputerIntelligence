import numpy as np

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


features = [[0, 0], [1, 0], [0, 1], [1, 1]]
label_and = [0, 0, 0, 1]
label_or = [0, 1, 1, 1]
label_xor = [0, 1, 1, 0]

weights = [1, 1]
threshold = 0.5
learning_rate = 0.1

