""" Main code """ 

import cv2 
import requests
import time 

camera = cv2.VideoCapture(0)
while True:
    _, image = camera.read()
    cv2.imshow('Camera', image)
    time.sleep(.5)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 


