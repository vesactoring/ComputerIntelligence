import numpy as np
from architecture import Architecture
import format as format
import forward_propagation as fp
import train as train

# def numPyPlay():
#     print(np.array([0,2,3,4]))

# """
# Main.py at the moment is just to test the output of the forward functions
# """

# param_values = {}
# param_values["W" + str(2)] = "Khoa"

# def testDictionary():
#     print(param_values["W" + "2"])

# testDictionary()

p1 = Architecture()

p1.addLayer(10, 9, "sigmoid")
p1.addLayer(9, 8, "sigmoid") 
p1.addLayer(8, 7,  "sigmoid")

x = [] 
print([1,2])
print(np.array([1, 2]).T)
param = []

def testForward():
    param_values = p1.init_layers()
    i = format.readFeatures("./data/features.txt")[1]
    print(i)
    formatted = format.readFeatures("./data/features.txt")
    targets = format.readFeatures("./data/targets.txt")
    for i in range(formatted.shape[0]):
        param = train.train(formatted[i], targets[i], p1.getArchitecture(), formatted.shape[0], 0.5, p1.init_layers())

testForward()
print(param)
print("success")
