""" Main code """ 

from flask.globals import request
import cv2 
import json 
import numpy as np
import requests
import time 

camera = cv2.VideoCapture(0)
while True:
    _, image = camera.read()
    cv2.imshow('Camera', image)
    time.sleep(.5)
    #print(image)
    image_data = {'image': image.tolist()}
    r = requests.post('http://localhost:5000/', json=image_data)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 


