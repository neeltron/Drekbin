# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:36:33 2021

@author: Neel
"""


import RPi.GPIO as GPIO
from time import sleep

def servoAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(11, True)
	p.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(11, False)
	p.ChangeDutyCycle(0)
    


GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(0)
servoAngle(90)
sleep(2)
servoAngle(0)