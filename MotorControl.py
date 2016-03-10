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
pan = mh.getMotor(1)
tilt = mh.getMotor(2)
motor1 = mh.getMotor(3)
motor2 = mh.getMotor(4)

#turret turn limit variables
pantrack = 0
tilttrack = 0
panlowerlimit = -180
panupperlimit = 180
tiltlowerlimit = 25
tiltupperlimit = 65

while (True):
    #get command data
    command = raw_input("\nPlease enter a command:\n ")
    if command == "help":
        print "Basic Movement:\nCommand format (forward/reverse): direction distance(m) speed(25, 50, 75, 100)\nExample: forward 10 50\nCommand format (left/right): direction angle(degrees) speed(25, 50, 75, 100)\nExample: left 90 50"
        print "Turret pan/tilt:\n Command format (pan left/right): pan left/right angle(degrees)\nExample: pan left 45\nCommand format (tilt up/down): tilt up/down angle(degrees)\nExample: tilt up 30"
        continue

    elif "turret" in command:
        pan.setSpeed(255)
        tilt.setSpeed(150)
        movetype = command.split(' ')[1]
        direction = command.split(' ')[2]
        angle = int(command.split(' ')[3])
        
        if movetype == "pan" or "tilt":
            if direction == "right":
                pantrack = pantrack + angle
            elif direction == "left":
                pantrack = pantrack - angle
            elif direction == "up"
                tilttrack = tilttrack + angle
            elif direction == "down"
                tilttrack = tiltrack + angle
            if pantrack > panupperlimit:
                exceed = pantrack - panupperlimit
                print "Error: desired amgle exceeds safety parameters by", exceed, "degrees. Aborting."
                continue
           elif pantrack < panlowerlimit:
               exceed = -1*(pantrack - panlowerlimit)
               print "Error: desired amgle exceeds safety parameters by", exceed, "degrees. Aborting."
               continue 
            degms = 5
            timetd = angle/degms
            totaltime = timetd
            degrem = angle        
            if direction == "left":
                pan.run(Adafruit_MotorHAT.FORWARD)
            elif direction == "right":
                pan.run(Adafruit_MotorHAT.BACKWARD)
            elif direction = "up":
                tilt.run(Adafruit_MotorHAT.FORWARD)
            elif direction = "down"
                tilt.run(Adafruit_MotorHAT.FORWARD)
            while (timetd>.1):
                    time.sleep(.1)
                    timetd=timetd-.1
                    sys.stdout.flush()
                    print "\r",
                    degrem = angle-degms*(totaltime-timetd)
                    print "Time remaining:", timetd, "Degrees:", degrem,
            pan.run(Adafruit_MotorHAT.RELEASE)
            tilt.run(Adafruit_MotorHAT.RELEASE)


    elif "forward" or "reverse" or "left" or "right" in command:		
        #parse command data to variables
        direction = command.split(' ')[0]
        distance = float(command.split(' ')[1])
        speed = int(command.split(' ')[2])
        if direction == "forward" or "reverse" or "left" or "right":		
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

                motor1.setSpeed((speed/100)*255)
                motor2.setSpeed((speed/100)*255)
        
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
                degrem = distance
                while (timetd>.1):
                        time.sleep(.1)
                        timetd=timetd-.1
                        sys.stdout.flush()
                        print "\r",
                        if direction == "forward" or direction == "reverse":
                                distancerem = distance-speedms*(totaltime-timetd)
                                print "Time remaining:", timetd, "Distance:", distancerem,
                        elif direction == "left" or direction == "right":
                                degrem = distance-degms*(totaltime-timetd)
                                print "Time remaining:", timetd, "Degrees:", degrem,
                motor1.run(Adafruit_MotorHAT.RELEASE)
                motor2.run(Adafruit_MotorHAT.RELEASE)
    else:
        print "Error: Invalid command syntax"	
