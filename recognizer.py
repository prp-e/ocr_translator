import cv2 
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
pytesseract_config = r'--oem 2'

image = cv2.imread("images/street.jpg")
image_processed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_data = pytesseract.image_to_data(image_processed, config=pytesseract_config)

for count, datum in enumerate(image_data.splitlines()):
    if count != 0:
        datum = datum.split()
        if len(datum) == 12:
            text = datum[11]
            x,y,w,h = int(datum[6]), int(datum[7]), int(datum[8]), int(datum[9])
            print(text)
            cv2.rectangle(image, (x,y), (w+x, h+y), (255, 0, 85), 5)

cv2.imshow("image", image)
cv2.waitKey(0)