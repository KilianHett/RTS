

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import numpy
from cv2 import *
import math
from PIL import Image
from PIL import ImageOps

def cvtMatrice(img):
	data=img.getdata();
	m=numpy.array(data);
	m=m.astype(numpy.float);
	m/=255.;
	w,h=img.size;
	return m.reshape(h, w);


# Convertion numpy -> Image
def cvtImage(matrice):
	img=Image.new("L", (matrice.shape[1], matrice.shape[0]));
	img.putdata((list(matrice.flat)));
	return img;

##
## Test avec une intercorrelation par fft
##
im=Image.open("test.jpg");
im=ImageOps.grayscale(im);
x=cvtMatrice(im);

him=Image.open("test.jpg");
him=ImageOps.grayscale(him);
h=cvtMatrice(him);

#empty=numpy.zeros((x.shape[0], x.shape[1]));
#empty=empty.astype(numpy.float);
#empty[:h.shape[0],:h.shape[1]]=h[:,:];
#h=empty;

fft=numpy.fft;
fX=fft.fft2(x);
fH=fft.fft2(h);

#fX=fft.fftshift(fX);
#fH=fft.fftshift(fH);

fxcorr=fX*fH;

xcorr=fft.ifft2(fxcorr);

xcorr=numpy.absolute(xcorr);
m=numpy.amax(xcorr.flat);
xcorr_norm=(xcorr/m)*255;
print (xcorr/m);

xcorr=cvtImage(numpy.absolute(xcorr_norm));
xcorr.save(fp="xcorr.jpg");
xcorr_fft=imread("xcorr.jpg");
namedWindow("fft_xcorr");
imshow("fft_xcorr",xcorr_fft);

## 
## Test avec la fonction matchTemplate opencv
##

im=imread("test.jpg");
him=imread("element.jpg");

namedWindow("Image");
namedWindow("Patch");
imshow("Image", im);
imshow("Patch", him);

xcorr_cv=matchTemplate(im, him, TM_SQDIFF_NORMED);
mi,ma,miLoc,maLoc=minMaxLoc(xcorr_cv);
f_x, f_y = maLoc;
f_x=(im.shape[0]/xcorr_cv.shape[0])*f_x + h.shape[0]/2;
f_y=(im.shape[0]/xcorr_cv.shape[0])*f_y + him.shape[1]/2;


print (f_x,f_y);
namedWindow("cv2_xcorr");
imshow("cv2_xcorr",xcorr_cv);
imshow("Image", im);
waitKey(0);




