""" Main code """ 

from flask.globals import request
import cv2 
import numpy as np
import requests
import sys 
import time 

camera = cv2.VideoCapture(0) 

fps = camera.get(cv2.CAP_PROP_FPS)
fps = int(fps) + 1
print(f'FPS : {fps}')

while True:
    _, image = camera.read()
    cv2.imshow('Camera', image)
    cv2.imwrite('output.jpg', image)
    time.sleep(.5)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 