# -*- coding: utf-8 -*-

import matplotlib.pyplot as py
from PIL import Image


def getY(R, G, B):
    temp = 0.299 * R + 0.587 * G + 0.114 * B
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return temp


def getCb(B, Y):
    temp = 128 + 0.564 * (B - Y)
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return temp


def getCr(R, Y):
    temp = 128 + 0.713 * (R - Y)
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return temp


def getR(Y, Cr):
    temp = Y + 1.403 * (Cr - 128)
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return int(temp)


def getG(Y, Cr, Cb):
    temp = Y - 0.714 * (Cr - 128) - 0.344 * (Cb - 128)
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return int(temp)


def getB(Y, Cb):
    temp = Y + 1.773 * (Cb - 128)
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return int(temp)


nomImage = "fjords.jpg"

fig1 = py.figure(figsize=(10, 10))
image = py.imread(nomImage)
# py.imshow(image)
# py.show()

hauteur = len(image)
largeur = len(image[0])

# Conversion RGB vers YCbCr 4:4:4
code = image.copy()

for ligne in range(hauteur):
    for colonne in range(largeur):
        pixel = image[ligne][colonne]
        y = getY(pixel[0], pixel[1], pixel[2])
        code[ligne][colonne][0] = getY(pixel[0], pixel[1], pixel[2])
        code[ligne][colonne][1] = getCb(pixel[1], y)
        code[ligne][colonne][2] = getCr(pixel[0], y)

# Conversion YCbCr vers RGB
imageDecode = image.copy()

for ligne in range(hauteur):
    for colonne in range(largeur):
        ycbcr = code[ligne][colonne]
        imageDecode[ligne][colonne] = (getR(ycbcr[0], ycbcr[2]),
                                       getG(ycbcr[0], ycbcr[2], ycbcr[1]),
                                       getB(ycbcr[0], ycbcr[1]))

py.imshow(imageDecode)
py.show()

# Conversion RGB vers YCbCr 4:2:0
code = image.copy()

for ligne in range(hauteur):
    if ligne % 2 == 0:
        for colonne in range(largeur):
            """ Si ligne impaire lire les infos au dessus de sa case sinon calculer ycbcr pour la case 
            courante (si colonne impaire lire la case precedente)
            On test avec un seul Y"""
            if colonne % 2 == 0:
                pixel = image[ligne][colonne]
                y = getY(pixel[0], pixel[1], pixel[2])
                code[ligne][colonne][0] = getY(pixel[0], pixel[1], pixel[2])
                code[ligne][colonne][1] = getCb(pixel[1], y)
                code[ligne][colonne][2] = getCr(pixel[0], y)
            else:
                code[ligne][colonne] = code[ligne][colonne - 1]
    else:
        # Copier la ligne au dessus
        code[ligne] = code[ligne - 1]

# Conversion YCbCr vers RGB
imageDecode = image.copy()

for ligne in range(hauteur):
    for colonne in range(largeur):
        ycbcr = code[ligne][colonne]
        imageDecode[ligne][colonne] = (getR(ycbcr[0], ycbcr[2]),
                                       getG(ycbcr[0], ycbcr[2], ycbcr[1]),
                                       getB(ycbcr[0], ycbcr[1]))

py.imshow(imageDecode)
py.show()
