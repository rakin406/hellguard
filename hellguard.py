#!/usr/bin/env python3
"""
Home surveillance
"""

import os
import sys
import time
import datetime
import cv2

# Create directory to store pictures
PIC_DIR = "surveillance-pictures"
if not os.path.exists(PIC_DIR):
    os.makedirs(PIC_DIR)

CASC_PATH = sys.argv[1]
FACE_CASCADE = cv2.CascadeClassifier(CASC_PATH)

# Get webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = FACE_CASCADE.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
            )

    # Save image if face is detected
    if len(faces) > 0:
        file_name = PIC_DIR + "/" + str(datetime.datetime.now()) + ".png"
        cv2.imwrite(file_name, frame)
        time.sleep(1)

# When everything is done, release the capture
video_capture.release()
