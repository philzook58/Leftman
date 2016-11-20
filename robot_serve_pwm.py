import RPi.GPIO as GPIO
from time import sleep
import socket
import cPickle as pickle
 
GPIO.setmode(GPIO.BCM)
 

ForwardPin = 16
BackwardPin = 18

frequency = 100
f = GPIO.PWM(ForwardPin, frequency)
b = GPIO.PWM(BackwardPin, frequency)

p.start(dc) # between 0 and 100



'''
 Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19
'''
 
GPIO.setup(ForwardPin,GPIO.OUT)
GPIO.setup(BackwardPin,GPIO.OUT)

 
def rangeConvert(val): #takes -1 to 1 of joystick to 0 to 100 of pwm
	return val*50.0 + 50.0

# Should I keep track of whether pin is already running or not? I'd rather not.
#p.ChangeDutyCycle(dc) 
def forward(val):
	print "Going forwards"
	b.stop()
	f.start(rangeConvert(val))

def backward():
	print "Going backwards"
	f.stop()
	b.start(rangeConvert(val))

def stop():
	b.stop()
	f.stop()




UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    xdir, rtrigger = pickle.loads(data)
    print "received message:",
    if rtrigger < -0.9:
    	stop()
    else:
    	forward(xdir)


GPIO.cleanup()