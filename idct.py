# -*-coding: utf-8 -*-
#Definición de la rutina para obtener la transformada de coseno discreta..

#	Name:   	dct
#	Author:		Julio C. Echeverri M.
#	Date:		02/12/2015

from math import sqrt, cos, pi

def idct(y,g=0):

	N = len(y)
	acu = 0.0
	x = [0.0 for h in range(0,N)]
	wn = pi/(2*N)
	wk1 = 1.0/sqrt(N)
	wk2 = sqrt(2.0/N)

	for n in range(0,N):
		acu = 0.0
		for k in range(0,N):
			if k == 0:
				acu += wk1*y[k]*cos(wn*(2*n+1)*(k))
			else:
				acu += wk2*y[k]*cos(wn*(2*n+1)*(k))
		x[n] = acu
	return x
