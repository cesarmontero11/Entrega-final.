#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:47:15 2019

@author: cesarmontero
"""

'''
importar modulos
from math import sin, pi
print(sin(pi/2))
'''


'''
#USO DE MEMORIA NUMPY VS PYTHON 

import numpy as np
import sys
print ('USO DE MEMORIA PYTHON')
S= range (1000)
print (sys.getsizeof(5) * len (S))
print ('/n'*1)
print ('USO DE MEMORIA NUMPY')
D=np.arange(1000)
print (D.size*D.itemsize)
'''

'''
#TEST DE VELICIDAD

import numpy as np
import time
 
SIZE = 1000000
 
L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2=np.arange(SIZE)
print ("\n"*1)
print ("RESULTADO USANDO LISTAS/TUPLAS EN PYTHON")
start= time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
print ("\n"*2)
print ("RESULTADO USANDO NUMPY")
start=time.time()
result= A1+A2
print((time.time()-start)*1000)
'''

