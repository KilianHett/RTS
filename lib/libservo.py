#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import math
import libport


COEF=10**(-3);
class Servo:
	Timp=0;
	Tc=1.25*COEF;
	T=20*COEF;
	def __init__(self, port):
		self._port=port;
		self._status=False;
	def __routine__(self):
		global COEF;
		while (self._status):
			Teff=abs(self.Tc+self.Timp);
			self._port.write(1);
			time.sleep(Teff);
			self._port.write(0);
			time.sleep(self.T-Teff);
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
		self.Timp=(teta/math.pi)*COEF;
		return self.Timp;


