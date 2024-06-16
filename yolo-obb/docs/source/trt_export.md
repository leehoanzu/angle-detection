# TensorRT Export

Deploying computer vision models in high-performance environments can require a format that maximizes speed and efficiency. This is especially true when you are deploying your model on NVIDIA GPUs. By using the [`TensorRT export`](https://docs.ultralytics.com/integrations/tensorrt/) format, you can enhance your Ultralytics YOLOv8 models for swift and efficient inference on NVIDIA hardware. 

## Usage

```python
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("angle.pt")

# Export the model to TensorRT format
model.export(format="engine")  # creates 'yolov8n.engine'

# Load the exported TensorRT model
tensorrt_model = YOLO("angle.engine")

# Run inference
results = tensorrt_model("https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/image/rightway.jpg")
```

### Exporting TensorRT with INT8 Quantization

- Reduced model size: Quantization from FP32 to INT8 can reduce the model size by 4x (on disk or in memory), leading to faster download times. lower storage requirements, and reduced memory footprint when deploying a model.

- Lower power consumption: Reduced precision operations for INT8 exported YOLO models can consume less power compared to FP32 models, especially for battery-powered devices.

- Improved inference speeds: TensorRT optimizes the model for the target hardware, potentially leading to faster inference speeds on GPUs, embedded devices, and accelerators.

```python
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("angle.pt")

# Export the model
model.export(
    format="engine",
    dynamic=True,  
    batch=8,  
    workspace=4,  
    int8=True,
    data="data.yaml",  
)
```

> [!NOTE]  
> <sup>- It took almost three hours to export with INT8 quantization.</sup><br>
> <sup>- File [`data.yaml`](https://github.com/leehoanzu/angle-detection/blob/main/train/data.yaml) is the confige file to train model.</sup>

## Reference

![tensor_rt_results](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/trt_export.png)