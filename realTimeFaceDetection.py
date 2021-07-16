# -*- coding: utf-8 -*-
"""
@author: Russa
"""

import cv2

# Load the cascade
face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    # Read input video & Detect faces
    check, frame = video.read()
    faces = face_detection.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    # Draw rectangle around the faces
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
     # Open (Face Detector) window to show the output   
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    # Stop the run
    if key == ord('q'):
        beake

video.release()
cv2.destroyAllWindows()
