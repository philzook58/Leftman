import car
import time
import picamera
import picamera.array
import cv2

radius = 5

myCar = car.Car()

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    while True:
	with picamera.array.PiRGBArray(camera) as stream:
		camera.capture(stream, format='bgr')
        	# At this point the image is available as stream.array
        	image = stream.array
        	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        	#blur = cv2.GaussianBlur(gray, (radius, radius), 0)
        	(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
        	print(maxLoc[0])
		if maxLoc[0] < 200:
			myCar.right() 
		elif maxLoc[0] > 520:
			myCar.left()
		time.sleep(0.1)
		myCar.forward()
		time.sleep(0.1)
		myCar.stop()
		myCar.center()
