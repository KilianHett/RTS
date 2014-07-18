#!/usr/bin/python

import time
import picamera
from PIL import Image
from PIL import ImageOps
import numpy
import os

# Convertion Image -> numpy
def cvtMatrice(img):
	data=img.getdata();
	m=numpy.matrix(data);
	w,h=img.size;
	return numpy.reshape(m, (w, h));

# Convertion numpy -> Image
def cvtImage(matrice):
	img=Image.new("L", (matrice.shape[1], matrice.shape[0]));
	img.putdata((list(matrice.flat)));
	return img;

# Prendre une image avec la camera
def takeImage(camera, def_w, def_h, t_wait, preview=False):
	stream=open("image.data","w+b");
	buf_w=(def_w%32);
	buf_h=(def_h%16);
	if not buf_w==0:
		coef_w=def_w/32;
		w=32*(coef_w+1);
	else:
		w=def_w;
	if not buf_h==0:
		coef_h=def_h/16;
		h=16*(coef_h+1);
	else:
		h=def_h;
	try:
		camera.resolution=(w,h);
		if(preview):
			camera.start_preview();
		time.sleep(t_wait);
		camera.capture(stream, "rgb");
		stream.seek(0);
	finally:
		camera.close();
	print def_h+buf_h;
	m=numpy.fromfile(stream, dtype=numpy.uint8).\
			reshape(h, w, 3);#\
			#[:def_h,:def_w,:];
	m=m.astype(numpy.float);
	os.remove("image.data");	
	return m/255.;


def toGrayScale(im):
	return (im[:,:,0] + im[:,:,1] + im[:,:,2])/3;



# Capture via picamera
camera=picamera.PiCamera();
im=takeImage(camera, 400, 400, 2, preview=True);
im=toGrayScale(im);
image=cvtImage(im*255.);
image.save(fp="test.jpg");

#try:
#	camera.resolution=(400,400);
#	time.sleep(1);
#	camera.capture("test.jpg");
#finally:
#	camera.close();


# Chargement et convertion de l'image en matrice ( numpy )
#h=Image.open("base.jpg");
#img=Image.open("test.jpg");
#img=ImageOps.grayscale(img);
#im=cvtMatrice(img);

# Transformer de fourrier 2D (fft)
fft=numpy.fft;
fim=fft.fft2(im);

#fxcorr=numpy.dot(fim,fh);
#xcorr=fft.ifft2(fxcorr);
#ximg=cvtImage(xcorr);
#ximg.save(fp="xcorr.png");

fim=fft.fftshift(fim);
fim=numpy.absolute(fim);
img=cvtImage(fim);
img.save(fp="fft_test.png");



#with picamera.PiCamera() as camera:
#	camera.start_preview();
#	camera.resolution = (1024,768);
#	#camera.start_preview();
#	camera.capture('test.jpg');

