#!/usr/bin/python
# -*- coding: UTF-8 -*-


try:
	import RPi.GPIO as GPIO
except:
	print ("Erreur: RPi.GPIO n'est pas disponible");
	exit();

import libi2c



class Port:
	IN=GPIO.IN;
	OUT=GPIO.OUT;
	def __init__(self, num, mode):
		self._nump=num;
		self._status=mode;
		GPIO.setmode(GPIO.BOARD);
		GPIO.setup(num, mode);
	def read(self):
		return GPIO.input(self._nump);
	def write(self, v):
		if (v==True or v==False):
			GPIO.output(self._nump, v);
		else:
			print "Error :  Bad value";




# Registre pour la puce MCP23017
IODIRA=0x00;
IODIRB=0x01;
GPIOA=0x12;
GPIOB=0x13;
GPPUA=0x0C;
GPPUB=0x0D;
OLATA=0x14;
OLATB=0x15;
class ExtPort(Port):
	def __init__(self, num, addr, mode):
		self._nump=num;
		self._i2c=libi2c.I2C(addr);
		#self._i2c.writeU8(IODIRA, 0xFF);
		#self._i2c.writeU8(IODIRB, 0xFF);
		self._direction=self._i2c.readU8(IODIRA);
		self._direction|=self._i2c.readU8(IODIRB);
		if (num<8):
			iodirav=self._i2c.readU8(IODIRA);
			iodirav=self._changeBit(iodirav, num, mode);
			self._i2c.writeU8(IODIRA, iodirav);
			self._direction=iodirav;
		else:
			iodirbv=self._i2c.readU8(IODIRB);
			iodirbv=self._changeBit(iodirbv, num-8, mode);
			self._i2c.writeU8(IODIRB, iodirbv);
			self._direction=iodirbv;
	def _changeBit(self, bits, pos, v):
		if (v==0):
			bits&=~(v<<pos);
		else:
			bits|=(v<<pos);

	def read(self):
		return 0;
	def write(self, v):
		if (v==True or v==False):
			# TODO write on component
			pass;
		else:
			print "Error : Bad value"; 
