import car
import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    image = np.empty((480, 640, 3), dtype=np.uint8)
    camera.capture(image, 'bgr')
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray, (radius, radius), 0)
    #(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)
    #print(maxLoc)
