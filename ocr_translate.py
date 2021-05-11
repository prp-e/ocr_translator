""" This code checks for macOS, if you have SSL problem with any other OS's, please add it to the code """
import sys

if sys.platform == 'darwin':
    import requests 

    requests.packages.urllib3.disable_warnings() 

    import ssl 

    try:

        _create_unverified_https_context = ssl._create_unverified_context 

    except AttributeError: 

        pass 

    else: 
        ssl._create_default_https_context = _create_unverified_https_context

""" Main code """ 

import cv2 
import easyocr 

reader = easyocr.Reader(['en'], gpu=False)

camera = cv2.VideoCapture(0)

while True:
    _, image = camera.read()

    cv2.imshow('Camera', image)
    exit = cv2.waitKey(30) & 0xff
    if exit == 27:
        break 