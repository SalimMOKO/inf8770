# -*- coding: utf-8 -*-
# Source : https://github.com/gabilodeau/INF8770

import numpy as np
import scipy.fftpack as dctpack

dctArray = []
Quant1 = np.matrix('16 11 10 16 24 40 51 61;\
        12 12 14 19 26 58 60 55;\
        14 13 16 24 40 57 69 56;\
        14 17 22 29 51 87 80 62;\
        18 22 37 56 68 109 103 77;\
        24 35 55 64 81 104 103 92;\
        49 64 78 77 103 121 120 101;\
        72 92 95 98 112 100 103 99').astype('float')

Quant2 = np.matrix('53 37 33 53 80 133 170 203;\
    40 40 47 63 87 193 200 183;\
    47 43 53 80 133 190 230 187;\
    47 57 73 97 170 290 267 207;\
    60 73 123 187 227 363 343 257;\
    80 117 183 213 270 347 377 307;\
    163 213 260 290 343 403 400 337;\
    240 307 317 327 373 333 343 300').astype('float')

Quant3 = np.matrix('1 1 1 1 1 1 1 1;\
    1 1 1 1 1 1 1 1;\
    1 1 1 1 1 1 1 1;\
    1 1 1 1 1 1 1 1;\
    1 1 1 1 1 1 1 1;\
    1 1 1 1 1 1 1 1;\
    1 1 1 1 1 1 1 1;\
    1 1 1 1 1 1 1 1').astype('float')


def discreteCosineTransform(blocs):
    blocs[:] -= 128
    for bloc in blocs:
        BlocDCTY = dctpack.dct(dctpack.dct(bloc[:, :, 0], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocDCTCb = dctpack.dct(dctpack.dct(bloc[:, :, 1], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocDCTCr = dctpack.dct(dctpack.dct(bloc[:, :, 2], axis=0, norm='ortho'), axis=1, norm='ortho')
        bloc[:, :, 0] = BlocDCTY
        bloc[:, :, 1] = BlocDCTCb
        bloc[:, :, 2] = BlocDCTCr
    return blocs


def reverseDCT(blocs):
    for bloc in blocs:
        BlocIDCTY = dctpack.idct(dctpack.idct(bloc[:, :, 0], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocIDCTCb = dctpack.idct(dctpack.idct(bloc[:, :, 1], axis=0, norm='ortho'), axis=1, norm='ortho')
        BlocIDCTCr = dctpack.idct(dctpack.idct(bloc[:, :, 2], axis=0, norm='ortho'), axis=1, norm='ortho')
        bloc[:, :, 0] = BlocIDCTY
        bloc[:, :, 1] = BlocIDCTCb
        bloc[:, :, 2] = BlocIDCTCr
    blocs[:] += 128
    return blocs


def quantification(blocs):
    for bloc in blocs:
        bloc[:, :, 0] = np.round(np.divide(bloc[:, :, 0], Quant3))
        bloc[:, :, 1] = np.round(np.divide(bloc[:, :, 1], Quant3))
        bloc[:, :, 2] = np.round(np.divide(bloc[:, :, 2], Quant3))
    return blocs


def reverseQuantification(blocs):
    for bloc in blocs:
        bloc[:, :, 0] = np.round(np.multiply(bloc[:, :, 0], Quant3))
        bloc[:, :, 1] = np.round(np.multiply(bloc[:, :, 1], Quant3))
        bloc[:, :, 2] = np.round(np.multiply(bloc[:, :, 2], Quant3))
    return blocs
