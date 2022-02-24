def epoches(epoch, features, weights, threshold, labels, learning_rate):
    for j in range(epoch):
        for i in range(features.shape[0]):
            actual = labels[i]
            data = features[i]

            x0 = data[0]
            x1 = data[1]

            z = x0 * weights[0] + x1 * weights[1]

            if(z > threshold):
                a = 1 
            else:
                a = 0
            
            lose = actual - a

            weights = weights + learning_rate * lose * data

        


