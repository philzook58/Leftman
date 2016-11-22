import RPi.GPIO as GPIO

ForwardPin = 16
BackwardPin = 18

LeftPin = 26
RightPin = 19

class Car():
	__init__(self):
		GPIO.setmode(GPIO.BCM)
 
 
		GPIO.setup(ForwardPin,GPIO.OUT)
		GPIO.setup(BackwardPin,GPIO.OUT)
		GPIO.setup(LeftPin,GPIO.OUT)
		GPIO.setup(RightPin,GPIO.OUT)
		self.stop()
		self.center()

	def left(self):
		GPIO.output(LeftPin,GPIO.HIGH)
		GPIO.output(RightPin,GPIO.LOW)


	def right(self):
		GPIO.output(RightPin,GPIO.HIGH)
		GPIO.output(LeftPin,GPIO.LOW)

	def center(self):
		GPIO.output(RightPin,GPIO.LOW)
		GPIO.output(LeftPin,GPIO.LOW)


	def forward(self):
		GPIO.output(ForwardPin,GPIO.HIGH)
		GPIO.output(BackwardPin,GPIO.LOW)

	def backward(self):
		GPIO.output(ForwardPin,GPIO.LOW)
		GPIO.output(BackwardPin,GPIO.HIGH)

	def stop(self):
		GPIO.output(ForwardPin,GPIO.LOW)
		GPIO.output(BackwardPin,GPIO.LOW)


