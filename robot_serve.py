import RPi.GPIO as GPIO
from time import sleep
import socket
import cPickle as pickle
 
GPIO.setmode(GPIO.BCM)
 

ForwardPin = 16
BackwardPin = 18
'''
 Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19
'''
 
GPIO.setup(ForwardPin,GPIO.OUT)
GPIO.setup(BackwardPin,GPIO.OUT)

 
def forward():
	print "Going forwards"
	GPIO.output(ForwardPin,GPIO.HIGH)
	GPIO.output(BackwardPin,GPIO.LOW)

def backward():
	print "Going backwards"
	GPIO.output(ForwardPin,GPIO.LOW)
	GPIO.output(BackwardPin,GPIO.HIGH)

def stop():
	GPIO.output(ForwardPin,GPIO.LOW)
	GPIO.output(BackwardPin,GPIO.LOW)




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
    	forward()


GPIO.cleanup()