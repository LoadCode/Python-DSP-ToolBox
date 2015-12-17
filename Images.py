# -*- coding: utf-8 -*-

from DSP_Utils import size, ones, zeros
from PIL import Image

# SOURCE: http://www.sitepoint.com/manipulating-images-with-the-python-imaging-library/
#		  http://stackoverflow.com/questions/1109422/getting-list-of-pixel-values-from-pil
#		  http://effbot.org/imagingbook/image.htm
#		  http://sourcedexter.com/2013/08/27/extracting-pixel-values-of-an-image-in-python/


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
	matriz = arrayInt2Float(matriz)

	return matriz


def imshow(data,formato="RGB"):
	m,n = size(data)
	dataL = List1D(data)
	if type(dataL[0]) == float: #para imágenes en escala de grices
		formato = "L"
	imagen = Image.new(formato,(n,m))
	imagen.putdata(dataL)
	imagen.show()

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


def List1D(data):
	#EJEMPLO: 
	#lista = [[(1,2,3),(3,2,1)],[(8,7,6),(7,5,3)],[(3,8,9),(9,4,5)]]
	#print List1D(lista)
	m,n = size(data)

	if type(data[0][0]) == tuple:
		lista = [(0,0,0) for k in range(m*n)]
	elif type(data[0][0]) == float:  #else, is gray-scale
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

	#conved = 

	if mk%2 == 0 or mk != nk:
		return [] #debe levantar una excepción porque el kernel debe ser cuadro e impar

	imaConv = padMatrix(imagen,padlen)
	imRes   = zeros(mi,ni)

	for i in range(mi):
		for j in range(ni):
			acu = 0
			for x in range(i,mk+i):
				for k in range(j,nk+j):
					acu += imaConv[x][k]*kernel[x-i][k-j]
			imRes[i][j] = acu

	return imRes
	#Se aplica la convolución


def printMatrix(mat):
	#Imprime en pantalla la matriz que se le ingresa
	m,n = size(mat)
	for i in range(m):
		print mat[i]


def umbralizar(imagen,umbral = 100):
	m,n = size(imagen)

	for i in range(m):
		for j in range(n):
			if imagen[i][j] >= umbral:
				imagen[i][j] = 254.0
			else:
				imagen[i][j] = 0.0

	return imagen


def matInt2Float(matrix):
	#Recibe un array de dos dimensiones que contiene valores de tipo entero (no tuplas)
	m,n = size(matrix)
	mat = zeros(m,n)
	for i in range(m):
		for j in range(n):
			mat[i][j] = float(matrix[i][j])

	return mat


def maxMatrix(mat):
	#Retorna el valor máximo en una matriz
	N = len(mat) #obtiene el número de filas
	maxVec = [0.0 for j in range(N)]

	for i in range(N):
		maxVec[i] = max(mat[i])

	return max(maxVec)


def minMatrix(mat):
	#Retorna el valor mínimo presente en una matriz
	N = len(mat) #obtiene el número de filas
	maxVec = [0.0 for j in range(N)]

	for i in range(N):
		maxVec[i] = min(mat[i])

	return min(maxVec)


def matScalarOperation(mat,scl,op = '+'):

	m,n = size(mat)

	if op == '+':

		for i in range(m):
			for j in range(n):
				mat[i][j] += scl 

	elif op == '-':

		for i in range(m):
			for j in range(n):
				mat[i][j] -= scl

	elif op == '*':

		for i in range(m):
			for j in range(n):
				mat[i][j] *= scl

	elif op == '/':

		for i in range(m):
			for j in range(n):
				mat[i][j] /= scl

	else:
		print 'error operacion no valida'
		return []

	return mat

def MatrixOperations(mat1,mat2,op = '+'):

	m1,n1 = size(mat1)
	m2,n2 = size(mat2)
	res = zeros(m1,n1)

	if op == '+':
		for i in range(m1):
			for j in range(n1):
				res[i][j] = mat1[i][j] + mat2[i][j]

	return res


def mapMatrix(mat,mini = 0.0,maxi = 255.0):

	m,n = size(mat)
	newMat = zeros(m,n)

	#Mínimo y máximo valor presente en la matriz
	mi = minMatrix(mat)
	ma = maxMatrix(mat)
	rango = ma-mi
	newMat = matScalarOperation( matScalarOperation(mat,mi,'-'),rango,'/')

	#Ahora se realiza el escalado entre los valores [mini, maxi]
	newRango = maxi-mini
	newMat = matScalarOperation( matScalarOperation(newMat,newRango,'*'),mini,'+')

	return newMat





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

