import car
import time
import picamera
import picamera.array
import cv2
import cv2.aruco as aruco

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    while True:
	with picamera.array.PiRGBArray(camera) as stream:
		camera.capture(stream, format='bgr')
        	# At this point the image is available as stream.array
        	image = stream.array
        	
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
		parameters =  aruco.DetectorParameters_create()

		corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    		print(corners)
