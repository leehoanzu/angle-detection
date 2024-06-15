# Train AI Model

In this section, we will delve into two primary methods for Creating AI models that can detect angles and colors. These methods utilize basic programming concepts in conjunction with machine learning techniques to achieve effective detection. Specifically, we will employ [`classification`](https://github.com/leehoanzu/angle-detection/blob/main/train/classification.ipynb) and [`object detection`](https://github.com/leehoanzu/angle-detection/blob/main/train/object_detection.ipynb) techniques in these methods.

# Classification

We follow [`PyTorch tutorial`](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html#creating-models) to create our AI model by dividing the 180-degree range into 36 distinct folders. Each folder represents a 5-degree segment, providing a structured way to organize the data. 

For instance, folder 0 contains images with angles ranging from 0 to 4 degrees. Similarly, folder 1 would contain images with angles from 5 to 9 degrees, and this pattern continues up to folder 35. This systematic division allows the AI model to learn and recognize angle variations more effectively, ensuring precise angle detection across the entire 180-degree spectrum. By organizing the data in this manner, we can enhance the model's ability to accurately classify and differentiate between small angle increments.

```python
# model_conv = torchvision.models.resnet34(weights="IMAGENET1K_V1")
model_conv = torchvision.models.resnet18(weights='IMAGENET1K_V1')

# Parameters of newly constructed modules have requires_grad=True by default
num_ftrs = model_conv.fc.in_features
model_conv.fc = nn.Linear(num_ftrs, 36)

model_conv = model_conv.to(device)

criterion = nn.CrossEntropyLoss()

# Observe that only parameters of final layer are being optimized as
# opposed to before.
optimizer_conv = optim.SGD(model_conv.fc.parameters(), lr=0.001, momentum=0.9)

# Decay LR by a factor of 0.1 every 7 epochs
exp_lr_scheduler = lr_scheduler.StepLR(optimizer_conv, step_size=7, gamma=0.1)

# Start trainning
model_conv = train_model(model_conv, criterion, optimizer_conv,
                         exp_lr_scheduler, num_epochs=25)
```
> [!NOTE]  
> <sup>- For more information. Please check [`classification.ipynb`](https://github.com/leehoanzu/angle-detection/blob/main/train/classification.ipynb)</sup>

![results](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/pytorch_predict_1.png) ![results](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/pytorch_predict_2.png) ![results](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/pytorch_predict_3.png)
![confusion_magic](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/pytorch_confusion_magic.png)

# Object Detection

In this section, we are guided by the [`Ultralytics documentation`](https://docs.ultralytics.com/tasks/obb/) to develop our AI model. Initially, we manually create bounding boxes for objects step by step. Once the bounding process is complete, we proceed to label each image with the corresponding object color. Regarding angles, these are calculated based on the coordinates within the bounding boxes. 
Using this approach makes achieving your goal easier and more straightforward.

```python
from ultralytics import YOLO

# Load a model
model = YOLO("data.yaml")  # build a new model from YAML
model = YOLO("best.pt")  # load a pretrained model (recommended for training)
model = YOLO("data.yaml").load("best.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="data.yaml", epochs=100, imgsz=640)
```
> [!NOTE]  
> <sup>- For more information. Please check [`object_detection.ipynb`](https://github.com/leehoanzu/angle-detection/blob/main/train/object_detection.ipynb)</sup>

![label](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/yolo_label.jpeg)
![label](https://github.com/leehoanzu/angle-detection/blob/main/screen-shots/yolo_valid.png)