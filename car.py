import RPi.GPIO as GPIO

class Car():
	def __init__(self, fwd = 16, rev = 18, left = 26, right = 19 ):

		self.forwardPin = fwd
		self.reversePin = rev
		self.leftPin = left
		self.rightPin = right

		GPIO.setmode(GPIO.BCM)


		GPIO.setup(self.forwardPin,GPIO.OUT)
		GPIO.setup(self.reversePin,GPIO.OUT)
		GPIO.setup(self.leftPin,GPIO.OUT)
		GPIO.setup(self.rightPin,GPIO.OUT)
		self.stop()
		self.center()

	def left(self):
		GPIO.output(self.leftPin,GPIO.HIGH)
		GPIO.output(self.rightPin,GPIO.LOW)


	def right(self):
		GPIO.output(self.rightPin,GPIO.HIGH)
		GPIO.output(self.leftPin,GPIO.LOW)

	def center(self):
		GPIO.output(self.rightPin,GPIO.LOW)
		GPIO.output(self.leftPin,GPIO.LOW)


	def forward(self):
		GPIO.output(self.forwardPin,GPIO.HIGH)
		GPIO.output(self.reversePin,GPIO.LOW)

	def reverse(self):
		GPIO.output(self.forwardPin,GPIO.LOW)
		GPIO.output(self.reversePin,GPIO.HIGH)

	def stop(self):
		GPIO.output(self.forwardPin,GPIO.LOW)
		GPIO.output(self.reversePin,GPIO.LOW)
