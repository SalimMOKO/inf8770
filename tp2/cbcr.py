# -*- coding: utf-8 -*-

import matplotlib.pyplot as py


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


def RGBtoYCbCr444(nomImage):
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


def RGBtoYCbCr420(nomImage):
    image = py.imread(nomImage)
    hauteur = len(image)
    largeur = len(image[0])
    code = image.copy()

    for ligne in range(hauteur):
        if ligne % 2 == 0:
            for colonne in range(largeur):
                """ TODO: Calculer les Y """
                pixel = image[ligne][colonne]
                y = getY(pixel[0], pixel[1], pixel[2])
                if colonne % 2 == 0:
                    code[ligne][colonne][0] = y
                    code[ligne][colonne][1] = getCb(pixel[1], y)
                    code[ligne][colonne][2] = getCr(pixel[0], y)
                else:
                    code[ligne][colonne] = code[ligne][colonne - 1]
                    code[ligne][colonne][0] = y
        else:
            # Copier la ligne au dessus
            code[ligne] = code[ligne - 1]
            for colonne in range(largeur):
                pixel = image[ligne][colonne]
                code[ligne][colonne][0] = getY(pixel[0], pixel[1], pixel[2])

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


# Main :
RGBtoYCbCr420("fjords.jpg")
