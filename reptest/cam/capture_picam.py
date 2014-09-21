#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import numpy
from cv2 import *
import math
#from PIL import Image
#from PIL import ImageOps
import picamera
import picamera.array

if __name__=="__main__":
	with picamera.PiCamera() as camera:
		namedWindow("capture");
		camera.resolution = (640,400);
		with picamera.array.PiRGBArray(camera) as stream:
			while (True):
				camera.capture(stream, "bgr");
				imshow("capture",stream.array);
				ch=0xFF&waitKey(1);
				if ch==27:
					break;
				stream.seek(0);

