# -*- coding: utf-8 -*-

import numpy as np


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


def RGBtoYCbCr444(image):
    hauteur = len(image)
    largeur = len(image[0])
    code = np.zeros_like(image)

    for ligne in range(hauteur):
        for colonne in range(largeur):
            pixel = image[ligne][colonne]
            y = getY(pixel[0], pixel[1], pixel[2])
            code[ligne][colonne][0] = getY(pixel[0], pixel[1], pixel[2])
            code[ligne][colonne][1] = getCb(pixel[2], y)
            code[ligne][colonne][2] = getCr(pixel[0], y)

    return code


def YCbCr444toRGB(code):
    hauteur = len(code)
    largeur = len(code[0])
    imageDecode = np.zeros_like(code)

    for ligne in range(hauteur):
        for colonne in range(largeur):
            ycbcr = code[ligne][colonne]
            imageDecode[ligne][colonne] = (getR(ycbcr[0], ycbcr[2]),
                                           getG(ycbcr[0], ycbcr[2], ycbcr[1]),
                                           getB(ycbcr[0], ycbcr[1]))

    return imageDecode.astype('uint8')


def RGBtoYCbCr420(image):
    hauteur = len(image)
    largeur = len(image[0])
    code = np.zeros_like(image)

    for ligne in range(hauteur):
        if ligne % 2 == 0:
            for colonne in range(largeur):
                pixel = image[ligne][colonne]
                y = getY(pixel[0], pixel[1], pixel[2])
                if colonne % 2 == 0:
                    code[ligne][colonne][0] = y
                    code[ligne][colonne][1] = getCb(pixel[2], y)
                    code[ligne][colonne][2] = getCr(pixel[0], y)
                else:
                    code[ligne][colonne] = code[ligne][colonne - 1]
                    code[ligne][colonne][0] = y
        else:
            code[ligne] = code[ligne - 1]
            for colonne in range(largeur):
                pixel = image[ligne][colonne]
                code[ligne][colonne][0] = getY(pixel[0], pixel[1], pixel[2])

    return code


def YCbCr420toRGB(code):
    hauteur = len(code)
    largeur = len(code[0])
    imageDecode = np.zeros_like(code)

    for ligne in range(hauteur):
        for colonne in range(largeur):
            ycbcr = code[ligne][colonne]
            imageDecode[ligne][colonne] = (getR(ycbcr[0], ycbcr[2]),
                                           getG(ycbcr[0], ycbcr[2], ycbcr[1]),
                                           getB(ycbcr[0], ycbcr[1]))

    return imageDecode.astype('uint8')
