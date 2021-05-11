""" Main code """ 

from flask.globals import request
import cv2 
import numpy as np
import requests
import time 

reader = easyocr.Reader(['en'], gpu=False)
camera = cv2.VideoCapture(1) 

fps = camera.get(cv2.CAP_PROP_FPS)
fps = int(fps) + 1
print(f'FPS : {fps}')


def image_data(image):
    print("This is a test!")

while True:
    _, image = camera.read()
    cv2.imshow('Camera', image)
    time.sleep(1/3.0)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 