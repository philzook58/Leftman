import RPi.GPIO as GPIO

class PWMCar():
	def __init__(self, fwd = 16, rev = 18, left = 26, right = 19 ):

		GPIO.setmode(GPIO.BCM)

		GPIO.setup(fwd,GPIO.OUT)
		GPIO.setup(rev,GPIO.OUT)
		GPIO.setup(left,GPIO.OUT)
		GPIO.setup(right,GPIO.OUT)

		self.forward = GPIO.PWM(fwd, 100)
		self.reverse = GPIO.PWM(rev, 100)
		self.left = GPIO.PWM(left, 100)
		self.right = GPIO.PWM(right, 100)

		self.stop()
		self.center()

	def left(self, dc):
		self.left.start(dc)
		self.right.stop()

	def right(self, dc):
		self.right.start(dc)
		self.left.stop()

	def center(self):
		self.left.stop()
		self.right.stop()


	def forward(self, dc):
		self.forward.start(dc)
		self.reverse.stop()

	def reverse(self, dc):
		self.reverse.start(dc)
		self.forward.stop()

	def stop(self):
		self.forward.stop()
		self.reverse.stop()
