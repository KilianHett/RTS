#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import numpy
from cv2 import *
import math
from PIL import Image
from PIL import ImageOps
import picamera
import picamera.array

if __name__=="__main__":
	camera=picamera.PiCamera();
	namedWindow("capture");
	with picamera.array.PiRGBArray(camera) as stream:
		while (True):
			camera.capture(stream);
			imshow("capture",stream);
			ch=0xFF&waitKey(5);
			if ch==27:
				break;
	camera.close();
