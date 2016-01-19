# -*- coding: utf-8 -*-

from Errores import *   #se importan todas las excepciones personalizadas del toolbox
from math import floor

def ones(m,n=0):
	#Esta función retorna una arreglo bidimensional que puede ser vector fila, columna o matriz de MxN
	#Si M!=0 y N==0 se retorna una lista de Python compuesta de 1s
	#Si M=0 y N=0 se retorna una matriz vacía.
	#Si M=1 y N=1 se retorna un escalar
	#Ejemplo: crear una lista:		     lista = ones(5) #lista Python de 5 elementos
	#Ejemplo: crear un vector columna:	 vecCol = ones(6,1) #Vector columna de 6 elementos 6x1
	#Ejemplo: crear un vector fila:		 vecFil = ones(1,6) #Vector fila de 6 elementos 1x6
	#Ejemplo: crear una matriz:		     matriz = ones(4,6) #Matriz 4x6

	if m != 0 and n == 0:
		mat = [1.0 for i in range(0,m)]

	elif m != 0 or n != 0:
		
		if m == 1 and n != 1:  #Vector  fila
			mat = [[1.0 for x in range(0,n)]]
		elif n == 1 and m != 1: #Vector columna
			mat = [[1.0] for x in range(0,m)]
		elif m != 1 and n != 1:
			mat = [[1.0 for x in range(0,n)] for x in range(0,m)] #Matriz MxN
		else:
			mat = 1.0 #Si m=1 y n=1 se retorna un escalar
	else:
		mat = [[]]   #Si M=0 y N=0 se retorna una matriz vacía 

	return mat




def ones(m,n=0):
	#Esta función retorna una arreglo bidimensional que puede ser vector fila, columna o matriz de MxN
	#Si M!=0 y N==0 se retorna una lista de Python compuesta de 0s
	#Si M=0 y N=0 se retorna una matriz vacía.
	#Si M=1 y N=1 se retorna un escalar
	#Ejemplo: crear una lista:		     lista = zeros(5) #lista Python de 5 elementos
	#Ejemplo: crear un vector columna:	 vecCol = zeros(6,1) #Vector columna de 6 elementos 6x1
	#Ejemplo: crear un vector fila:		 vecFil = zeros(1,6) #Vector fila de 6 elementos 1x6
	#Ejemplo: crear una matriz:		     matriz = zeros(4,6) #Matriz 4x6

	if m != 0 and n == 0:
		mat = [0.0 for i in range(0,m)]

	elif m != 0 or n != 0:
		
		if m == 1 and n != 1:  #Vector  fila
			mat = [[0.0 for x in range(0,n)]]
		elif n == 1 and m != 1: #Vector columna
			mat = [[0.0] for x in range(0,m)]
		elif m != 1 and n != 1:
			mat = [[0.0 for x in range(0,n)] for x in range(0,m)] #Matriz MxN
		else:
			mat = 0.0  #Si M=1 y N=1 se retorna un escalar
	else:
		mat = [[]]   #Si M=0 y N=0 se retorna una matriz vacía 

	return mat




def matInit(m,n=0,val=1.0):

	#Esta función retorna una matriz o vector cuyos valores está inicializados con el valor que se pasa como
	#tercer parámetro.
	#Si M=1 y N=1 se retorna un escalar
	#Ejemplo: crear una lista python con valores 3.0 ->                   lista = matInit(10,val=3.0)
	#Ejemplo: crear un vector fila de 10 elementos con valores 2.0 ->    vecFil = matInit(1,10,2.0)
	#Ejemplo: crear un vector columna de 10 elementos con valores 2.0 -> vecCol = matInit(10,1,2.0)
	#Ejemplo: crear una matriz de 4x7 con valores 78.0 ->				 matriz = matInit(4,7,78.0)	

	val = float(val)
	
	if m != 0 and n == 0:
		mat = [val for i in range(m)]

	elif m != 0 or n != 0:
		if m == 1 and n != 1:
			mat = [[val for x in range(0,n)]] #Vector fila 
		elif n == 1 and m != 1:
			mat = [[val] for x in range(0,m)] #Vector columna
		elif m != 1 and n != 1:
			mat = [[val for x in range(0,n)] for x in range(0,m)] #Matriz MxN con valores iniciales 'val'
		else:
			mat = val #Si M=1 y N=1 se retorna un escalar
	else:
		mat = [[]]   #si M=0, N=0 entonces se retorna una matriz vacía

	return mat




def linspace(xmin,xmax,n = 100,tipo='l'):
	
	#Rutina para la generación de vectores con elementos linealmente espaciados
	# xmin puede ser mayor a xmax, la serie será entregada en orden inverso
	#Su lista de parámetros es:
	#			xmin = valor inicial del array
	#			xmax = valor final del array
	#			   n = cantidad de elementos del array
	#			tipo = Tipo de array a retornar: 
	#						'l' -> valor por defecto que retorna una lista de Python
	#						'f' -> retorna un vector fila
	#						'c' -> retorna un vector columna
	#					si se pasa una opción no válida se lanza la excepción OptionInvalidError
	
	#En caso que los valores se pasen como números enteros
	xmin = float(xmin)
	xmax = float(xmax)

	stp = (xmax-xmin)/(n-1) #Valor para el 'paso' entre elementos de la serie

	vec = [0.0 for x in range(0,n)] #Inicialización del vector que almacenará los valores
	#se llena la lista con la serie ya completa
	vec[0] = xmin
	for x in range(1,n):
		vec[x] = vec[x-1] + stp
	vec[n-1] = xmax

	if tipo == 'l':
		return vec

	elif tipo == 'f':  #Se convierte la lista a un vector fila y se retorna
		return list2VecFil(vec)

	elif tipo == 'c':  #Se convierte la lista a un vector columna y se retorna
		return list2VecCol(vec)

	else:  #si se pasa un 'tipo' no reconocido se lanza una excepción
		raise OptionInvalidError




def size(mat):
	#Esta función retorna una lista con las dimensiones de una lista o tupla de dos dimensiones (no solo numéricas)
	#En caso de que todas sus columnas no posean la misma cantidad de elementos se lanzará una excepción de tipo
	# DimensionError por inconsistencia en las dimensiones.
	
	#En caso de que no se pase una lista
	if not isinstance(mat,list) and not isinstance(mat,tuple):
		raise TypeError

	m = len(mat)
	cont = 0

	#Verificamos que no hayan problemas de dimensión en cuanto al número de columnas para listas simples de Python
	for i in range(m):
		try:
			k = len(mat[i])
		except TypeError:
			cont += 1

	if cont < m and cont != 0:
		raise DimensionError

	#sino hay problema de dimensiones inconsistentes, se puede calcular las dimensiones
	try:
		n = len(mat[0])
	except TypeError:
		return [m,None]  #Se pasó como argumento una lista simple de Python ejemplo: [1,2,3,4]
	else:
		#Se verifica que todas las columnas tengan el mismo número de elementos, de lo contrario se poseen errores de dimensión
		for i in range(m):
			if len(mat[i]) != n:
				raise DimensionError
		return [m,n]




def typeArray(array):
	#Esta función retorna una cadena indicando el tipo de arreglo que es pasado
	#Retorna:
	#			'Row Vector'
	#			'Column Vector'
	#			'Matrix'
	#			'Square Matrix'
	#			'Simple Python List'   -> una lista de Python normal (no matricial)
	#			'Simple Python Tuple'  -> una lista de Python normal (no matricial)

	if (not isinstance(array,list)) and (not isinstance(array,tuple)):
		return 'Not An Array'
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
			if isinstance(array,tuple):
				return 'Simple Python Tuple'
			else:
				return 'Simple Python List'


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
