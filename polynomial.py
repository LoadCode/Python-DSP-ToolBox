# -*-coding: utf-8 -*-

# FUNCIÓN POLY() EN PYTHON PARA HALLAR LOS COEFICIENTES DEL POLINOMIO DADAS SUS RAICES
# FUNCIÓN POLYVAL() EN PYTHON PARA EVALUAR UN POLINOMIO EN UN VALOR ESPECÍFICO

# @Author: Julio César Echeverri Marulanda
# @E-mail: julio.em7@gmail.com

import convolution as conv

def poly(roots):
    #Esta función retorna un vector con los coeficientes de un polinomio que corresponde
    #a la lista de polos o raices dadas en 'Polos'

    #Ejemplo de uso de la función poly en Python
    #print poly([-0.5+3*1j, -0.5-3*1j, 4]) => s^3-3s^2+5.25s-37
    
    orden = len(roots)
    poli = [0 for x in range(0,orden)]
    poliaux = -roots[0]
    for k in range(0,orden-1):
        if k == 0:
            poli[k+1] = conv.conv([1,poliaux],[1,-roots[k+1]])
        else:
            poli[k+1] = conv.conv(poliaux,[1,-roots[k+1]])
        poliaux = poli[k+1]

    for k in range(0,len(poliaux)):
        if poliaux[k].imag == 0:
            poliaux[k] = poliaux[k].real
    
    return poliaux





def polyval(pol,x):
    #Esta función realiza la evaluación de un polinomio dado el vector que contiene sus coeficientes

#     Ejemplo
##    pol = [1,-2,-3,4,-5]
##    x = 2
##    print polyval(pol,x)

    
    N = len(pol)-1  #Orden del polinomio
    n = N
    acu = 0
    for h in range(0,len(pol)):
        aux = 1
        for k in range(0,n):
            aux *= x;
        acu += pol[h]*aux
        n -= 1
    return acu
