""" Main code """ 

from flask.globals import request
import cv2 
import easyocr
import threading
import time 

reader = easyocr.Reader(['en'], gpu=False)
camera = cv2.VideoCapture(1) 

def image_data(image):
    print("This is a test!")

while True:
    _, image = camera.read()
    cv2.imshow('Camera', image)
    time.sleep(.15)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 


