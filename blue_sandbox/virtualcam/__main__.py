#

import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat

cap = cv2.VideoCapture(0)  # Capture video from the first webcam

with pyvirtualcam.Camera(width=640, height=480, fps=20, fmt=PixelFormat.BGR) as cam:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process frame (apply your functions here)
        processed_frame = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )  # Example: convert to grayscale

        cam.send(processed_frame)
        cam.sleep_until_next_frame()
