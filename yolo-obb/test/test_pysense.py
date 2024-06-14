import pyrealsense2 as rs
import numpy as np
import cv2

# Configure RealSense pipeline for color stream
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

# Start the pipeline
profile = pipeline.start(config)

# Align object to align frames to color stream
align_to = rs.stream.color
align = rs.align(align_to)

# for i in range(num_images):ss
while True:
    # Wait for frames and align them
    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)
    color_frame = aligned_frames.get_color_frame()
    
    if not color_frame:
        print("Failed to capture color frame")
        continue
    
    # Convert frame to numpy array
    color_image = np.asanyarray(color_frame.get_data())
    
    # Display the captured image
    cv2.imshow('Align Example', color_image)
    
    
    # Wait for a key press and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
pipeline.stop()
