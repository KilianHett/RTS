#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print ("You have not the permission");


print ("{0} {1}".format("RPI VERSION  ", GPIO.RPI_REVISION));
print ("{0} {1}".format("GPIO VERSION ", GPIO.VERSION));

pin1 = 8;
pin2 = 10;
pin3 = 12;

pp1 = 22;
pp2 = 24;
pp3 = 26;

# Initialisation
GPIO.setmode (GPIO.BOARD);
GPIO.setup (pin1, GPIO.OUT);
GPIO.setup (pin2, GPIO.OUT);
GPIO.setup (pin3, GPIO.IN);

GPIO.setup(pp1, GPIO.OUT);
GPIO.setup(pp2, GPIO.OUT);
GPIO.setup(pp3, GPIO.OUT);

# Mise de la pin à 1
##GPIO.output(pin1, False);
GPIO.output(pin1, True);
GPIO.output(pin2, False);

GPIO.output(pp1, False);
GPIO.output(pp2, False);
GPIO.output(pp3, False);


it=-1;
i=0;
while i<8:
	if not GPIO.input(pin3)==1:
		GPIO.output(pin2, False);
		it=i;
	else:
		if i==it:
			i=i+1;
			print(i);
			time.sleep(0.1);
		else:
			if i==1:
				GPIO.output(pp1,True);
				GPIO.output(pp2,False);
				GPIO.output(pp3,False);
			elif i==2:
				GPIO.output(pp1,False);
				GPIO.output(pp2,True);
				GPIO.output(pp3,False);
			elif i==3:
				GPIO.output(pp1,True);
				GPIO.output(pp2,True);
				GPIO.output(pp3,False);
			elif i==4:
				GPIO.output(pp1,False);
				GPIO.output(pp2,False);
				GPIO.output(pp3,True);
			elif i==5:
				GPIO.output(pp1,True);
				GPIO.output(pp2,False);
				GPIO.output(pp3,True);
			elif i==6:
				GPIO.output(pp1,False);
				GPIO.output(pp2,True);
				GPIO.output(pp3,True);
			elif i==7:
				GPIO.output(pp1,True);
				GPIO.output(pp2,True);
				GPIO.output(pp3,True);
			else:
				GPIO.output(pp1,False);
				GPIO.output(pp2,False);
				GPIO.output(pp3,False);
			time.sleep(0.5);


GPIO.output(pin1, False);
GPIO.output(pin2, False);


GPIO.cleanup();

