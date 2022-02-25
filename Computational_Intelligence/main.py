import numpy as np
from architecture import Architecture
import format as format
import forward_propagation as fp

def numPyPlay():
    print(np.array([0,2,3,4]))

"""
Main.py at the moment is just to test the output of the forward functions
"""

param_values = {}
param_values["W" + str(2)] = "Khoa"

def testDictionary():
    print(param_values["W" + "2"])

testDictionary()

p1 = Architecture()

p1.addLayer(10, 9, "sigmoid")
p1.addLayer(9, 8, "sigmoid") 
p1.addLayer(8, 7,  "sigmoid")

def testForward():
    param_values = p1.init_layers()
    for i in format.readFeatures("./data/features.txt"):
        print(fp.forwardAllLayers(i, param_values, p1.getArchitecture()))

testForward()
