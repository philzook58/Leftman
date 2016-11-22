import pwmcar as car
import time
import picamera
import picamera.array
import cv2

radius = 5

myCar = car.PWMCar()

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)

    myCar.forward(25)

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
			myCar.right(100)
		elif maxLoc[0] > 520:
			myCar.left(100)
		else:
			myCar.center()
