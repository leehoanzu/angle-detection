# Quickstart

This section instructs how to start using the AI model to detect angles. Before we get started, be sure to check the  [`installation`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/docs/source/installation.md) and [`export`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/docs/source/trt_export.md) guides.

## Tutorial

### Create a Socket Connection

Change Host, IP or role in [`config.yml`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/config.yml)

```yaml
Name: 'server' # or client role

Receive: 'a'  # Receive message from another host
Send: 'e'     # Send message to another host

Port: 3000
Host: '192.168.1.8'
```

### Replace Model AI

Choose your model format such as PyTorch, TensorRT in [`opencv_processing.py`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/utils/opencv_processing.py) or [`pysence_processing.py`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/utils/pysence_processing.py)

```python
# Path of pretrained model
preTrainedModelPath = getAbsPath("../model/best.pt") # PyTorch format

# preTrainedModelPath = getAbsPath("../model/best.engine") # TensorRT format
```

### Choose Threading

If you use the Pysense camera, you should choose Pysense threading or simply use OpenCV to read the camera. Change it in [`main.py`](https://github.com/leehoanzu/angle-detection/blob/main/yolo-obb/utils/main.py)

```python
 # Choose your main script
default_script = 'pysence'  # Set 'pysence' or 'cv'

# Set argparse 
parser = argparse.ArgumentParser(description="Choose a script to run.")
parser.add_argument('script', nargs='?', choices=['pysence', 'cv'], help="The script to run: 'pysence' or 'cv'")
args = parser.parse_args()

# If dont have agr in command line, it will use default script
chosen_script = args.script if args.script else default_script

script_map = {
    'pysence': 'pysence_processing.py',
    'cv': 'opencv_processing.py'
}

if chosen_script in script_map:
    run_script(script_map[chosen_script])
else:
    print(f"Invalid choice: {chosen_script}. Please choose 'pysence' or 'cv'.")
```

### Start inferring

After connecting with the client, it's time for the demonstration.

```bash
$ python3 main.py
```