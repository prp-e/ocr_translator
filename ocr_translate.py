""" Main code """ 

from flask.globals import request
import cv2 
import easyocr
import json 
import numpy as np
import requests
import time 

reader = easyocr.Reader(['en'], gpu=False)
camera = cv2.VideoCapture(1)
while True:
    _, image = camera.read()
    cv2.imshow('Camera', image)
    time.sleep(.15)
    #print(image)
    image_data = reader.readtext(image)
    print(image_data)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 


