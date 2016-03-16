#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import sys 
import subprocess 

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
getch = _GetchUnix()

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

direction = ""
while (True):
    if getch() == "w":
        if direction != "forward":
            print "Going forward"
        direction = "forward"
        motor1.run(Adafruit_MotorHAT.FORWARD)
        motor2.run(Adafruit_MotorHAT.FORWARD)
    elif getch() == "a":
        if direction != "left":
            print "Going left"
        motor1.run(Adafruit_MotorHAT.BACKWARD)
        motor2.run(Adafruit_MotorHAT.FORWARD)
        direction = "left"
    elif getch() == "s":
        if direction != "reverse":
            print "Going backward"
        motor1.run(Adafruit_MotorHAT.BACKWARD)
        motor2.run(Adafruit_MotorHAT.BACKWARD)
        direction = "reverse"
    elif getch() == "d":
        if direction != "right":
            print "Going right"
        motor1.run(Adafruit_MotorHAT.FORWARD)
        motor2.run(Adafruit_MotorHAT.BACKWARD)
        direction = "right"
    elif getch() == "q":
        print "Terminating"
        exit()
