import numpy as np
import activation as activ

#useless currB?
def backwardOneLayer(currdA, currW, currB, currZ, prevA):
    n = prevA.shape[0]

    sg = activ.activationFunction(currZ)

    dZ = currdA * sg * (1 - sg)
    dW = np.dot(dZ, prevA.T) / n
    dB = np.sum(dZ, axis=1, keepdims=True) / n
    prevdA = np.dot(currW.T, dZ)

    return prevdA, dW, dB

def backwardAllLayers(Y_Hat, Y, memory, paramValues, neuralNetWorkArchitecturnp.reshape((np.array(pdata),(150,1)), int(number))e):
    gradients = {}
    #n = Y.shape[1]
    # Y = Y.reshape(Y_Hat.shape)

    prevdA = - ((Y / Y_Hat) - ((1 - Y) / (1 - Y_Hat)))

    for prevIdx, layer in reversed(list(enumerate(neuralNetWorkArchitecture))):
        currIdx = prevIdx + 1
        #activ_function_curr = layer["activation"]
        currdA = prevdA

        prevA = memory["A" + str(prevIdx)]
        currZ = memory["Z" + str(currIdx)]
        currW = paramValues["W" + str(currIdx)]
        currB = paramValues["b" + str(currIdx)]

        prevdA, currdW, currdB = backwardOneLayer(currdA, currW, currB, currZ, prevA)
        gradients["dW" + str(currIdx)] = currdW
        gradients["db" + str(currIdx)] = currdB

    return gradients
