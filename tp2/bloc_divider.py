# -*- coding: utf-8 -*-

import matplotlib.pyplot as py
import numpy as np


image = py.imread("fjords.jpg")

hauteur = len(image)
largeur = len(image[0])




def divider8by8(image):
    bloc8x8 = []
    for row in range(0, image.shape[0] - 8 + 1, 8):
        for column in range(0, image.shape[1] - 8 + 1, 8):
            bloc8x8.append(image[row:row + 8, column:column + 8])
    return np.array(bloc8x8)


def  rebuildFrom8by8(blocs):
    imageReconstruite = np.zeros_like(image)

    ligne = 0
    indexLBlocs = 0
    while ligne < hauteur:
        colonne = 0
        indexCBlocs = 0
        while colonne < largeur:
            imageReconstruite[ligne:ligne + 8, colonne:colonne + 8] = blocs[indexLBlocs][indexCBlocs]
            indexCBlocs += 1
            colonne += 8
        ligne += 8
        indexLBlocs += 1

    return imageReconstruite

def inverseDivision8x8(bloc, result):
    indexbloc = 0
    for i in range(0, result.shape[0] - 8 + 1, 8):
        for j in range(0, result.shape[1] - 8 + 1, 8):
            result[i:i+8,j:j+8] = bloc[indexbloc]
            indexbloc = indexbloc + 1
    return result

def divider8by8_blocs(image):
    if len(image) % 8 != 0 or len(image[0]) % 8 != 0:
        print ('Erreur image non compatible')
        return -1

    blocs = []
    index = 0
    ligne = 0
    while ligne < hauteur:

        blocs.append([])

        colonne = 0
        while colonne < largeur:
            bloc = image[ligne:ligne + 8, colonne:colonne + 8]
            blocs[index].append(bloc)
            colonne += 8

        ligne += 8
        index += 1

    return blocs