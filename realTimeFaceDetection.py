# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 06:30:43 2021

@author: Russa
"""

import cv2


face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    faces = face_detection.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        
    cv2.imshow('Face Detector', frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        beake

video.release()
cv2.destroyAllWindows()