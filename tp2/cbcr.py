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

hauteur = len(image) - 1
largeur = len(image[0]) - 1

# py.imshow(image)
# py.show()

# Conversion 4:2:0
code = []
for ligne in range(hauteur):
    code.append([])
    code.append([])
    for colonne in range(largeur):
        # Case haut-gauche
        pixel = image[ligne][colonne]
        y = getY(pixel[0], pixel[1], pixel[2])
        cb = getCb(pixel[1], y)
        cr = getCr(pixel[0], y)
        code[ligne].append([y, cb, cr])

        # Case haut-droite
        pixel = image[ligne][colonne + 1]
        y = getY(pixel[0], pixel[1], pixel[2])
        code[ligne].append([y, cb, cr])

        # Case bas-gauche
        pixel = image[ligne + 1][colonne]
        y = getY(pixel[0], pixel[1], pixel[2])
        code[ligne + 1].append([y, cb, cr])

        # Case bas-droite
        pixel = image[ligne + 1][colonne + 1]
        y = getY(pixel[0], pixel[1], pixel[2])
        code[ligne + 1].append([y, cb, cr])

        # On saute une colonne
        colonne += 1

    # On saute une ligne
    ligne += 1

    """if ligne % 2 != 0:
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
            code[ligne].append([y, cb, cr])"""


# INVERSE : Conversion
imageDecode = Image.new('RGB', (largeur, hauteur), "black")
pixels = imageDecode.load()

for ligne in range(hauteur):
    for colonne in range(largeur):
        ycbcr = code[ligne][colonne]
        pixels[colonne, ligne] = (getR(ycbcr[0], ycbcr[2]), getG(ycbcr[0], ycbcr[2], ycbcr[1]), getB(ycbcr[0], ycbcr[1]))

py.imshow(imageDecode)
py.show()
