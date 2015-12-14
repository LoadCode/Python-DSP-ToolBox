# -*- coding: utf-8 -*-

def ones(m,n=1):

	if m != 0 or n != 0:
		if m == 1 and n != 1:
			mat = [1.0 for x in range(0,n)]
		elif n == 1 and m != 1:
			mat = [1.0 for x in range(0,m)]
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
			mat = [0.0 for x in range(0,n)]
		elif n == 1 and m != 1:
			mat = [0.0 for x in range(0,m)]
		elif m != 1 and n != 1:
			mat = [[0.0 for x in range(0,n)] for x in range(0,m)]
		else:
			mat = 0.0
	else:
		mat = []

	return mat



def matInit(m,n,val=1.0):

	if m != 0 or n != 0:
		if m == 1 and n != 1:
			mat = [val for x in range(0,n)]
		elif n == 1 and m != 1:
			mat = [val for x in range(0,m)]
		elif m != 1 and n != 1:
			mat = [[val for x in range(0,n)] for x in range(0,m)]
		else:
			mat = val
	else:
		mat = []

	return mat


def linspace(xmin,xmax,n = 100):
	
	#Rutina para la generación de vectores con elementos linealmente espaciados (ver documentación)
	
	xmin *= 1.0  #En caso que los valores se pasen como números enteros
	xmax *= 1.0

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
	n = len(mat[1][:])
	return [m,n]


def round_vec(vec):
	#Esta rutina aplica la función round() a cada elemento de un vector
	N = len(vec)
	for n in range(0,N):
		vec[n] = round(vec[n])
	return vec
