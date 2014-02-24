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
	#p22=libport.Port(22, libport.Port.OUT);
	pext=libport.ExtPort(0, 0x20, libport.ExtPort.OUT);
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
#controle();

pext=libport.ExtPort(7, 0x20, libport.ExtPort.OUT);
#print "0v";
#pext.write(0);
#time.sleep(30);
print "1v";
pext.write(1);
time.sleep(30);
print "Fin";
