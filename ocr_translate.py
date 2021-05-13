""" Main code """ 

import cv2 
import easyocr 
import time 

def read_image_data(image):
    image_data = reader.readtext(image, workers=1)
    texts = []
    for datum in image_data:
        coordinates, text, confidence = datum 
        top_left = (int(coordinates[0][0]), int(coordinates[0][1]))
        bottom_right = (int(coordinates[2][0]), int(coordinates[2][1]))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 5) 

def camera_data(camera):
    while True:
        _, image = camera.read()
        cv2.imshow('Camera', image)
        exit = cv2.waitKey(30) & 0xff
        if exit == 32:
            cv2.imwrite(file_name, image)
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    """ Global Variables """
    camera = cv2.VideoCapture(0) 
    reader = easyocr.Reader(['en'], gpu=False)
    file_name = 'photo_taken.jpg'
    fps = camera.get(cv2.CAP_PROP_FPS)
    fps = int(fps) + 1
    print(f'FPS : {fps}')

    camera_data(camera=camera)

    image_to_recognize = cv2.imread(file_name)
    cv2.imshow('Result', image_to_recognize)
