# -*- coding: utf-8 -*-
# https://github.com/wzq94qzw/naive-jpeg

import matplotlib.pyplot as py
import numpy as np


def zig_zag(input_matrix,block_size):
    z = np.empty([block_size*block_size*3])
    index = -1
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
                z[index] = input_matrix[j, i - j][1]
                index += 1
                z[index] = input_matrix[j, i - j][2]
            else:
                z[index] = input_matrix[i-j, j][0]
                index += 1
                z[index] = input_matrix[i - j, j][1]
                index += 1
                z[index] = input_matrix[i - j, j][2]
    return z


def zig_zag_reverse(input_matrix,block_size):
    image = py.imread('fjords.jpg').astype('float')
    output_matrix = np.empty([image.shape[0],image.shape[1],3])
    index = -1
    for i in range(0, 2 * block_size -1):
        if i < block_size:
            bound = 0
        else:
            bound = i - block_size + 1
        for j in range(bound, i - bound + 1):
            index += 3
            if i % 2 == 1:
                output_matrix[j, i - j][0] = input_matrix[index]
                output_matrix[j, i - j][1] = input_matrix[index]
                output_matrix[j, i - j][2] = input_matrix[index]
            else:
                output_matrix[i - j, j][0] = input_matrix[index]
                output_matrix[i - j, j][1] = input_matrix[index]
                output_matrix[i - j, j][2] = input_matrix[index]
    return output_matrix
