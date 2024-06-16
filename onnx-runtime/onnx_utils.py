import onnxruntime as ort

import numpy as np
from PIL import Image

import torch
from torchvision import transforms

class OnnxUtils:
    def __init__(self, labelPath, onnxModelPath):
        # Initialize the class with paths to the label file and ONNX model.

        self.labelPath = labelPath
        self.onnxModelPath = onnxModelPath
        self.labels = []
    
    def _loadOnnxModel(self):
        # Load the ONNX model using ONNX Runtime.
        return ort.InferenceSession(self.onnxModelPath)
    
    def _loadLabels(self):
        # Load the labels from a file.
        with open(self.labelPath, 'r') as file:
            self.labels = [line.strip() for line in file.readlines()]
    
    def preProcessImage(self, imagePath):
        # Preprocess the image to prepare it for inference.

        inputImage = Image.open(imagePath)

        preprocess = transforms.Compose([
            transforms.CenterCrop((730, 247)),  # Change image size
            transforms.Grayscale(num_output_channels=3),
            transforms.ToTensor(),   # Change tensor
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), # Normolize
        ])

        return preprocess(inputImage)
    
    def infernce(self, imagePath):
        # Perform inference on the preprocessed image using the ONNX model.

        ortSession = self._loadOnnxModel()

        image = self.preProcessImage(imagePath)
        self._loadLabels()

        imageY = image.unsqueeze(0)
        ortInput = {ortSession.get_inputs()[0].name: imageY.numpy()}
        ortOutputs = ortSession.run(None, ortInput)
        
        return ortOutputs
    
    def dispPreds(self, output):
        # Display the prediction results.
        out = np.array(output)
        preds = np.argmax(out)
        print(f'Predicted: {self.labels[preds]}')

if __name__ == "__main__":
    # Define paths for the ONNX model, labels, and the image to be inferred
    onnx_model_path = "/path/to/model.onnx"
    pathLabels = "/path/to/label.txt"
    pathImage = "/path/to/image.jpg"

    # Create an instance of the model deployment class
    session = OnnxUtils(pathLabels, onnx_model_path)
    
    # Perform inference and display the prediction
    output = session.infernce(pathImage)

    # Display prediction
    session.dispPreds(output)

    print("Build successfully!")
