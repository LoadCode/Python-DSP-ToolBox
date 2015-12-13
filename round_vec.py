# -*- coding: utf-8 -*-
#Esta rutina aplica la función round() a cada elemento de un vector

def round_vec(vec):
	N = len(vec)
	for n in range(0,N):
		vec[n] = round(vec[n])
	return vec