#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 	       Schéma du port d'I/O
#
#         bottom    <-- left -->    top
#                   P1_1   P1_2
#  1  	3V3Power        * *    5V Power		2
#  3  	GPIO0(SDA)      * *    --		4
#  5  	GPIO1(SCL)      * *    Ground		6
#  7  	GPIO4(GPCLK0)   * *    GPIO14(TXD)	8
#  9  	--              * *    GPIO15(RXD)	10
#  11 	GPIO17          * *    GPIO18(PCMCLK)	12
#  13 	GPIO21(PCMDOUT) * *    --		14
#  15 	GPIO22          * *    GPIO23		16
#  17 	--              * *    GPIO24		18
#  19 	GPIO10(MOSI)    * *    --		20
#  21 	GPIO9(MISO)     * *    GPIO25		22
#  23 	GPIO11(SCKL)    * *    GPIO8(CEO)	24
#  25 	--              * *    GPIO7(CEL)	26
#            	   P1_25   P1_26
#   	  bottom    <-- right -->    top

import time

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print ("Erreur: RPi.GPIO n'est pas disponible");

print ("{0} {1}".format("RPI VERSION  ", GPIO.RPI_REVISION));
print ("{0} {1}".format("GPIO VERSION ", GPIO.VERSION));

# Initialisation des pins
GPIO.setmode (GPIO.BOARD);
GPIO.setup (23, GPIO.IN);
##GPIO.setup (18, GPIO.OUT);
# Mise du pins GPIO24 à 1
##GPIO.output(, 1);
# Lecture du pin 0
value = GPIO.input (23);
print (value);

while (GPIO.input(23)==0):
	time.sleep(0.5);
	print ("value : 0");

print ("Le port GPIO23 est passé à 1");


# A faire à chaque fin de programme
GPIO.cleanup();

