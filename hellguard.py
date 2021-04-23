#!/usr/bin/env python3
"""
Home surveillance
"""

import sys
import cv2

CASC_PATH = sys.argv[1]
FACE_CASCADE = cv2.CascadeClassifier(CASC_PATH)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
            )

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
