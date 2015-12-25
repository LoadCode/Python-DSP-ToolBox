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

def vecTranspose(x):
    #Esta función retorna el vector transpuesto de un vector original que se recibe como parámetro
    
    if typeArray(x) == 'Row Vector':
        x = Fil2Col(x) #aplicamos la transpuesta
    elif typeArray(x) == 'Column Vector':
	x = Col2Fil(x) #aplicamos la transpuesta
    else:
	raise ValueError  #Por si un petardo le metió otro tipo de dato a la función o es un valor escalar lo que ingresa

    return x



def fft(x,pad=0):
        
	if typeArray(x) == 'Single Value':
		omega = exp(-(2*pi*1j))  #exp(-(2*pi*1j)/N) con N = 1
		F = omega**0
		return F*x
	
	m,n = size(x)
	if (m == 1 and n == None):
		print 'entro'
		omega = exp(-(2*pi*1j))  #exp(-(2*pi*1j)/N) con N = 1
		F = omega**0
		return F*x[0]
	elif m == 1 and n == 1:
	    omega = exp(-(2*pi*1j))  #exp(-(2*pi*1j)/N) con N = 1
	    F = omega**0
	    return F*x[0][0]   

	x = vecTranspose(x)
	M,N = size(x)
	if M != 1: # en caso que sea un vector columna
		N = M
	print 'N',N    
	omega = exp(-(2*pi*1j)/N)

	if N%2 == 0:
		#división recursiva
		k = list2VecCol(list(range(0,N/2)))
		Nk,aux = size(k) #aux será siempre un auxiliar que no almacenará valores relevantes
		w = zeros(Nk,1)  #vector columa de ceros
		#print 'w'
		#printMatrix(w)
		#print 'k'
		#printMatrix(k)
		for i in range(Nk):
			w[i][0] = omega**k[i][0]

		if typeArray(x) == 'Row Vector':
			temp = list2VecFil(list(range(0,N,2))) #VecFil = 1:2:N-1..saca los impares
			cont = 0
			for i in range(0,N,2):  #temp = x(1:2:N-1) se le sacan los impares a x
				temp[0][cont] = x[0][i]
				cont += 1

			u = fft(temp)  # u = fft(x(1:2:N-1)) debe ser vector fila

			# fft(x[2:2:N])
			temp = list2VecFil(list(range(1,N+1,2)))   #Se le sacan los de posiciones pares a X
			cont = 0
			for i in range(1,N+1,2):
				temp[0][cont] = x[0][i]  #temp = x(2:2:N) según .pdf
				cont += 1

			temp = fft(temp)  #temp = fft(x(2:2:N)) debe ser columna según matlab

			m,n = size(w)
			v = list2VecCol(list(range(m)))  #debe ser columna porque w es columna
			for i in range(m):
				v[i][0] = w[i][0]*temp[i][0]  # v = w.*fft(x(2:2:N))
			
			#k = u+v  h = u-v
			m,n = size(u)  #U es vector fila
			k = zeros(m,n)
			h = zeros(m,n)
			y = list2VecFil(list(range(2*n)))

			for i in range(n):
				k[0][i] = u[0][i] + v[0][i]
				h[0][i] = u[0][i] - v[0][i]

			cont = 0
			for i in range(m):
				y[0][i] = k[0][i]
				cont += 1

			for i in range(m):
				y[0][cont] = h[0][i]
				cont += 1

		elif typeArray(x) == 'Column Vector':
			temp = list2VecCol(list(range(0,N,2))) #VecCol = 1:2:N-1
			cont = 0
			for i in range(0,N-1,2):  #temp = x(1:2:N-1)
				temp[cont][0] = x[i][0]
				cont += 1

			u = fft(temp)  # u = fft(x(1:2:N-1)) debe ser vector columna

			# fft(x[2:2:N])
			temp = list2VecCol(list(range(1,N+1,2)))
			cont = 0
			for i in range(1,N,2):
				temp[cont][0] = x[i][0]  #temp = x(2:2:N) según .pdf
				cont += 1

			temp = fft(temp)  #temp = fft(x(2:2:N)) debe ser columna según matlab

			m,n = size(w)
			v = list2VecCol(list(range(m)))  #debe ser columna porque w es columna
			for i in range(m):
				v[i][0] = w[i][0]*temp[i][0]  # v = w.*fft(x(2:2:N))
			
			#k = u+v  h = u-v
			m,n = size(u)  #U es vector columna
			k = zeros(m,n)
			h = zeros(m,n)
			y = list2VecCol(list(range(2*m)))

			for i in range(n):
				k[i][0] = u[i][0] + v[i][0]
				h[i][0] = u[i][0] - v[i][0]

			cont = 0
			for i in range(m):
				y[cont][0] = k[i][0]
				cont += 1

			for i in range(m):
				y[cont][0] = h[i][0]
				cont += 1			
	else:
		#Hacer la matriz de Fourier
		print 'entro matriz'
		j = list([range(N)])         #Vector fila 0:N-1
		k = Fil2Col(j)	             #Vector columna

		res = MatrixOperations(k,j,'*')  #Debe ser una matiz NxN = k*j -> Nx1 * 1xN

		F = zeros(N,N)
		for i in range(N):
			for j in range(N):
				F[i][j] = omega**res[i][j]   #F = omegaga.^(k*j) según el .pdf

		yv = MatrixOperations(F,x,'*')
		y = yv  #esa mierda result+o ser matriz
		if typeArray(yv) == 'Row Vector':
			y = Fil2Col(yv)
		elif typeArray(yv) == 'Column Vector':
			y = Col2Fil(yv)

	return y



if __name__ == '__main__':
	print 'inicia'
	vec = [[1],[2],[1],[0],[7],[8]]
	inicial = time()
	y = fft(vec)
	trans = time()-inicial
	print 'Tiempo ',trans
	#for i in range(len(y)):
	#	y[i] = abs(y[i])
	print y
