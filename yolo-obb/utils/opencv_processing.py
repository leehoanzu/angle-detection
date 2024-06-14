import cv2

from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from SocketProgram import SocketConnection
from YoloUtil import YoloInference

import yaml
import sys
import os

import time 
import logging

def threadPredict(path, connType, connector):
    # Start unferencing
    # t0 = time.time()
    results = modelDeploy.predict(path)
    if results is not None:
        cls, angle = results
        connector.send(connType, connector, f"C_{cls} A_{angle}")
        modelDeploy.display(cls, angle)
    else:
        print("Can't infer picture!\n")
        print("Try again!\n")
        # threadCap(connType, connector)
        time.sleep(1)
        executor.submit(threadCap, connType, connector)
    # print(f'Done. ({time.time() - t0:.3f}s)')

def threadCap(connType, connector):
    print("\nSensor detected!")
    cap = cv2.VideoCapture(4) # Number cam is 4
    access, img = cap.read()

    # Release buffer
    cap.release()

    if access:
        # cv2.imwrite("./image/sample.jpg", img)
        # Give the thread inference
        Thread(target=threadPredict, args=(img, connType, connector)).start()
        # Give the thread inference
        # executor.submit(threadPredict, img, connType, connector).result()
    else:
        print("Failed to capture image!")
        time.sleep(2)
        threadCap(connType, connector)
    
def configYmlFile():
    '''
        - This is 2 method read file yaml config from local disk
        - Number 1 is given argrument via terminal console
        - Number 2 is loaded from local disk via function
    '''
    if len(sys.argv) <= 1:
        with open(getAbsPath("../config.yml"), 'r') as f:  
            return yaml.load(f, Loader=yaml.FullLoader)
    else:
        stream = open(sys.argv[1], 'r')
    return yaml.load(stream, Loader=yaml.FullLoader)

def serverProgram():
    print("Current role is server!")
    # Make connection
    server = SocketConnection(items['Host'], int(items['Port']))
    # Bind host address and port together
    server.serverBind()
    while True:
        try:     
            print("Waiting data...\n")            
            data = server.serverRcv()
            if data.strip().lower() == items['Receive']:
                # print("Received from client: " + str(data))
                # Thread(target=threadCap, args=("server", server)).start()
                # Wait for the task to complete
                executor.submit(threadCap, "server", server)
            else:
                server.serverSend(items['Send'])
                print("Incorrect message!\n")
                # Close socket and reconnect
                server.close() 
                serverProgram()
        except Exception as e:
            server.serverSend(items['Send'])
            print(e)
        except KeyboardInterrupt:
            server.close() # Close connection
            break
    
    # server.close() # Close connection

def clientProgram():
    print("Current role is client!")
    # Make connection
    client = SocketConnection(items['Host'], int(items['Port']))
    client.clientConnect()
    while True:
        try:      
            print("Waiting data...\n")       
            data = client.clientRcv() # Listening signal from server
            if data.strip().lower() == items['Receive']:                
                # Thread(target=threadCap, args=("server", server)).start()
                # Wait for the task to complete
                executor.submit(threadCap, "client", client)
            else:
                client.clientSend(items['Send'])
                print("Incorrect message!\n")
                client.close()
                clientProgram()
        except Exception as e:
            client.clientSend(items['Send'])
            print(e)
        except KeyboardInterrupt:
            client.close() # Close connection
            break
    
    # client.close() # Closed connection

def getAbsPath(path):
    # Get absolutely path
    currentDir = os.path.dirname(os.path.abspath(__file__))

    return os.path.abspath(os.path.join(currentDir, path))

def main():   
    print("\nStarting demo now! Press CTRL+C to exit\n")
    if items['Name'] == "server":
        serverProgram()        
    else:
        clientProgram()
    print("\nEnd.")

if __name__ == '__main__':
    # Set logging level to ERROR 
    # Only logging when there is an error
    logging.getLogger().setLevel(logging.ERROR)

    # Define path label
    labelPath =  getAbsPath("../label/label.txt")

    # Path of pretrained model
    preTrainedModelPath = getAbsPath("../model/best.pt") # PyTorch format
    # preTrainedModelPath = getAbsPath("../model/best.engine") # TensorRT format

    # Path of class color
    classPath = getAbsPath("../label/class.txt")

    # Initialize the thread pool executor
    executor = ThreadPoolExecutor(max_workers=4)

    # Create intance
    modelDeploy = YoloInference(preTrainedModelPath, labelPath, classPath)

    # [{Name: 'server'}, {Receive: 'a'}, {Send: 'b'}, {Port: 3000}, {Host: '192.168.137.226'}]
    items = configYmlFile()
    # for key, values in items.items():
    #     print(key + " : " + str(values)) # Co the bo qua

    main()