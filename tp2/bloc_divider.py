# -*- coding: utf-8 -*-

import matplotlib.pyplot as py
import numpy as np


def divider8by8_blocs(image):
    hauteur = len(image)
    largeur = len(image[0])
    if len(image) % 8 != 0 or len(image[0]) % 8 != 0:
        print('Erreur image non compatible')
        return -1
    blocs = []
    ligne = 0
    while ligne < hauteur:
        colonne = 0
        while colonne < largeur:
            blocs.append(image[ligne:ligne + 8, colonne:colonne + 8])
            colonne += 8
        ligne += 8
    return np.array(blocs)


def rebuildFrom8by8(blocs):
    image = py.imread("fjords.jpg")
    hauteur = len(image)
    largeur = len(image[0])
    imageReconstruite = np.zeros_like(image)
    ligne = 0
    indexCBlocs = 0
    while ligne < hauteur:
        colonne = 0
        while colonne < largeur:
            imageReconstruite[ligne:ligne + 8, colonne:colonne + 8] = blocs[indexCBlocs]
            indexCBlocs += 1
            colonne += 8
        ligne += 8
    return imageReconstruite
