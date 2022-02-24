import numpy as np

def readFeatures(path):

    featureFile = open(path, "r")

    clusterLayer = featureFile.read().split('\n')
    breakClusterLayer = clusterLayer
    for x in range(0, len(clusterLayer)):
        temp = np.array(clusterLayer[x].split(','))
        if temp.size == 1:
            continue
        breakClusterLayer[x] = temp.astype(np.float)
    
    return breakClusterLayer

