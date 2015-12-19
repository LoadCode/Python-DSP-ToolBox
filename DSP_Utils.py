# -*- coding: utf-8 -*-

from Errores import *   #se importan todas las excepciones personalizadas del toolbox
from math import floor

def ones(m,n=1):

	if m != 0 or n != 0:
		if m == 1 and n != 1:
			mat = [1.0 for x in range(0,n)]
		elif n == 1 and m != 1:
			mat = [[1.0] for x in range(0,m)]
		elif m != 1 and n != 1:
			mat = [[1.0 for x in range(0,n)] for x in range(0,m)]
		else:
			mat = 1.0
	else:
		mat = []

	return mat

def zeros(m,n=1):
	if m != 0 or n != 0:
		if m == 1 and n != 1:
			mat = [[0.0 for x in range(0,n)]]
		elif n == 1 and m != 1:
			mat = [[0.0] for x in range(0,m)]
		elif m != 1 and n != 1:
			mat = [[0.0 for x in range(0,n)] for x in range(0,m)]
		else:
			mat = 0.0
	else:
		mat = []

	return mat

def matInit(m,n,val=1.0):

	val = float(val)
	if m != 0 or n != 0:
		if m == 1 and n != 1:
			mat = [val for x in range(0,n)]
		elif n == 1 and m != 1:
			mat = [[val] for x in range(0,m)]
		elif m != 1 and n != 1:
			mat = [[val for x in range(0,n)] for x in range(0,m)]
		else:
			mat = val
	else:
		mat = []

	return mat

def linspace(xmin,xmax,n = 100):
	
	#Rutina para la generación de vectores con elementos linealmente espaciados (ver documentación)
	
	xmin = float(xmin) #En caso que los valores se pasen como números enteros
	xmax = float(xmax)

	stp = (xmax-xmin)/(n-1)
	vec = [0 for x in range(0,n)] #Inicialización del vector que almacenará los valores
	vec[0] = xmin

	for x in range(1,n):
		vec[x] = vec[x-1] + stp

	vec[n-1] = xmax

	return vec



def size(mat):
	#Esta función retorna las dimensiones de un Array que es pasado como parámetro
	m = len(mat)
	try:
		n = len(mat[0])
	except TypeError:
		return [m,None]  #porque es vector fila (1 fila)
	else:
		for i in range(m):
			if len(mat[i]) != n:
				raise DimensionError
		return [m,n]



def typeArray(array):
	#Esta función retorna una cadena indicando el tipo de arreglo que es pasado
	if type(array) == float or type(array) == int:
		return 'Single Value'
	elif type(array) == str:
		return 'Not a Numeric Array'
	else:	
		m,n = size(array)
		if m == 1 and n != 1:
			return 'Row Vector'
		elif m != 1 and n == 1:
			return 'Column Vector'
		elif m > 1 and n > 1:
			return 'Matrix'
		elif m == n:
			return 'Square Matrix'
		else:
			return 'Undefined Matrix Type'


def round_vec(vec):
	#Esta rutina aplica la función round() a cada elemento de un vector
	N = len(vec)
	for n in range(0,N):
		vec[n] = round(vec[n])
	return vec


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

	elif op == '^':

		for i in range(m):
			for j in range(n):
				mat[i][j] **= scl

	else:
		print 'error operacion no valida'
		return []

	return mat

def printMatrix(mat):
	#Imprime en pantalla la matriz que se le ingresa
	m,n = size(mat)
	for i in range(m):
		print mat[i]


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



def MatrixOperations(mat1,mat2,op = '+'):

	m1,n1 = size(mat1)
	m2,n2 = size(mat2)

	if n1 == None or n2 == None:  #Seguridad para el metodo
		raise VectorDimensionError
	
	res = zeros(m1,n1)

	if op == '+':
		for i in range(m1):
			for j in range(n1):
				res[i][j] = mat1[i][j] + mat2[i][j]
	
	elif op == '-':
		for i in range(m1):
			for j in range(n1):
				res[i][j] = mat1[i][j] - mat2[i][j]

	elif op == '*':
		#EJEMPLO: 
		#b = [[3,2,4],[4,3,2],[7,6,4]]
		#d = [[3],[4],[6]]
		#res = MatrixOperations(b,d,'*')
		#printMatrix(res)
		if n1 == m2: #las matrices son de demensiones adecuadas
			#En este método python si puede operar con vectores columna como matrices no con vectores fila
			res = zeros(m1,n2)
			for i in range(m1):
				for j in range(n2):
					acu = 0.0
					for r in range(n1):
						acu += mat1[i][r]*mat2[r][j]
					if type(res) == float or type(res) == int:
						return acu

					res[i][j] = acu
	else:
		print 'Error operación no implementada'

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


def rangeStep(x_1,step,x_2):
	N = int(floor((x_2-x_1)/float(step)))+1
	print 'N =',N
	y = [0.0 for i in range(N)]
	i = 0
	if x_1 < x_2:
		cont = x_1
		while cont <= x_2:
			y[i] = cont
			cont += step
			i += 1
	elif x_2 < x_1:
		if step >= 0:
			return []
		cont = x_1
		while cont >= x_2:
			y[i] = cont
			cont += step
			i += 1
	else:
		return [x_1]

	return y[:i]



def list2VecFil(x):
	#Esta función recibe una lista de una dimensión y la convierte en
	#un vector fila válido para aplicar las funciones del módulo DSP_Utils
	return [[x[i] for i in range(len(x))]]


def list2VecCol(x):
	#Esta función recibe una lista unidimensional y retorna un
	#vector columna válido para aplicar las funciones del módulo DSP_Utils
	return [[x[i]] for i in range(len(x))]

def Col2Fil(x):
	#Esta función convierte un vector columna en un vector fila
	if typeArray(x) == 'Column Vector':
		m,n = size(x)
		return [[x[i][0] for i in range(m)]]
	else:
		return []

def Fil2Col(x):
	#Esta función convierte un vector fila en un vector columna
	if typeArray(x) == 'Row Vector':
		m,n = size(x)
		return [[x[0][i]] for i in range(n)]
	else:
		return []
