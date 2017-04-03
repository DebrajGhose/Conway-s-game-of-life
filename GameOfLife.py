# -*- coding: utf-8 -*-
"""
Python 2.7

Created on Sun Apr 02 21:14:23 2017

@author: Debraj Ghose
"""


from pylab import *


size = 40 #define size of the domain
grid = np.random.rand(size,size) #define intial condition from which game of life happens

steps = 1000

threshhold = 0.7 #threshhold to grid to 1 or 0 matrix
low_indices = grid<threshhold #get indexes for values lower than the threshhold
grid[low_indices] = 0 #change values to 0
high_indices = grid>=threshhold
grid[high_indices] = 1



gridnew = np.zeros((size,size))



for time in range(0,steps):
    
    for i in range(0,size):
        
        for j in range(0,size):
            
            #define pixels
            
            up = mod(i-1,size); down = mod(i+1,size);
            left = mod(j-1,size); right = mod(j+1,size);
            
            #find numrbe of surrounding live cells
            surround_sum = grid[i,left] + grid[up,left] + grid[up,j] + grid[up,right] + grid[i,right] + grid[down,right] + grid[down,j] + grid[down,left]
    
            if grid[i,j] == 1:
                
                if surround_sum < 2 or surround_sum > 3:#death by under or overpopulation
                    gridnew[i,j] = 0 
                else:
                    gridnew[i,j] = 1 #cell survives
                    
            if grid[i,j] == 0:
                
                if surround_sum == 3: #cell created via reproduction
                    gridnew[i,j] = 1
                else:
                    gridnew[i,j] = 0

    grid = np.copy(gridnew)
    imshow(grid)
    plt.show







