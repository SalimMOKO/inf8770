import matplotlib.pyplot as py
import numpy as np

import matplotlib.pyplot as py
import numpy as np
import scipy.fftpack as dctpack

image = py.imread('C:/Users/USER/Desktop/INF8770_TP2/inf8770/tp2/fjords.jpg').astype('float')
hauteur = len(image)
largeur = len(image[0])
dctArray = []
Quant1= np.matrix('16 11 10 16 24 40 51 61;\
        12 12 14 19 26 58 60 55;\
        14 13 16 24 40 57 69 56;\
        14 17 22 29 51 87 80 62;\
        18 22 37 56 68 109 103 77;\
        24 35 55 64 81 104 103 92;\
        49 64 78 77 103 121 120 101;\
        72 92 95 98 112 100 103 99').astype('float')

def dct(blocs):
    img = np.zeros_like(blocs)
    blocs[:] -= 128
    for bloc in blocs:
        BlocDCT = dctpack.dct(dctpack.dct(bloc[:, :, 0], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocDCT2 = dctpack.dct(dctpack.dct(bloc[:, :, 1], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocDCT3 = dctpack.dct(dctpack.dct(bloc[:, :, 2], axis=0, norm='ortho'), axis=1, norm='ortho')
        bloc[:, :, 0] = BlocDCT
        bloc[:, :, 1] = BlocDCT2
        bloc[:, :, 2] = BlocDCT3
    return blocs

def reversedct(blocs):
    img = np.zeros_like(blocs)
    for bloc in blocs:
        BlocIDCT = dctpack.idct(dctpack.idct(bloc[:, :, 0], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocIDCT2 = dctpack.idct(dctpack.idct(bloc[:, :, 1], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocIDCT3 = dctpack.idct(dctpack.idct(bloc[:, :, 2], axis=0, norm='ortho'), axis=1, norm='ortho')
        bloc[:, :, 0] = BlocIDCT
        bloc[:, :, 1] = BlocIDCT2
        bloc[:, :, 2] = BlocIDCT3
    blocs[:] += 128
    return blocs

def quantification(blocs):
    for bloc in blocs:
        bloc[:, :, 0] = np.round(np.divide(bloc[:, :, 0], Quant1))
        bloc[:, :, 1] = np.round(np.divide(bloc[:, :, 1], Quant1))
        bloc[:, :, 2] = np.round(np.divide(bloc[:, :, 2], Quant1))
    return blocs


def reverseQuantification(blocs):
    for bloc in blocs:
        bloc[:, :, 0] = np.round(np.multiply(bloc[:, :, 0], Quant1))
        bloc[:, :, 1] = np.round(np.multiply(bloc[:, :, 1], Quant1))
        bloc[:, :, 2] = np.round(np.multiply(bloc[:, :, 2], Quant1))
    return blocs