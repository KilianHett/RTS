#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import math
import libport


COEF=10**(-4);
class Servo:
	_DeadBand=10**(-4);
	_Timp=0;
	_Tc=15*_DeadBand;
	_T=25*_DeadBand;
	def __init__(self, port):
		self._port=port;
		self._status=False;
		self.bornes(-180, 180);
	def bornes(self, bmin, bmax):
		self._min=bmin;
		self._max=bmax;
	def __routine__(self):
		global COEF;
		while (self._status):
			if (self._Timp+self._Tc>=0):
				Teff=self._Tc+self._Timp;
			self._port.write(1);
			time.sleep(Teff);
			self._port.write(0);
			time.sleep(self._T-Teff);
		print "Fin";
	def configure_servo(self, imin, imax, db):
		self._Tc=(imin+imax)/2.;
		self._T=imax;
		self_DeadBand=db;
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
		self._Timp=(10.*(teta/180.))*self._DeadBand;
		return self._Timp;


