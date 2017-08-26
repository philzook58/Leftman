from car import pwmcar
import time

car = pwmcar.PWMCar()

car.forward()

while not car.isHome():
	print "Not Home"
	time.sleep(0.1)

car.stop()


	

