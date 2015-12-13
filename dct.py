# -*-coding: utf-8 -*-
#Definición de la rutina para obtener la transformada de coseno discreta..

#	Name:   	dct
#	Author:		Julio C. Echeverri M.
#	Date:		02/12/2015

from math import sqrt, cos, pi
import idct as ic
import round_vec as rv

def dct(x,g=0):

	N = len(x)
	y = [0.0 for h in range(0,N)]

	#definición de constantes
	wk = sqrt(2.0/N)
	wn = pi/(2.0*N)
	acu = 0.0

	#Realizar aquí la primera iteración para k=0 para no disminuir la eficiencia.
	k = 0
	for n in range(0,N):
 		acu += x[n]*cos(wn*(2*n+1)*(k))
 	y[k] = (1.0/sqrt(N))*acu

	#Transformada
	for k in range(1,N):
		acu = 0.0
		for n in range(0,N):
			acu += x[n]*cos(wn*(2*n+1)*(k))
		y[k] = wk*acu

	return y





#Ejemplo para comprobar su funcionamiento

#signal =  [1,4,3,2,5,6,4,2,45,6,3,32,64,3,21,6,32,67,8,93,13,54,23,65,23,56,8,64,23,214,6,4,3,231,6,53,667,434,233,234,65,345,355]

#y = dct(signal)
#x = rv.round_vec(ic.idct(y))

#Se imprimen las listas en un archivo de texto
#import json
#f = open('recons.txt', 'w')
#json.dump(x, f)
#f.close()
#f = open('senal.txt', 'w')
#json.dump(y, f)
#f.close()