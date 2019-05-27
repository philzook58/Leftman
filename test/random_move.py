from car import pwmcar
import time
from random import randint

car = pwmcar.PWMCar()

def moveRandom():
	steer = randint(0,2)
	dir = randint(0,1)
	if steer == 0:
		car.center()
	elif steer == 1:
		car.right()
	elif steer == 2:
		car.left()
	if dir == 0:
		car.forward()
	elif dir == 1:
		car.reverse()


while not car.isHome():
        print "Not Home"
        moveRandom()
        time.sleep(1)



car.stop()
