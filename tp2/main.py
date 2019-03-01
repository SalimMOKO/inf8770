# -*- coding: utf-8 -*-

import ycbcr_converter as ycbcr
import bloc_divider as bdiv
import matplotlib.pyplot as py
import discreteCosineTransform as dct
import zigzag as zz

image = py.imread('fjords.jpg').astype('float')

code420 = ycbcr.RGBtoYCbCr420(image)
decode420 = ycbcr.YCbCr420toRGB(code420)

code444 = ycbcr.RGBtoYCbCr444(image)
decode444 = ycbcr.YCbCr444toRGB(code444)

# Division par bloc 8x8
blocs = bdiv.divider8by8_blocs(code420)
blocs = blocs.astype('float64')

# Calcul des coefficients pour les fonctions cosinus
dctImage = dct.discreteCosineTransform(blocs)
# Quantification des coefficients des fonctions cosinus
imageQuantifiee = dct.quantification(dctImage)
# lecture en zigzag
zigzagString = ''
for bloc in imageQuantifiee:
            zigzag = list(map(str,zz.zig_zag(bloc,8)))
            binary_string = ','.join(zigzag)
            zigzagString += binary_string
print(zigzagString)

# Inverser la quantification
imageDequantifiee = dct.reverseQuantification(imageQuantifiee)
# Inverser le calcul des coefficients en recupérant les valeurs ycbcr
imageReverseDCT = dct.reverseDCT(imageDequantifiee)
# Reconstitution de l'image à partir des blocs 8x8
imageReconstituee = bdiv.rebuildFrom8by8(imageReverseDCT)
# Recupération des RGB depuis ycbcr
imageReconstituee = ycbcr.YCbCr420toRGB(imageReconstituee).astype('uint8')
# Affichage de l'image reconstituée
py.imshow(imageReconstituee)
py.show()

# Taux de compression :
# Longueur originale => nombre de pixels x 3 couleurs x 8 bits
# Longueur finale => nombre de bits de la chaine de bits
