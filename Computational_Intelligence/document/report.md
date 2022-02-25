# Questions
**How many input neurons are needed for this assignment?**

For this network we need to classify an input of 10 features. This means that we need at least 10 variables to identify each of these variables. We also need to consider the bias term for each of the neuron, so add another 1 input neuron on top of that for a concluding 11 input neurons.
***

**How many output neurons do you require?**

Since we need to classify the input into one of the 7 classes. We need 7 output neurons to represent each of these classes.
***

**How many hidden neurons and layers will your network have?**

From what we have read; the number of hidden neurons should be between the size of the input layer and the size of the output layer.[[1]](https://stats.stackexchange.com/questions/350718/confused-in-selecting-the-number-of-hidden-layers-and-neurons-in-an-mlp-for-a-bi) That's why for our initial guess we are going for 2 hidden layers where each layer narrows down the amount of neurons by 1. So for hidden layer 1 we are going for 11-1 = 10 neurons. And for layer 2 we are going for 10-1 = 9 neurons. 
***

**Which activation function(s) will you use?**

We choose sigmoid function to use for all of our activation functions. To find the optimal weight values, we need to use back propagation which uses gradient descent on finding the "best step" to apply on the weight. Since gradient descent uses derivation on finding the new optimal weight, we can't use step function as step function is not differentiable. Sigmoid function is differentiable, so we chose this.
***

