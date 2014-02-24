#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../lib");
import libservo
import libport
import Getch

def controle():
	i=0;
	k='0';
	getch=Getch._Getch();
	#p22=libport.Port(22, libport.Port.OUT);
	pext=libport.ExtPort(7, 0x20, libport.ExtPort.IN);
	servo=libservo.Servo(pext);
	servo.start();
	while (not k=='c'):
		k=getch();
		if (k=='q'):
			i=i-0.5;
		elif (k=='d'):
			i=i+0.5;
		elif (k=='s'):
			i=0;
		print ("{0} rad".format(i));
		print servo.Tc+servo.rotate(i);
	servo.stop();
controle();
