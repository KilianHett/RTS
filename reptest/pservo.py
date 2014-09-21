#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys

sys.path.append("../lib");

import time
import threading
import Getch

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print ("Erreur: RPi.GPIO n'est pas disponible");


print ("{0} {1}".format("RPI VERSION  ", GPIO.RPI_REVISION));
print ("{0} {1}".format("GPIO VERSION ", GPIO.VERSION));


Tmax=1.65;
Tmin=0.9;
Tc=1.4;
To=1;
i=0;
k='0';

def controleKey():
	global i;
	global k;
	getch=Getch._Getch();
	while (not k=='c'):
		k=getch();
		if (k=='q'):# and i>-0.5):
			i=i-0.1;
		elif (k=='d'): #and i<0.35):
			i=i+0.1;
		elif (k=='s'):
			i=0;
		print((Tc+i)*(10**(-3)), " ms");

def controleServo():
	ctrl=7;
	GPIO.setmode(GPIO.BOARD);
	GPIO.setup(ctrl,GPIO.OUT);

	print ("Initialisation du servomoteur");
	cm = 10**(-3);
	while (not k=='c'):
		GPIO.output(ctrl, True);
		time.sleep((Tc+i)*cm);
		GPIO.output(ctrl, False);
		time.sleep(20*cm);
	print ("Fin");
	GPIO.cleanup();

servo = threading.Thread(None, controleServo, None);
keys = threading.Thread(None, controleKey, None);

servo.start();
keys.start();

