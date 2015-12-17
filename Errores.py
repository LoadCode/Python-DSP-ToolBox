# -*- coding: utf-8 -*-
#Este módulo contiene las definiciones de todas las posibles excepciones específicas que puede lanzar el toolbox

class DimensionError(Exception):
	def __init__(self):
		pass

	def __str__(self):
		print '   Dimension inconsistente del Array'

