[![a header for a software project about building AI model](https://raw.githubusercontent.com/dusty-nv/jetson-containers/docs/docs/images/header_blueprint_rainbow.jpg)](https://www.jetson-ai-lab.com)

# Welcome to Angle Detection Repository

In this repository, we provide comprehensive guidance on how to deploy an AI model for detecting angles and colors in an industrial conveyor system. You will find in this repo the following stuff:

<a href="https://www.jetson-ai-lab.com"><img align="right" width="200" height="200" src="https://nvidia-ai-iot.github.io/jetson-generative-ai-playground/images/JON_Gen-AI-panels.png"></a>

1. **Training the Model**: offering a detailed guide on [`trainning model`](https://github.com/leehoanzu/angle-detection/blob/main/train/README.md) effectively to detect angles and colors, with complete documentation available here. 
2. **Deploying the Model**: How to deploy the model using [`ONNX Runtime`](https://github.com/leehoanzu/angle-detection/blob/main/onnx-runtime/README.md) which inferences efficiently across multiple platforms and hardware or  [`TensorRT`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/README.md) to optimize their model for NVIDIA devices.
3.  **Setting Up Communication**: Ensuring efficient communication between systems, we include a guide on setting up a [`socket connection`](https://github.com/leehoanzu/angle-detection/blob/main/socket/README.md) for data transfer between devices.


## Gallery

* Integrate Jetson's inference capabilities and communicate with the ABB robot arm.

<a href="https://youtu.be/C5XvOQaP5cA"><img src="https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/automatic_operation.gif"></a> <br/>

* Overview

![`Overview`](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/genaral.jpg)

* Console

![`ABB robot console`](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/console_ABB.jpg) ![`Jetson Console`](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/yolo_results.png)

## Future Update

* Deploying on DeepStream

## Contact

* Connect with me via email: lehoangvu260602@gmail.com

## Copyright

* Copyright &#169; 2024 Lê Hoàng Vũ

## Authors

* Lê Hoàng Vũ
* Nguyễn Trọng Hiếu
* Nguyễn Thành Sơn
