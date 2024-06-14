# Select and use the correct version of the l4t-pytorch container
# Go to the NVIDIA NGC website: https://ngc.nvidia.com.

FROM  dustynv/l4t-pytorch:r35.4.1

WORKDIR /home

COPY . .
   
RUN apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install ultralytics && \
    pip install onnx onnxruntime && \
    pip install "opencv-python-headless<4.3" && \
    pip install numpy --upgrade  && \
    pip install numpy==1.23.5 && \
    pip install pyrealsense2

# Command to run the application
CMD ["python3", "./utils/main.py"]
    

