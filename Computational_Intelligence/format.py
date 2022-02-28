import numpy as np

def readFeatures(path):

    featureFile = open(path, "r")

    clusterLayer = featureFile.read().split('\n')
    breakClusterLayer = clusterLayer
    for x in range(0, len(clusterLayer)):
        temp = np.array(clusterLayer[x].split(','))
        if temp.size < 9:
            # Since numpy can't comprehend the empty string
            # i.e: [""]
            # so the formatter have to have a if to detect this empty string
            # Because the empty string only appear ONCE, and in the final array
            # Hence, we just need to check if the array size is one in order to detect this empty string
            continue
        breakClusterLayer[x] = temp.astype(np.float)
    
    return breakClusterLayer

