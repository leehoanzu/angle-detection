# Installation

This repository is tested on Python 3.8, and Linux/Debian systems.
It is recommended to install in a [virtual environment](https://docs.python.org/3/library/venv.html) to keep your system in order.
Currently supported ML Frameworks are the following: `torch`, `torchvison`,`onnxruntime`, `python 3.8`.

```bash
pip install ultralytics
```
> [!NOTE]  
> <sup>- If Torch and Torchvision are installed via pip, they are not compatible to run on the Jetson platform, which is based on the ARM64 architecture.</sup><br>
> <sup>- The steps below are optional for manually installing the pre-built PyTorch pip wheel and compiling/installing Torchvision from source.</sup>

## Optional Dependencies

Additionally, optional dependencies can be installed based on the framework you are using.

### PyTorch and Torchvision

Download the [`pre-built PyTorch`](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048) binaries for your version of JetPack, and see the installation instructions to run on your Jetson. In these instruction, we use PyTorch v2.1.0 for JetPack 5.1.

- PyTorch
```bash
# substitute the link URL and wheel filename from the desired torch version
$ wget https://developer.download.nvidia.cn/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl -o torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl 
$ sudo apt-get install python3-pip libopenblas-base libopenmpi-dev libomp-dev
$ pip3 install 'Cython<3'
$ pip3 install numpy torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl 
```

- Torchvision
```bash
$ sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev
$ git clone --branch v.0.16.1 https://github.com/pytorch/vision torchvision   
$ cd torchvision
$ export BUILD_VERSION=0.16.1  # where 0.16.1  is the torchvision version
$ python3 setup.py install --user
```
> [!NOTE]  
> <sup>- The Torchvision version for PyTorch v2.1 is v0.16.1. See the table for the correct version of Torchvision to download!</sup>

| PyTorch Version | Torchvision Version |
|-----------------|---------------------|
| v1.0            | v0.2.2              |
| v1.1            | v0.3.0              |
| v1.2            | v0.4.0              |
| v1.3            | v0.4.2              |
| v1.4            | v0.5.0              |
| v1.5            | v0.6.0              |
| v1.6            | v0.7.0              |
| v1.7            | v0.8.1              |
| v1.8            | v0.9.0              |
| v1.9            | v0.10.0             |
| v1.10           | v0.11.1             |
| v1.11           | v0.12.0             |
| v1.12           | v0.13.0             |
| v1.13           | v0.13.0             |
| v1.14           | v0.14.1             |
| v2.0            | v0.15.1             |
| v2.1            | v0.16.1             |
| v2.2            | v0.17.1             |
| v2.3            | v0.18.0             |

### Onnxruntime-GPU

The [`onnxruntime-gpu`](https://elinux.org/Jetson_Zoo#ONNX_Runtime) package hosted in PyPI does not have aarch64 binaries for the Jetson. So we need to manually install this package. This package is needed for some of the exports.

```bash
$ wget https://nvidia.box.com/shared/static/zostg6agm00fb6t5uisw51qi6kpcuwzd.whl -O onnxruntime_gpu-1.17.0-cp38-cp38-linux_aarch64.whl
$ pip install onnxruntime_gpu-1.17.0-cp38-cp38-linux_aarch64.whl
```
