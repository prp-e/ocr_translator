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
from flask import Flask, request
import easyocr 
import numpy as np 

reader = easyocr.Reader(['en'], gpu=False)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def magic():
    json_input = request.get_json()
    image = np.array(json_input['image'])
    image_input = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_data = reader.readtext(image_input)
    print(image_data)
    return {'output': 0}

if __name__ == '__main__':
    app.run(debug=True)