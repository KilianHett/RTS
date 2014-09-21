#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import math
import libport


COEF=10**(-3);
class Servo:
	Timp=0;
	Tc=10*COEF;
	T=20*COEF;
	def __init__(self, port):
		self._port=port;
		self._status=False;
		self.bornes(-120, 120);
	def bornes(self, bmin, bmax):
		self._min=bmin;
		self._max=bmax;
	def __routine__(self):
		global COEF;
		Teff=Tc;
		while (self._status):
			if (self.Tc+self.Timp>0):
				Teff=self.Tc+self.Timp;
			self._port.write(1);
			time.sleep(Teff);
			self._port.write(0);
			time.sleep(self.T-(Teff));
		print "Fin";
	def start(self):
		self._status=True;
		self._daemon=threading.Thread(None, self.__routine__, self);
		self._daemon.setDaemon(True);
		self._daemon.start();
	def stop(self):
		self._status=False;
		self._daemon.join();
	def rotate(self, teta):
		assert teta>=self._min and teta<=self._max, "Bad angle";
		self.Timp=(teta/180)*COEF;
		return self.Timp;


