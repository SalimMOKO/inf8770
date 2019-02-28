# -*- coding: utf-8 -*-

import matplotlib.pyplot as py
import numpy as np


image = py.imread("fjords.jpg")

hauteur = len(image)
largeur = len(image[0])




def divider8by8(image):
    if len(image) % 8 != 0 or len(image[0]) % 8 != 0:
        print 'Erreur image non compatible'
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
