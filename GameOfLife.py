# -*- coding: utf-8 -*-
"""
Python 2.7

Created on Sun Apr 02 21:14:23 2017

@author: Debraj Ghose
"""


from pylab import *


size = 40 #define size of the domain
grid = np.random.rand(size,size) #define intial condition from which game of life happens



for i in range(0,size):
    
    for j in range(0,size):
        
        #define pixels
        
        up = mod(i-1,size); down = mod(i+1,size);
        left = mod(j-1,size); right = mod(j+1,size);







