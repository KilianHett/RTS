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
	IN=1;
	OUT=0;
	def __init__(self, num, addr, mode):
		assert num<16 and num>=0, "Bad pin number"; 
		self._nump=num;
		self._i2c=libi2c.I2C(addr);
		if (num<8):
			self._portmap=self._i2c.readU8(IODIRA);
			iodirav=self._i2c.readU8(IODIRA);
			iodirav=self._changeBit(iodirav, num, mode);
			self._i2c.writeU8(IODIRA, iodirav);
			self._portmap=iodirav;
		else:
			self._portmap=self._i2c.readU8(IODIRB);
			iodirbv=self._i2c.readU8(IODIRB);
			iodirbv=self._changeBit(iodirbv, num%8, mode);
			self._i2c.writeU8(IODIRB, iodirbv);
			self._portmap=iodirbv;
		for i in range(7):
			print (self._portmap>>i)&0x1;
		print " \n\n";
	def _changeBit(self, bits, pos, v):
		if (v==0):
			return bits & ~(1<<pos);
		else:
			return bits | (1<<pos);
	def read(self):
		assert not (self._portmap&(1<<self._nump%8)==0),"bad mode";
		if (self._nump<8):
			val=self._i2c.readU8(GPIOA);
			return (val>>self._nump)&(0x1);
		else:
			val=self._i2c.readU8(GPIOB);
			return (val>>(self._nump-8))&(0x1);
	def write(self, v):
		assert (self._portmap&(1<<(self._nump%8)))==0,"bad mode";
		if (v==1 or v==0):
			if (self._nump<8):
				gpioav=self._i2c.readU8(OLATA);
				gpioav=self._changeBit(gpioav, self._nump, v);
				self._i2c.writeU16(GPIOA, gpioav);
			else:
				gpiobv=self._i2c.readU8(OLATB);
				gpiobv=self._changeBit(gpiobv, self._nump%8, v);
				self._i2c.writeU16(GPIOB, gpiobv);
		else:
			print "Error : Bad value"; 
