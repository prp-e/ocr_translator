""" Main code """ 

import cv2 
import easyocr 
import requests

reader = easyocr.Reader(['en'], gpu=False)
camera = cv2.VideoCapture(0)

while True:
    _, image = camera.read()
    cv2.imshow('Camera', image)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 


