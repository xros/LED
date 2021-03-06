#!/usr/bin/env python2
# coding: utf-8

import wiringpi
from time import sleep
"""
A blink.py to light on/off LED on Raspberry Pi using wiringpi
Created by Songhua
liusongh@gmail.com
"""
# Change log: This works with wiringpi in year 2012 - 2013
#io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS) # Create an object
# Change log: This works with wiringpi in year 2016
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO) # Create an object
io.pinMode(18,io.OUTPUT)		# initiate pin 18
while True:
	io.digitalWrite(18,io.HIGH)	#Turn on light
	print "LED light is on" 
	sleep(1)
	io.digitalWrite(18,io.LOW)	#Turn off light
	print "LED light is off" 
	sleep(1)
