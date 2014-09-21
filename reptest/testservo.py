#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../lib");
import libservo
import libport
import Getch
import time

def controle():
	i=0;
	k='0';
	getch=Getch._Getch();
	p22=libport.Port(7, libport.Port.OUT);
	#pext=libport.ExtPort(7, 0x20, libport.ExtPort.OUT);
	servo=libservo.Servo(p22);
	#servo=libservo.Servo(pext);
	servo.start();
	while (not k=='c'):
		k=getch();
		if (k=='d'):
			i=i-1;
		elif (k=='q'):
			i=i+1;
		elif (k=='s'):
			i=0;
		print ("{0}° ".format(i));
		try:
			print servo._Tc+servo.rotate(i);
		except Exception:
			print "Error";
	servo.stop();
controle();



