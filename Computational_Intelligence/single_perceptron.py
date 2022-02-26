import numpy as np

features = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]])
label_and = np.array([0, 0, 0, 1])
label_or = np.array([0, 1, 1, 1])
label_xor = np.array([0, 1, 1, 0])

weights = [1, 0, 0]
threshold = 0.5
learning_rate = 0.1
max_epoch = 10


def sum(data, weights):
    x0 = data[0]
    x1 = data[1]
    bias = data[2]

    return x0 * weights[0] + x1 * weights[1] + bias * weights[2]

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

            w[0] = w[0] + learning_rate * lose * data[0]
            w[1] = w[1] + learning_rate * lose * data[1]
            w[2] = w[2] + learning_rate * lose * data[2]


    return w


def predict(features, weights, threshold):
    n = features.shape[0]
    result = np.zeros(n)

    for i in range(n):
        data = features[i]
        z = sum(data, weights)
        
        result[i] = activate(z, threshold)
    return result

def error(predicts, labels):
    return np.sum(np.square(labels- predicts)) / predicts.size


def plot(max_epoch, labels):
    errors = []
    epoches = np.linspace(1, max_epoch, max_epoch)

    for i in range(max_epoch):
        w = training(i, features, weights, threshold, labels, learning_rate)
        e = error(predict(features, w, threshold), labels)
        errors.append(e)

    print(epoches)
    print(errors)

    # This is put to plotting.ipynb
    # plt.plot(epochs, errors)
    
    # axis.legend()
    # axis.set_xlabel('epoch')
    # axis.set_ylabel('errors')
    # plt.title('errors for different epoch')
    # plt.grid()
    # plt.show()

