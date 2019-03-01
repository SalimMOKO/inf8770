import matplotlib.pyplot as py
import numpy as np
image = py.imread('C:/Users/USER/Desktop/INF8770_TP2/inf8770/tp2/fjords.jpg').astype('float')

def zig_zag(input_matrix,block_size):
    z = np.empty([block_size*block_size*3])
    index = -1
    bound = 0
    for i in range(0, 2 * block_size -1):
        if i < block_size:
            bound = 0
        else:
            bound = i - block_size + 1
        for j in range(bound, i - bound + 1):
            index += 1
            if i % 2 == 1:
                z[index] = input_matrix[j, i-j][0]
                index += 1
                z[index] = input_matrix[j, i - j][0]
                index += 1
                z[index] = input_matrix[j, i - j][0]
            else:
                z[index] = input_matrix[i-j, j][0]
                index += 1
                z[index] = input_matrix[i - j, j][1]
                index += 1
                z[index] = input_matrix[i - j, j][2]
    return z