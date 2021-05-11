""" Main code """ 

from flask.globals import request
import cv2 
import easyocr
import numpy as np
import requests
import sys 
import time 

camera = cv2.VideoCapture(0) 
reader = easyocr.Reader(['en'], gpu=False)
fps = camera.get(cv2.CAP_PROP_FPS)
fps = int(fps) + 1
print(f'FPS : {fps}')

while True:
    _, image = camera.read()
    cv2.imwrite('output.jpg', image)
    image_data = reader.readtext('output.jpg')
    for datum in image_data:
        coordinates, text, confidence = datum 
        top_left = (int(coordinates[0][0]), int(coordinates[0][1]))
        bottom_right = (int(coordinates[2][0]), int(coordinates[2][1]))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 5)
    
    time.sleep(.75)
    cv2.imshow('Camera', image)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 