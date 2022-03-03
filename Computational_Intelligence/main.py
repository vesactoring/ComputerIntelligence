
import Neural_Network
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axis as axis
from single_perceptron import plot

if __name__ == '__main__':
    label_and = np.array([0, 0, 0, 1])
    label_or = np.array([0, 1, 1, 1])
    label_xor = np.array([0, 1, 1, 0])

    max_epoch = 10
    
    plot = plot(max_epoch, label_xor)

    data_features = np.genfromtxt("data/features.txt", delimiter=",")
    data_targets = np.genfromtxt("data/targets.txt", delimiter=",")
    data_unknown = np.genfromtxt("data/unknown.txt", delimiter=",")


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
    learning_rate = 0.4

    Networks_sample = Neural_Network.Network([data_features.shape[1], 18, 12 , 7], X_validation, Y_validation, learning_rate, iterations)
    _, cost_list_epoch = Networks_sample.model()

    ###picking the best parameters
    accuracy = []
    accuracies_plot = []
    validation_accuracy = []
    test_accuracy = []
    i = 0
    while i < iterations:
      Networks_sample = Neural_Network.Network([data_features.shape[1], 18, 12 , 7], X_validation, Y_validation, learning_rate, i)
      para, cost_list = Networks_sample.model()
      accu = round(Networks_sample.accuracy(X_train, Y_train), 2)
      # validation_accuracy.append(round(Networks_sample.accuracy(X_validation, Y_validation), 2))
      # test_accuracy.append(round(Networks_sample.accuracy(X_test, Y_test), 2))
      accuracy.append((accu, para))
      # accuracies_plot.append(accu)
      i = i + 200

    # times = []
    # j = 0
    # while j < iterations:
    #     times.append(j)
    #     j = j + 200
    # plt.plot(times, accuracies_plot)
    # plt.xlabel('Training')
    # plt.ylabel('Accuracies')
    # plt.title('performance accuracies for different weights')
    # plt.grid()
    # plt.show()

    # plt.plot(times, validation_accuracy)
    # plt.xlabel('Validation')
    # plt.ylabel('Accuracies')
    # plt.title('performance accuracies for different weights')
    # plt.grid()
    # plt.show()

    # plt.plot(times, test_accuracy)
    # plt.xlabel('Test')
    # plt.ylabel('Accuracies')
    # plt.title('performance accuracies for different weights')
    # plt.grid()
    # plt.show()

    num=(0, {})
    for item in accuracy:
    if item[0]>num[0]:
      num=item #num has the whole tuple with the highest y value and its x value
    ####################
    #####PLOTING########
    ####################
    plt.xlabel('different epochs')
    plt.ylabel('cost_function_values')
    plt.xlim(0, iterations)
    plt.ylim(0, np.max(cost_list_epoch))
    plt.title('performance errors')
    plt.grid()
    new_cost_list = []
    new_validation_list = []
    i_list = []
    i=0
    print(i)
    while i < iterations:
      new_cost_list.append(cost_list_epoch[i])
      i_list.append(i)
      i = i + 10
    plt.plot(i_list, new_cost_list)
    plt.show()

    plt.xlabel('different epochs')
    plt.ylabel('cost_function_values')
    plt.xlim(0, iterations)
    plt.ylim(0, np.max(cost_list))
    plt.title('performance errors')
    plt.grid()
    plt.plot(i_list, new_validation_list)
    plt.show()
    ####################
    #####PLOTING########
    ####################

    #------------------#

    ####################
    ###UNKNOWN SET######
    ####################
    forward_memory = Networks_sample.forward_propagation_static(data_unknown.T, num[1])
    y_prediction = forward_memory["a3"]
    y_prediction = np.argmax(y_prediction, 0) + 1
    converted_list = [str(element) for element in y_prediction]
    joined_string = ",".join(converted_list)
    with open('../Group_01_classes.txt', 'w') as f:
      f.write(joined_string)
    ####################
    ###UNKNOWN SET######
    ####################

    #Accuracy
    print("Accuracy of Train Dataset", round(Networks_sample.accuracy(X_train, Y_train), 2), "%")
    print("Accuracy of Validation Dataset", round(Networks_sample.accuracy(X_validation, Y_validation), 2), "%")
    print("Accuracy of Test Dataset", round(Networks_sample.accuracy(X_test, Y_test), 2), "%")


