import easyocr 
import time

reader = easyocr.Reader(['en'], gpu=False)
while True:
    image_data = reader.readtext('output.jpg')
    print(image_data)
    time.sleep(1)