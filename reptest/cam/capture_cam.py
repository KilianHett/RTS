#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import numpy
from cv2 import *
import math
from PIL import Image
from PIL import ImageOps
import video


if __name__=="__main__":
	cam=video.create_capture(0);
	namedWindow("capture");
	while (True):
		ret, frame = cam.read();
		im=frame.copy();
		imshow("capture", im);
		ch=0XFF&waitKey(5);
		if ch==27:
			break;
	imwrite("capture.jpg", im);
