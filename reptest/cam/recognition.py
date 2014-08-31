#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import numpy as np
from cv2 import *
import math


def loadBar(percent, char='='):
	print('|', end='');
	n=0;
	percent=percent;
	while(n<100):
		if (n<percent):
			print (char, end='');
		else:
			print (' ', end='');
		n=n+1;
	msg="| {0}%   \r".format(percent);
	print(msg, end='');

class recognition:
	def houghCircle1(self, im, thresold=50, min=10, max=100, showed=True, 
			debug=True):
		edge=Canny(im,50,70);
		if (showed):
			namedWindow("canny");
			imshow("canny",edge);
		w,h=edge.shape;
		print (w,h);
		xi=min;
		upsi=min;
		accumulator=[];
		finish=(w-2*min)*(h-2*min);
		while (xi<w-min):
			upsi=min;
			while (upsi<h-min):
				rho=min;
				while (rho<max):
					teta=0;
					counts=0;
					while (teta<2*math.pi):
						_x=xi+math.cos(teta)*rho;
						_y=upsi+math.sin(teta)*rho;
						if (self.inFrame([w,h], [_x,_y]) and edge[_x,_y]>0):
							counts=counts+1;
							if (debug):
								print (_x,_y,edge[_x,_y]);
						teta=teta+0.01;
					if (counts>thresold):
						accumulator=accumulator+[(xi,upsi,rho)];
					rho=rho+1;
				upsi=upsi+1;
			xi=xi+1;
			percent=100*((w-2*min)*(xi-min))/finish;
			loadBar(percent);
		print ("");
		print (accumulator);
		return edge;
	def houghCircle2(self, im, treshold=50, showed=True, debug=True):
		edge=Canny(im, 50, 70);
		if (showed):
			namedWindow("canny");
			imshow("canny", edge);
		w,h=edge.shape;
		if (debug):
			print (w,h);
		edgeDetected=[];
		for i in range(0,w):
			for j in range(0,h):
				if (edge[i,j]>0):
					edgeDetected=edgeDetected+[(i,j)];
		if (debug):
			print (edgeDetected);
		for p in edgeDetected:
			xi,upsi=p;
	def houghLine(self, im):
		return im;
	def inFrame(self, frame, point):
		return point[0]>=0 and point[0]<frame[0] and point[1]>=0 and point[1]<frame[1];


def __main__(param):
	img=imread("test.jpg");
	namedWindow("test");
	imshow("test", img);
	reco=recognition();
	edge=reco.houghCircle1(img, 40, 70, 250, True, False);
	waitKey(0);
	return;



## Test de la lib ##
param=0;
__main__(param);

