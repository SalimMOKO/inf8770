# -*- coding: utf-8 -*-

import matplotlib.pyplot as py
from PIL import Image

# Etape 1 : Conversion RGB/YCBCR avec sous echantillonnage 4 : 2 : 0

"""
Y′= 0.299R+ 0.587G+ 0.114B
CB= 128 + 0.564(B−Y′)
CR= 128 + 0.713(R−Y′)
R=Y′+ 1.403(CR−128)
G=Y′−0.714(CR−128)−0.344(CB−128)
B=Y′+ 1.773(CB−128)
"""


def getY(R, G, B):
    temp = 0.299 * R + 0.587 * G + 0.114 * B
    if temp > 255:
        print('255')
        return 255
    elif temp < 0:
        print('0')
        return 0
    return temp


def getCb(B, Y):
    temp = 128 + 0.564 * (B - Y)
    if temp > 255:
        print('255')
        return 255
    elif temp < 0:
        print('0')
        return 0
    return temp


def getCr(R, Y):
    temp = 128 + 0.713 * (R - Y)
    if temp > 255:
        print('255')
        return 255
    elif temp < 0:
        print('0')
        return 0
    return temp


def getR(Y, Cr):
    temp = Y + 1.403 * (Cr - 128)
    if temp > 255:
        print('255')
        return 255
    elif temp < 0:
        print('0')
        return 0
    return int(temp)


def getG(Y, Cr, Cb):
    temp = Y - 0.714 * (Cr - 128) - 0.344 * (Cb - 128)
    if temp > 255:
        print('255')
        return 255
    elif temp < 0:
        print('0')
        return 0
    return int(temp)


def getB(Y, Cb):
    temp = Y + 1.773 * (Cb - 128)
    if temp > 255:
        print('255')
        return 255
    elif temp < 0:
        print('0')
        return 0
    return int(temp)


nomImage = "fjords.jpg"

fig1 = py.figure(figsize=(10, 10))
image = py.imread(nomImage)
# py.imshow(image)
# py.show()

hauteur = len(image) - 1
largeur = len(image[0]) - 1

# Conversion 4:4:4
code = image.copy()

for ligne in range(hauteur):
    for colonne in range(largeur):
        pixel = image[ligne][colonne]
        y = getY(pixel[0], pixel[1], pixel[2])
        code[ligne][colonne][0] = getY(pixel[0], pixel[1], pixel[2])
        code[ligne][colonne][1] = getCb(pixel[1], y)
        code[ligne][colonne][2] = getCr(pixel[0], y)

# INVERSE : Conversion
imageDecode = image.copy()

for ligne in range(hauteur):
    for colonne in range(largeur):
        ycbcr = code[ligne][colonne]
        imageDecode[ligne][colonne] = (getR(ycbcr[0], ycbcr[2]),
                                       getG(ycbcr[0], ycbcr[2], ycbcr[1]),
                                       getB(ycbcr[0], ycbcr[1]))

py.imshow(imageDecode)
py.show()
