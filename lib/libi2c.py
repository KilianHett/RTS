#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smbus

class I2C:
	def __init__(self, addr):
		self._addr=addr;
		self._bus=smbus.SMBus(1);
	def writeU8(self, reg, v):
		try:
			self._bus.write_byte_data(self._addr, reg, v);
		except IOError, err:
			return "Error : write data";
	def readU8(self, reg):
		try:
			return self.read_byte_data(self._addr, reg);
		except IOError, err:
			return "Error : read data";
	def writeBlock(self, reg, b):
		try:
			self._bus.write_block_data(self._addr, reg, b);
		except IOError, err:
			return "Error : write block";
	def readBlock(self, reg, length):
		try:
			return self._bus.read_block_data(self._addr, reg, length);
		except IOError, err:
			return "Error : read data";
		
		



















