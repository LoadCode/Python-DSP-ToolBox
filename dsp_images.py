# -*- coding: utf-8 -*-

from DSP_Utils import *
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


def imshow(data,formato="RGB"):
	m,n = size(data)
	dataL = List1D(data)
	if type(dataL[0]) == float or type(dataL[0]) == int: #para imágenes en escala de grices
		formato = "L"
	imagen = Image.new(formato,(n,m))
	imagen.putdata(dataL)
	imagen.show()


def imsave(imagenMat,filename = 'Imagen sin nombre.png'):
	#Esta función almacena en disco la imagen que se le pasa con el nombre que se le indica (debe llevar extensión)
	
	formato="RGB"
	m,n = size(imagenMat)
	dataL = List1D(imagenMat)
	if type(dataL[0]) == float or type(dataL[0]) == int: #para imágenes en escala de grices
		formato = "L"
	imagen = Image.new(formato,(n,m))
	imagen.putdata(dataL)
	imagen.save(filename)


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
	matriz = matInt2Float(matriz)

	return matriz


def ImageMat(Lista1D,m,n): #Image reconstruction (volver a forma matricial)
	imagemat = [Lista1D[i * n:(i + 1) * n] for i in xrange(m)]
	return imagemat


def getPlane(imagen, pln = 'R'):
	
	#Función para obtener un plano de color determinado de una imagen RGB
	#EJEMPLO:#imagen = imread('brick-house.png')
	#imagen = rgb2gray(imagen)
	#green = getPlane(imagen,'g')
	#imshow(green)
	m,n = size(imagen)
	dataPlane = [[ (0,0,0) for h in range(m)] for x in range(n)] #Se inicializa el vector previamente

	if pln == 'r' or pln == 'R':
		plane = 0
		for i in range(n):
			for j in range(m):
				dataPlane[i][j] = (imagen[i][j][plane],0,0)
	elif pln == 'g' or pln == 'G':
		plane = 1
		for i in range(n):
			for j in range(m):
				dataPlane[i][j] = (0,imagen[i][j][plane],0)
	elif pln == 'b' or pln == 'B':
		plane = 2
		for i in range(n):
			for j in range(m):
				dataPlane[i][j] = (0,0,imagen[i][j][plane])
	else:
		return []

	return dataPlane


def getPlaneR(imagen,matOption = None):
	#esta función extrae la componente R de una imagen RGB.
	#Sino se especifica otra opción, se retorna una matriz de formato RGB.
	#Si el parámetro matOption es igual a 'matrix' se retorna una matriz de MxN con los valores numéricos de la componente R
	if matOption == 'matrix':
		m,n = size(imagen)  
		matrix = zeros(m,n)

		for i in range(m):
			for j in range(n):
				matrix[i][j] = imagen[i][j][0]

		return matrix

	elif matOption == None:
		return getPlane(imagen,'R')

	else:
		print 'Opción no válida'
		return []


def getPlaneG(imagen,matOption = None):
	#esta función extrae la componente G de una imagen RGB.
	#Sino se especifica otra opción, se retorna una matriz de formato RGB.
	#Si el parámetro matOption es igual a 'matrix' se retorna una matriz de MxN con los valores numéricos de la componente G
	
	if matOption == 'matrix':
		m,n = size(imagen)  
		matrix = zeros(m,n)

		for i in range(m):
			for j in range(n):
				matrix[i][j] = imagen[i][j][1]

		return matrix

	elif matOption == None:
		return getPlane(imagen,'G')

	else:
		print 'Opción no válida'
		return []


def getPlaneB(imagen,matOption = None):
	#esta función extrae la componente B de una imagen RGB.
	#Sino se especifica otra opción, se retorna una matriz de formato RGB.
	#Si el parámetro matOption es igual a 'matrix' se retorna una matriz de MxN con los valores numéricos de la componente B
	if matOption == 'matrix':
		m,n = size(imagen)  
		matrix = zeros(m,n)

		for i in range(m):
			for j in range(n):
				matrix[i][j] = imagen[i][j][2]

		return matrix

	elif matOption == None:
		return getPlane(imagen,'B')

	else:
		print 'Opción no válida'
		return []


def setPlane(imagen,matPlane,plane='R'):
	#Esta función crea una nueva imagen de tipo RGB donde la componente que se indique, contendrá
	#los nuevos valores indicados en la matriz 'matPlane'

	m,n = size(imagen)
	matRGB = [[(0,0,0) for h in range(m)] for x in range(n)]

	if plane == 'r' or plane == 'R':
		#Se opera con la componente rojo
		for i in range(m):
			for j in range(n):
				matRGB[i][j] = (int(round(matPlane[i][j])),imagen[i][j][1],imagen[i][j][2])

	elif plane == 'g' or plane == 'G':
		#Se opera con la componente verde 
		for i in range(m):
			for j in range(n):
				matRGB[i][j] = (imagen[i][j][0],int(round(matPlane[i][j])),imagen[i][j][2])

	elif plane == 'b' or plane == 'B':
		#Se opera con la componente azul	
		for i in range(m):
			for j in range(n):
				matRGB[i][j] = (imagen[i][j][0],imagen[i][j][1],int(round(matPlane[i][j])))

	else:
		print 'Opción no válida'
		return []

	return matRGB


def setPlaneR(imagen,matPlane):
	#Esta función pone los valores en la matriz matPlane en el plano rojo (R) de la imagen RGB indicada
	#print maxMatrix(matPlane)  #para ver cual es el mayr valor que se puede presentar en la matriz matPlane
	return setPlane(imagen,matPlane,'R')


def setPlaneG(imagen,matPlane):
	#Esta función pone los valores en la matriz matPlane en el plano verde (G) de la imagen RGB indicada
	#print maxMatrix(matPlane)  #para ver cual es el mayr valor que se puede presentar en la matriz matPlane
	return setPlane(imagen,matPlane,'G')


def setPlaneB(imagen, matPlane):
	#Esta función pone los valores en la matriz matPlane en el plano azul (B) de la imagen RGB indicada
	#print maxMatrix(matPlane)  #para ver cual es el mayr valor que se puede presentar en la matriz matPlane
	return setPlane(imagen,matPlane,'B')


def List1D(data):
	#EJEMPLO: 
	#lista = [[(1,2,3),(3,2,1)],[(8,7,6),(7,5,3)],[(3,8,9),(9,4,5)]]
	#print List1D(lista)
	m,n = size(data)

	if type(data[0][0]) == tuple:
		lista = [(0,0,0) for k in range(m*n)]
	elif type(data[0][0]) == float or type(data[0][0]) == int:  #else, is gray-scale
		lista = [0.0 for k in range(m*n)]

	h = 0
	for k in range(m):
		for j in range(n):
			lista[h] = data[k][j]
			h += 1

	return lista


def padMatrix(matrix, padlen, opt = '0'):
	#Esta función retorna una matriz enmarcada con ceros es sus bordes por defecto, si se le
	#indica la opción opt = 'r' se replican los bordes
	m,n = size(matrix)
	mat = [[0 for i in range(n+2*padlen)] for x in range(m+2*padlen)]		#inicializa el espacio en memoria

	for i in range(padlen,m+padlen):
		for j in range(padlen,n+padlen):
			mat[i][j] = matrix[i-padlen][j-padlen]

	return mat



def imconv(imagen, kernel,pad = None):

	mi, ni = size(imagen)
	mk, nk = size(kernel)
	padlen = mk/2


	if mk%2 == 0 or mk != nk:
		return [] #debe levantar una excepción porque el kernel debe ser cuadro e impar

	imaConv = padMatrix(imagen,padlen)
	imRes   = zeros(mi,ni)

	#Se aplica la convolución espacial

	for i in range(mi):
		for j in range(ni):
			acu = 0
			for x in range(i,mk+i):
				for k in range(j,nk+j):
					acu += imaConv[x][k]*kernel[x-i][k-j]
			imRes[i][j] = acu

	return imRes



def umbralizar(imagen,umbral = 100):
	m,n = size(imagen)

	for i in range(m):
		for j in range(n):
			if imagen[i][j] >= umbral:
				imagen[i][j] = 254.0
			else:
				imagen[i][j] = 0.0

	return imagen


#imagen = imread('sobel.png')
#imagen = rgb2gray(imagen)
#imf    = matInt2Float(imagen) #imagen en formato flotante
#imagen = matInt2Float(imagen)

#Procesamiento con máscara
#kernel = [[1/9.0,1/9.0,1/9.0],[1/9.0,1/9.0,1/9.0],[1/9.0,1/9.0,1/9.0]]
#kernel = [[-1,0,1],[-2,0,2],[-1,0,1]]  #bordes verticales
#kernel = [[-1,-2,-1],[0,0,0],[1,2,1]]  #bordes horizontales

#imf = imconv(imf,kernel)
#imf = mapMatrix(imf)
#imf = umbralizar(imf,115)  #para vertical
#imf = umbralizar(imf,100)  #para horizontal

#imshow(imf)
#imshow(imagen)


#							EJEMPLO PARA UN FILTRO DE MEDIANA

#imOr = imread('matlab.png')
#imshow(imOr)

#rojo = getPlaneR(imOr,'matrix') #se extrae la componente de rojo en forma matricial
#verde = getPlaneG(imOr,'matrix')
#azul = getPlaneB(imOr,'matrix')

#kernel = matScalarOperation(ones(3,3),1/9.0,'*')  #Obtenemos el filtro de mediana

#newRed = imconv(rojo,kernel)  #filtramos la componente de rojo
#newGreen = imconv(verde,kernel)
#newBlue = imconv(azul,kernel)

#newRed = mapMatrix(newRed) #Se mapea debido a que la convolución puede entregar valores del orden de miles

#imOr = setPlaneR(imOr,newRed) #se ponen el componente rojo modificado en la imagen original de nuevo
#imOr = setPlaneG(imOr,newGreen)
#imOr = setPlaneB(imOr,newBlue)

#imshow(imOr) #se muestra la imagen filtrada



#							EJEMPLO PARA UN FILTRO DE REALCE DE BORDES

#imOr = imread('matlab.png')
#imshow(imOr)

#rojo = getPlaneR(imOr,'matrix') #se extrae la componente de rojo en forma matricial
#verde = getPlaneG(imOr,'matrix')
#azul = getPlaneB(imOr,'matrix')

#kernel = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]

#newRed = imconv(rojo,kernel)  #filtramos la componente de rojo
#newGreen = imconv(verde,kernel)
#newBlue = imconv(azul,kernel)

#newRed = mapMatrix(newRed) #Se mapea debido a que la convolución puede entregar valores del orden de miles

#imOr = setPlaneR(imOr,newRed) #se ponen el componente rojo modificado en la imagen original de nuevo
#imOr = setPlaneG(imOr,newGreen)
#imOr = setPlaneB(imOr,newBlue)

#imshow(imOr) #se muestra la imagen con el rojo filtrado

