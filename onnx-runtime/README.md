# Deploy with ONNX Runtime

This section will provide a detailed guide on how to deploy your model using ONNX Runtime on a Jetson. Initially, we will explain how to receive input signals through the [`Jetson'GPIO`](https://github.com/NVIDIA/jetson-gpio). Once the input signal is detected, the system will capture an image and commence the inference process. Additionally, we will cover how to establish a socket connection, which allows you to transfer messages to an opponent system seamlessly if you choose to implement this feature. This can ensure efficient communication and coordination between devices, potentially enhancing the overall functionality and performance of your deployed model.

## Quickstart

### Export

In this tutorial, we describe how to convert a model defined in PyTorch into the ONNX format using the TorchScript [`torch.onnx.export`](https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html) ONNX exporter.

The [`exported model`](https://github.com/leehoanzu/angle-detection/blob/main/onnx-runtime/onnx_export.py) will be executed with ONNX Runtime. ONNX Runtime is a performance-focused engine for ONNX models, which inferences efficiently across multiple platforms and hardware.

```python
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
```

### Load Model

```python
import onnxruntime as ort

def _loadOnnxModel(self):
    # Load the ONNX model using ONNX Runtime.
    return ort.InferenceSession(self.onnxModelPath)
```

### Define Input Pin

```python
def callbackFcn(channel):
    """
    Callback function that is triggered when the sensor detects an event.
    Captures an image and starts a prediction thread.
    """
    GPIO.output(ouputPin, GPIO.HIGH)
    if GPIO.input(sensorPin) == 0:
        print("Sensor detected!")
        cap = cv2.VideoCapture(4)  # Adjust camera index if needed
        access, img = cap.read()
        if access:
            cv2.imwrite(pathImage, img)
            Thread(target=threadPredict, args=(pathImage,)).start()
        else:
            print("Failed to capture image.")
        cap.release()
    print("finish!")
    GPIO.output(ouputPin, GPIO.LOW)

def _init_():
    """
    Function to initialize GPIO settings.
    sensorPin = 18
    ouput PIn = 16
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensorPin, GPIO.IN)
    GPIO.setup(ouputPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(sensorPin, GPIO.FALLING, callback=callbackFcn, bouncetime=20)

    print("Starting demo now! Press CTRL+C to exit\n")
```

### Infer

```python
def infernce(self, imagePath):
    # Perform inference on the preprocessed image using the ONNX model.

    ortSession = self._loadOnnxModel()

    image = self.preProcessImage(imagePath)
    self._loadLabels()

    imageY = image.unsqueeze(0)
    ortInput = {ortSession.get_inputs()[0].name: imageY.numpy()}
    ortOutputs = ortSession.run(None, ortInput)
    
    return ortOutputs
```

### Display

```python
def dispPreds(self, output):
    # Display the prediction results.
    out = np.array(output)
    preds = np.argmax(out)
    print(f'Predicted: {self.labels[preds]}')
```

> [!NOTE]  
> <sup>- This quote is sourced from [`onnx_utils.py`](https://github.com/leehoanzu/angle-detection/blob/main/onnx-runtime/onnx_utils.py) and [`main.py`](https://github.com/leehoanzu/angle-detection/blob/main/onnx-runtime/main.py).</sup><br>
> <sup>- For more detailed information, please refer to these files.</sup>
