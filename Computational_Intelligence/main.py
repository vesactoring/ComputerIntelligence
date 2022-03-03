import Neural_Network
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axis as axis

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

print(Y_train.T)

X_validation = np.transpose(X_validation)
Y_validation = np.transpose(Y_validation)

X_test = np.transpose(X_test)
Y_test = np.transpose(Y_test)

# Test

iterations = 500
learning_rate = 0.5

Networks_sample = Neural_Network.Network([data_features.shape[1], 10, 9 , 7], X_train, Y_train, learning_rate, iterations)
_, cost_list = Networks_sample.model()

####################
#####PLOTING########
####################
plt.xlabel('different epochs')
plt.ylabel('cost_function_values')
plt.xlim(0, iterations)
plt.ylim(0, np.max(cost_list))
plt.title('performance errors')
plt.grid()
new_cost_list = []
i_list = []
i=0
while i < iterations:
    new_cost_list.append(cost_list[i])
    i_list.append(i)
    i = i + 10
plt.plot(i_list, new_cost_list)
plt.show()
####################
#####PLOTING########
####################

#------------------#

####################
###UNKNOWN SET######
####################
forward_memory = Networks_sample.forward_propagation(data_unknown.T)
y_prediction = forward_memory["a3"]
y_prediction = np.argmax(y_prediction, 0) + 1
converted_list = [str(element) for element in y_prediction]
joined_string = ",".join(converted_list)
with open('readme.txt', 'w') as f:
    f.write(joined_string)
####################
###UNKNOWN SET######
####################

#Accuracy
print("Accuracy of Train Dataset", round(Networks_sample.accuracy(X_train, Y_train), 2), "%")
print("Accuracy of Validation Dataset", round(Networks_sample.accuracy(X_validation, Y_validation), 2), "%")
print("Accuracy of Test Dataset", round(Networks_sample.accuracy(X_test, Y_test), 2), "%")