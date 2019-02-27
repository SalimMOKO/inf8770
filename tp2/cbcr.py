# -*- coding: utf-8 -*-

import matplotlib.pyplot as py
from PIL import Image

# Etape 1 : Conversion RGB/YCBCR avec sous echantillonnage 4 : 2 : 0
nomImage = "fjords.jpg"
hauteur = 400
largeur = 600

fig1 = py.figure(figsize=(10, 10))
image = py.imread(nomImage)
# py.imshow(image)
# py.show()

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
    return temp


def getG(Y, Cr, Cb):
    temp = Y - 0.714 * (Cr - 128) - 0.344 * (Cb - 128)
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return temp


def getB(Y, Cb):
    temp = Y + 1.773 * (Cb - 128)
    if temp > 255:
        return 255
    elif temp < 0:
        return 0
    return temp


# Conversion 4:2:0
code = []
for ligne in range(hauteur):
    code.append([])
    if ligne % 2 != 0:
        for colonne in range(largeur):
            pixel = image[ligne][colonne]
            y = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
            code[ligne].append([y, 0, 0])
    else:
        for colonne in range(largeur):
            pixel = image[ligne][colonne]
            y = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
            if colonne % 2 != 0:
                code[ligne].append([y, 0, 0])
            else:
                cb = 128 + 0.564 * (pixel[2] - y)
                cr = 128 + 0.713 * (pixel[0] - y)
                code[ligne].append([y, cb, cr])

# INVERSE : Conversion
imageDecode = Image.new('RGB', (largeur, hauteur), "black")
pixels = imageDecode.load()

for colonne in range(largeur):
    for ligne in range(hauteur):
        ycbcr = code[ligne][colonne]
        r = ycbcr[0] + 1.403 * (ycbcr[2] - 128)
        g = ycbcr[0] - 0.714 * (ycbcr[2] - 128) - 0.344 * (ycbcr[1] - 128)
        b = ycbcr[0] + 1.773 * (ycbcr[1] - 128)
        pixels[colonne, ligne] = (int(getR(ycbcr[0], ycbcr[2])), int(g), int(b))

py.imshow(imageDecode)
py.show()
#