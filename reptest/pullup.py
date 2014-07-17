#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../lib");
import Getch
import libport


def pull():
	getch=Getch._Getch();
	pin=libport.Port(3, libport.Port.IN);
	pout=libport.Port(5, libport.Port.OUT);
	k='0';
	while (not k=='q'):
		k=getch();
		if (k=='o'):	
			pout.write(1);
		elif (k=='f'):
			pout.write(0);
		v=pin.read();
		print "la tension est de {0} v :".format((v*3.3));


pull();



