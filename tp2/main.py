# -*- coding: utf-8 -*-

import ycbcr_converter as ycbcr
import bloc_divider as bdiv
import matplotlib.pyplot as py
import huffman
import parplages
import discreteCosineTransform as dct

image = py.imread('C:/Users/USER/Desktop/INF8770_TP2/inf8770/tp2/fjords.jpg').astype('float')

code420 = ycbcr.RGBtoYCbCr420(image)
decode420 = ycbcr.YCbCr420toRGB(code420)
# py.imshow(decode420)
# py.show()

code444 = ycbcr.RGBtoYCbCr444(image)
decode444 = ycbcr.YCbCr444toRGB(code444)
# py.imshow(decode444)
# py.show()

blocs = bdiv.divider8by8(image)
blocs = blocs.astype('float64')

dctImage = dct.dct(blocs)

imageQuantifiee = dct.quantification(dctImage)

imageDequantifiee = dct.reverseQuantification(imageQuantifiee)

imageReverseDCT = dct.reversedct(imageDequantifiee)

image = bdiv.inverseDivision8x8(imageReverseDCT, image)
image = image.astype('uint8')
py.imshow(image)
py.show()

# Taux de compression :
# Longueur originale => nombre de pixels x 3 couleurs x 8 bits
# Longueur finale => nombre de bits de la chaine de bits
