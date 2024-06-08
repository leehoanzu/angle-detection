import yaml
import sys

import os

# def getAbsPath(path):
#     # Get absolutely path
#     currentDir = os.path.dirname(os.path.abspath(__file__))

#     return os.path.abspath(os.path.join(currentDir, path))

# def extract_parent_directory(path):
#     # Chuyển đổi dấu ngã thành đường dẫn tuyệt đối
#     absolute_path = os.path.expanduser(path)
#     print("abs path first: ", absolute_path)
#     # Lấy thư mục cha của tệp
    
#     return os.path.dirname(absolute_path)

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

def load_labels(labelPath):
    # Read list label from .txt file
    with open(labelPath, 'r') as file:
        # Read all lines from the file into a list
        labels = file.readlines()
        
        # Strip whitespace characters from each label and create a list of stripped labels
        labels = [label.strip() for label in labels]

    # Return the list of stripped labels
    return labels

if __name__ == '__main__':
    def getAbsPath(path):
        # Get absolutely path
        currentDir = os.path.dirname(os.path.abspath(__file__))

        return os.path.abspath(os.path.join(currentDir, path))
    
    # Test yaml path
    items = configYmlFile()
    print("Items: ", items['Send'])

    # Test label
    label =  load_labels(getAbsPath("../label/label.txt"))
    # classId = load_labels(".././label/class.txt") # "~/../label/class.txt"
    classId = load_labels(getAbsPath("../label/class.txt"))
    # classId = load_labels(os.path.abspath(classPath)) ## ERROR
    modelpath = getAbsPath("../model/best.pt")

    print("Model path: ", modelpath)

    print(f'This is {classId[1][3:]} object at {label[90][4:]}\n') # This is blue object at Angle 90


    # print("Extract parent file: ", extract_parent_directory("../label/class.txt"))

    # print("label path: ", os.path.dirname(os.path.abspath("label.txt")))