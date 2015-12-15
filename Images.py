# -*- coding: utf-8 -*-

from DSP_Utils import size

from PIL import Image

# SOURCE: http://www.sitepoint.com/manipulating-images-with-the-python-imaging-library/
#		  http://stackoverflow.com/questions/1109422/getting-list-of-pixel-values-from-pil
#		  http://effbot.org/imagingbook/image.htm
#		  http://sourcedexter.com/2013/08/27/extracting-pixel-values-of-an-image-in-python/
#		  http://stackoverflow.com/questions/29637191/python-pil-putdata-method-not-saving-the-right-data


#EJEMPLO PARA LA MANIPULACIÓN DE IMÁGENES
#imagen = imread('matlab.png')
#imagen = rgb2gray(imagen)
#imshow(imagen)

def imread(filename,gray=False):

	im = Image.open(filename)
	if not gray:
		pixels = list(im.getdata())
		width, height = im.size
		pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
	else:
		im = im.convert('L')		
		pixels = list(im.getdata())
		width, height = im.size
		pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

	return pixels


def rgb2gray(dataMat,formato = 'RGB'):
	
	formatConv = 'L'  #Formato para convertir a escala de grices
	m,n = size(dataMat)
	lista1D = List1D(dataMat)
	
	imagine = Image.new(formato,(n,m))
	imagine.putdata(lista1D)
	imagine = imagine.convert(formatConv) #Nueva imagen en escala de grices

	#Nuevamente se convierte a forma matricial
	pixelsList = list(imagine.getdata())
	width, height = imagine.size
	matriz = ImageMat(pixelsList,height,width) 

	return matriz


def imshow(data,formato="RGB"):
	m,n = size(data)
	dataL = List1D(data)
	if type(dataL[0]) == int: #para imágenes en escala de grices
		formato = "L"
	imagen = Image.new(formato,(n,m))
	imagen.putdata(dataL)
	imagen.show()

def ImageMat(Lista1D,m,n): #Image reconstruction (volver a forma matricial)
	imagemat = [Lista1D[i * n:(i + 1) * n] for i in xrange(m)]
	return imagemat

def List1D(data):
	#EJEMPLO: 
	#lista = [[(1,2,3),(3,2,1)],[(8,7,6),(7,5,3)],[(3,8,9),(9,4,5)]]
	#print List1D(lista)
	m,n = size(data)

	if type(data[0][0]) == tuple:
		lista = [(0,0,0) for k in range(m*n)]
	elif type(data[0][0]) == int:  #else, is gray-scale
		lista = [0 for k in range(m*n)]

	h = 0
	for k in range(m):
		for j in range(n):
			lista[h] = data[k][j]
			h += 1

	return lista
