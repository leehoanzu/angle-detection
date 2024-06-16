import cv2
import RPi.GPIO as GPIO
from threading import Thread

from onnx_utils import OnnxUtils

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

def threadPredict(pathImage):
    """
    Function to start a prediction thread.
    """
    results = modelDeploy.infernce(pathImage)
    modelDeploy.dispPreds(results)
    print()

def _init_():
    """
    Function to initialize GPIO settings.
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensorPin, GPIO.IN)
    GPIO.setup(ouputPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(sensorPin, GPIO.FALLING, callback=callbackFcn, bouncetime=20)
    print("Starting demo now! Press CTRL+C to exit\n")

def main():
    """
    Main function to run the GPIO event loop.
    This function will loop until a trigger signal is received.
    """
    _init_()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        print(e)
        GPIO.cleanup()

if __name__ == '__main__':
    # Define the GPIO pin numbers
    sensorPin = 18  # Sensor input pin
    ouputPin = 16  # Output pin to control an external device

    # Path to the image where the captured image will be saved
    pathImage = '/path/to/image.jpg'  # Replace with actual path

    # Initialize the ONNX model with label and model paths
    modelDeploy = OnnxUtils('/path/to/label.txt', '/path/to/model.onnx')  # Replace with actual paths

    main()
