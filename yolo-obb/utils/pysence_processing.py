from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from socketProgram import SocketConnection
from YoloUtil import YOLOInference

import yaml
import sys
import os

import time 
import logging

import pyrealsense2 as rs
import numpy as np

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
        time.sleep(2)
        connector.send(connType, connector, f"C_{2} A_{0}")
        #executor.submit(threadCap, connType, connector)
    # print(f'Done. ({time.time() - t0:.3f}s)')

def threadCap(connType, connector):
    print("\nSensor detected!")
    try:
        # wait for frames and align them
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        color_frame = aligned_frames.get_color_frame()
    
        if not color_frame:
            print("failed to capture color frame")
            time.sleep(2)
            threadCap(connType, connector)
    
        # Convert frame to numpy array
        color_image = np.asanyarray(color_frame.get_data())
    
        # Give the thread inference
        Thread(target=threadPredict, args=(color_image, connType, connector)).start()

    except Exception as e:
        print("camera isnt work\n")
        connector.send(connType, connector, f"C_{2} A_{0}")
    
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
    print("\nWaiting data...\n") 
    while True:
        try:                
            data = server.serverRcv()
            if data.strip().lower() == items['Receive']:
                # print("Received from client: " + str(data))
                # Thread(target=threadCap, args=("server", server)).start()
                # Wait for the task to complete
                executor.submit(threadCap, "server", server)
            else:
                # server.serverSend(items['Send'])
                # print("Incorrect message!\n")
                server.close()
                serverProgram()
        except Exception as e:
            # server.serverSend(items['Send'])
            print(e)
        except KeyboardInterrupt:
            pipeline.stop() # Close pipeline
            server.close()  # Close connection
            break
    
    # server.close() # Close connection

def clientProgram():
    print("Current role is client!")
    # Make connection
    client = SocketConnection(items['Host'], int(items['Port']))
    client.clientConnect()
    print("Waiting data...\n") 
    while True:
        try:            
            data = client.clientRcv() # Listening signal from server
            if data.strip().lower() == items['Receive']:                
                # Thread(target=threadCap, args=("server", server)).start()
                # Wait for the task to complete
                executor.submit(threadCap, "client", client)
            else:
                #client.clientSend(items['Send'])
                #print("Incorrect message!\n")
                clientProgram()
        except Exception as e:
            # client.clientSend(items['Send'])
            print(e)
        except KeyboardInterrupt:
            pipeline.stop() # Close pipeline
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
    # Config Realsense pipeline for color stream 
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

    # Start the pipeline
    profile = pipeline.start(config)

    # Align object to align frames to color stream
    align_to = rs.stream.color 
    align = rs.align(align_to)


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
    modelDeploy = YOLOInference(preTrainedModelPath, labelPath, classPath)

    # [{Name: 'server'}, {Receive: 'a'}, {Send: 'b'}, {Port: 3000}, {Host: '192.168.137.226'}]
    items = configYmlFile()
    # for key, values in items.items():
    #     print(key + " : " + str(values)) # Co the bo qua

    main()
