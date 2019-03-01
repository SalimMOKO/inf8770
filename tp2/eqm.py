# -*- coding: utf-8 -*-


def calculErreurQuadratiqueMoyenne(imageOriginale, imageConvertie):
    hauteur = len(imageOriginale)
    largeur = len(imageOriginale[0])

    sommeR = 0
    sommeG = 0
    sommeB = 0

    for ligne in range(hauteur):
        for colonne in range(largeur):
            erreurR = (imageOriginale[ligne][colonne][0] - imageConvertie[ligne][colonne][0]) ** 2
            erreurG = (imageOriginale[ligne][colonne][1] - imageConvertie[ligne][colonne][1]) ** 2
            erreurB = (imageOriginale[ligne][colonne][2] - imageConvertie[ligne][colonne][2]) ** 2

            sommeR += erreurR
            sommeG += erreurG
            sommeB += erreurB

    eqmR = sommeR / (hauteur * largeur)
    eqmG = sommeG / (hauteur * largeur)
    eqmB = sommeB / (hauteur * largeur)

    print('EQM R :', eqmR)
    print('EQM G :', eqmG)
    print('EQM B :', eqmB)
