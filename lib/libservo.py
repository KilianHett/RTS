#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import math
import libport

class Servo:
	_Unit=(10.)**(-4.);
	_Timp=0.;
	_Tmin=10.*_Unit;
	_Tc=15.*_Unit;
	_Tmax=20.*_Unit;
	def __init__(self, port):
		self._port=port;
		self._status=False;
		self.bornes(-90, 90);
	def bornes(self, bmin, bmax):
		self._min=bmin;
		self._max=bmax;
	def __routine__(self):
		while (self._status):
			if (self._Timp+self._Tc>=self._Tmin and 
				self._Timp+self._Tc<=self._Tmax):
				Teff=self._Tc+self._Timp;
			self._port.write(1);
			time.sleep(Teff);
			self._port.write(0);
			time.sleep(self._Tmax-Teff);
		print "Fin";
	def configureImpulse(self, imin, imax, db):
		self._Tc=(imin+imax)/2.;
		self._Tmax=imax;
		self._Tmin=imin;
		self_Unit=db;
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
		self._Timp=(self._Tmax-self._Tmin)*(teta/180.);
		return self._Timp;


