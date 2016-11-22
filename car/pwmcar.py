import RPi.GPIO as GPIO

class PWMCar():
	def __init__(self, fwd = 16, rev = 18, left = 26, right = 19 ):

		GPIO.setmode(GPIO.BCM)

		GPIO.setup(fwd,GPIO.OUT)
		GPIO.setup(rev,GPIO.OUT)
		GPIO.setup(left,GPIO.OUT)
		GPIO.setup(right,GPIO.OUT)

		self.forwardPWM = GPIO.PWM(fwd, 100)
		self.reversePWM = GPIO.PWM(rev, 100)
		self.leftPWM = GPIO.PWM(left, 100)
		self.rightPWM = GPIO.PWM(right, 100)

		self.stop()
		self.center()

	def left(self, dc):
		self.leftPWM.start(dc)
		self.rightPWM.stop()

	def right(self, dc):
		self.rightPWM.start(dc)
		self.leftPWM.stop()

	def center(self):
		self.leftPWM.stop()
		self.rightPWM.stop()


	def forward(self, dc):
		self.forwardPWM.start(dc)
		self.reversePWM.stop()

	def reverse(self, dc):
		self.reversePWM.start(dc)
		self.forwardPWM.stop()

	def stop(self):
		self.forwardPWM.stop()
		self.reversePWM.stop()
