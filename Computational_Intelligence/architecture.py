import numpy as np

print(np.random.randn(2, 3))

class Architecture:
    def __init__(self):
        self.neuralNetWorkArchitecture = []
    
    def addLayer(self, numberOfInputNeurons: int, numberOfOutputNeurons: int, activationFunction: str):
        self.neuralNetWorkArchitecture.append({"inputDimension": numberOfInputNeurons,"outputDimension": numberOfOutputNeurons, "activation": activationFunction})

    def getArchitecture(self):
        return self.neuralNetWorkArchitecture

    def init_layers(self, seed = 99):
        np.random.seed(seed)
        number_of_layers = len(self.neuralNetWorkArchitecture)
        params_values = {}

        for idx, layer in enumerate(self.neuralNetWorkArchitecture):
            layer_idx = idx + 1
            layer_input_size = layer["inputDimension"]
            outputLayerSize = layer["outputDimension"]
        
            params_values['W' + str(layer_idx)] = np.random.randn(outputLayerSize, layer_input_size) * 0.1
            params_values['b' + str(layer_idx)] = np.random.randn(outputLayerSize, 1) # For now the bias is set to 1
        
        return params_values
nn_architecture = [
    {"input_dim": 10, "activation": "sigmoid"},
    {"input_dim": 9, "activation": "sigmoid"},
    {"input_dim": 8, "activation": "sigmoid"},
]

    