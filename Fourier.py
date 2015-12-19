# -*-coding: utf-8 -*-

#SOURCES:   file:///C:/Users/Julio/Downloads/Recursos%20Fundamentos%20de%20Control/Downloads/Dialnet-DelAnalisisDeFourierALasWaveletsAnalisisDeFourier-4807129.pdf
#		    http://dialnet.unirioja.es/servlet/articulo?codigo=4807129
#		    http://www.sciencedirect.com/science/article/pii/S0024379504003398
#			http://www.vtvt.ece.vt.edu/research/references/video/DCT_Video_Compression/Feig92a.pdf
#			http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=1165060&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D1165060
 
from cmath import exp, pi
from Errores import *
from DSP_Utils import *

#medimos el tiempo
from time import time

def fft(x,pad=0):

	N = len(x)
	Ome = exp(-(2*pi*1j)/N)

	if N%2 == 0:
		#división recursiva
		k = list(range(0,N/2))
		w = [0.0 for i in range(len(k))]

		for i in range(len(w)):
			w[i] = Ome**k[i]

		temp = list(range(0,N-1,2))
		cont = 0
		for i in range(0,N-1,2):
			temp[cont] = x[i]
			cont += 1

		u = fft(temp)

		# fft(x[2:2:N])
		temp = list(range(1,N,2))
		cont = 0
		for i in range(1,N,2):
			temp[cont] = x[i]
			cont += 1
		temp = fft(temp)

		v = list(range(len(temp)))
		for i in range(len(w)):
			v[i] = w[i]*temp[i]
		
		#k = u+v  h = u-v
		k = list(range(len(u)))
		h = list(range(len(v)))
		y = list(range(len(u)+len(v)))

		for i in range(len(u)):
			k[i] = u[i] + v[i]
			h[i] = u[i] - v[i]

		cont = 0
		for i in range(len(k)):
			y[i] = k[i]
			cont += 1

		for i in range(len(h)):
			y[cont] = h[i]
			cont += 1
	else:
		#Hacer la matriz de Fourier
		j = list([range(N)])
		k = [[i] for i in range(N)]
		res = MatrixOperations(j,k,'*')

		#F = list([range(len(res))])
		F = Ome**res

		try:
			y = list(range(len(x)))
		except TypeError:
			return F*x
		else:
			for i in range(len(x)):
				y[i] = F*x[i]
	return y



if __name__ == '__main__':
	print 'inicia'
	vec = [3,2,4,1,8,9,6]
	inicial = time()
	y = fft(vec)
	trans = time()-inicial
	print 'Tiempo ',trans
	for i in range(len(y)):
		y[i] = abs(y[i])
	print y