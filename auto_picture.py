from time import sleep
from picamera import PiCamera
from ControlCarLib import Car
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
driveTime = 0.2
picNum = 10
car = Car()
sleep(2)

for i in range(picNum)
	car.forward()
	sleep(driveTime)
	car.stop()
	sleep(0.1)
	camera.capture('img/'str(i) + '.jpg')

