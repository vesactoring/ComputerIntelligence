import numpy as np

def sum(features, weights):
    z = features @ weights

def activate(z, threshold):
    if(z > threshold):
        return 1 
    else：
        return 0

def loss(actual, predict):
    return actual - predict

def update_weights(loss, weights, features, learning_rate):
    weights = weights + loss * features * learning_rate


