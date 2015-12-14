# -*- coding: utf-8 -*-

#Rutina para la generación de vectores con elementos linealmente espaciados (ver documentación)

def linspace(xmin,xmax,n = 100):
	
	xmin *= 1.0  #En caso que los valores se pasen como números enteros
	xmax *= 1.0

	stp = (xmax-xmin)/(n-1)
	vec = [0 for x in range(0,n)] #Inicialización del vector que almacenará los valores
	vec[0] = xmin

	for x in range(1,n):
		vec[x] = vec[x-1] + stp

	vec[n-1] = xmax

	return vec
