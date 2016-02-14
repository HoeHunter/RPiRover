#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import sys 

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)
#define motors
motor1 = mh.getMotor(3)
motor2 = mh.getMotor(4)

while (True):
	#get command data
	command = raw_input("\nPlease enter a command:\n ")
	#parse command data to variables
	direction = command.split(' ')[0]
	distance = float(command.split(' ')[1])
	speed = int(command.split(' ')[2])
	if direction == "forward" or direction == "reverse" or direction == "left" or direction == "right":		
		#convert speed to m/s and degrees/s
		if speed == 25:
			speedms = .02
			degms = 5
		elif speed ==  50:
			speedms = .05
			degms = 15
		elif speed == 75:
			speedms = .08
			degms = 25
		elif speed == 100:
			speedms = .1
			degms = 35

		motor1.setSpeed(speed)
		motor2.setSpeed(speed)
	
		if direction == "forward":
			motor1.run(Adafruit_MotorHAT.FORWARD)
			motor2.run(Adafruit_MotorHAT.FORWARD)
		elif direction == "reverse":
			motor1.run(Adafruit_MotorHAT.BACKWARD)
			motor2.run(Adafruit_MotorHAT.BACKWARD)
		elif direction == "left":
			motor1.run(Adafruit_MotorHAT.BACKWARD)
			motor2.run(Adafruit_MotorHAT.FORWARD)
		elif direction == "right":
			motor1.run(Adafruit_MotorHAT.FORWARD)
			motor2.run(Adafruit_MotorHAT.BACKWARD)	

		#calculate time to distance at requested speed
		if direction == "forward" or direction == "reverse":
			timetd = distance/speedms
		elif direction == "left" or direction == "right":
			timetd = distance/degms
		totaltime = timetd
		distancerem = distance
		
		while (timetd>.1):
			time.sleep(.1)
			timetd=timetd-.1
			sys.stdout.flush()
			print "\r",
			distancerem = distance-speedms*(totaltime-timetd)
			print "Time remaining:", timetd, "Distance:", distancerem,
		motor1.run(Adafruit_MotorHAT.RELEASE)
		motor2.run(Adafruit_MotorHAT.RELEASE)
				
	if command == "help":
		print "Command format (forward/reverse): direction distance(m) speed(25, 50, 75, 100)"
		print "Example: forward 10 50"
		print "Command format (left/right): direction angle(degrees) speed(25, 50, 75, 100)"
		print "Example: left 90 50"
		
