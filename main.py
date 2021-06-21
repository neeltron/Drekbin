# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:27:29 2021

@author: Neel
"""

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/Downloads/cognitio-7378d-f0c72d841d75.json"

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
sleep(5)
camera.capture('a.jpg')
