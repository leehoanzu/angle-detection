# NVIDIA Jetson with Ultralytics YOLOv8

In this section, we will guide you through a comprehensive end-to-end process. You will learn how to export a model from the PyTorch format to TensorRT, deploy it using TensorRT on an NVIDIA Jetson device.
Finally, we will demonstrate how to [`encapsulate`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/docs/build.md) the deployment environment into a Docker container, ensuring that your model can be easily shared, replicated, and deployed across different systems with consistency and ease.


### Start with Docker

* Pull image from [`Docker Hub`](https://hub.docker.com/repository/docker/leehoanzu/yolo-utils/general)

```bash
$ sudo docker pull leehoanzu/yolo-utils
```

* Running Conntainer

```bash
$ jetson-containers run leehoanzu/yolo-utils
```

> [!NOTE]  
> <sup>- The [`jetson-containers run`](https://github.com/leehoanzu/angle-detection/blob/main/run.sh) command and the "./run.sh" script serve the same purpose in our workflow.</sup><br>

### Start without Docker

```bash
$ python3 main.py
```

> [!NOTE]  
> <sup>- Please check [`quickstart.md`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/docs/source/quickstart.md) for more information.</sup><br>
