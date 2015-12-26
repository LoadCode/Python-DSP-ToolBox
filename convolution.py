# -*- coding: utf-8 -*-

            #ALGORITMO PARA CALCULAR LA CONVOLUCIÓN

#@Author: Julio César Echeverri Marulanda
#@Email : julio.em7@gmail.com

#Vectores a convolucionar como ejemplo

#a = [1,2,3]     #Vector A para la convolución (puede ser >= B)
#b = [3,2,4,6,1] #Vector B para la convolución (puede ser >= A)
#print conv(a,b)

from Errores import OptionInvalidError

def conv(a,b,opt = 'os'):
    #Esta función realiza el cálculos de la convolución entre dos secuencias de datos que son valores numéricos en formato lista

    if opt == 'os':
        y = conv_output_side(a,b)

    elif opt == 'is':
        y = conv_input_side(a,b)
    elif opt == 'th': #theoretical computation
        Na = len(a)
        Nb = len(b)

        y = [0 for x in range(0,Na+Nb-1)]
        Ny = len(y)


        #Sumatoria de convolución
        for n in range(0,Ny):
            k = n; f = 1;
            while k >= 0:
                if n >= Na:   #Este if es para cuando el vector que va recorriendo se sale del indice de a[k]
                    k = Na-f; f += 1;
                    
                y[n] += a[k]*b[n-k] #Ecuación de la convolución
                k -= 1
                if (n-k) >= Nb:
                    break
    else:
        print 'Opción no soportada, debe elegir entre os, is, th'
        raise OptionInvalidError

    return y


def conv_input_side(x, h):
    #SOURCE: http://www.dspguide.com/ch6/3.htm
    #input-side algorithm for convolution computation

    y = [0.0 for i in range(len(x)+len(h)-1)]

    for i in range(len(x)):
        for j in range(len(h)):
            y[i+j] += x[i]*h[j]

    return y


def conv_output_side(x,h):
    #SOURCE: http://www.dspguide.com/ch6/4.htm
    #output-side algorithm for convolution computation

    y = [0.0 for i in range(len(x)+len(h)-1)]

    for i in range(len(y)):
        for j in range(len(h)):
            if (i-j < 0) or (i-j > len(x)-1):
                continue
            y[i] += h[j]*x[i-j]

    return y

