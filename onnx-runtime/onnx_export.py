from PIL import Image

from torchvision import models, transforms
import torch.nn as nn
import torch

import numpy as np
import onnxruntime
import onnx


class OnnxExport:
    def __init__(self, pre_trained_model_path, onnx_model_path, label_path):
        """
        Initialize the session with paths for the pre-trained model, ONNX model, and label file.
        Check if CUDA is available and set the device accordingly.
        """
        self.pre_trained_model_path = pre_trained_model_path
        self.onnx_model_path = onnx_model_path
        self.label_path = label_path
        self.model = self._load_model()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def _load_model(self):
        # Load the pre-trained model.

        #print(self.device)
        model = models.resnet18(pretrained=False)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, 36)
        model = model.to(self.device)

        model.load_state_dict(torch.load(self.pre_trained_model_path, map_location=self.device))

        model.eval()
        return model
    
    def load_labels(self):
        # Load labels from the label file.

        with open(self.label_path, 'r') as file:
            labels = [line.strip() for line in file.readlines()]
        return labels
    
    def export_onnx(self):
        # Export the loaded model to ONNX format.

        # Example input
        dummy_input = self._preprocess_image("./image/sample.jpg").unsqueeze(0).to(self.device)

        torch.onnx.export(self.model, 
                          dummy_input, 
                          self.onnx_model_path, 
                          export_params=True, 
                          opset_version=10, 
                          do_constant_folding=True, 
                          input_names=['input'], 
                          output_names=['output'])
        print(f"Model has been successfully exported to {self.onnx_model_path}")
    
    def load_onnx_model(self):
        # Load the ONNX model using ONNX Runtime.
        return onnxruntime.InferenceSession(self.onnx_model_path)
    
    def _preprocess_image(self, image_path):
        # Preprocess the image for inference.

        input_image = Image.open(image_path)
        preprocess = transforms.Compose([
            transforms.CenterCrop((730, 247)),
            transforms.Grayscale(num_output_channels=3),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        return preprocess(input_image)
    
    def inference(self, ort_session, image_tensor):
        """
        Perform inference using the ONNX model.
        """
        image_tensor = image_tensor.unsqueeze(0).numpy()
        ort_input = {ort_session.get_inputs()[0].name: image_tensor}
        ort_outputs = ort_session.run(None, ort_input)

        return ort_outputs
    
    def display_prediction(self, output):
        # Display the prediction results.

        out = np.array(output)
        preds = np.argmax(out)
        labels = self.load_labels()
        print(f'Predicted: {labels[preds]}')

if __name__ == '__main__':
    # Paths for the models and labels
    pre_trained_model_path = "/path/to/detect_angle_5.pt.pth"
    onnx_model_path = "/path/to/detect_angle_5.onnx"
    label_path = "/path/to/label.txt"

    # Create an instance of the session
    session = OnnxExport(pre_trained_model_path, onnx_model_path, label_path)

    # Export the PyTorch model to ONNX format
    session.export_onnx()

    # Test 
    # Load the ONNX model
    ort_session = session.load_onnx_model()

    # Preprocess the image for inference
    image_path = "./image/rightway.jpg"
    image_tensor = session._preprocess_image(image_path)

    # Perform inference
    output = session.inference(ort_session, image_tensor)

    # Display the prediction results
    session.display_prediction(output)

    print("Build successfully!")
