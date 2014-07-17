#!/usr/bin/python

import time
import picamera
from PIL import Image
import numpy


camera=picamera.PiCamera();
try:
	time.sleep(10);
	camera.capture("test.jpg");
finally:
	camera.close();



im=Image.open("test.jpg");



#with picamera.PiCamera() as camera:
#	camera.start_preview();
#	camera.resolution = (1024,768);
#	#camera.start_preview();
#	camera.capture('test.jpg');

