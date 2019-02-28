import matplotlib.pyplot as py
import numpy as np

import matplotlib.pyplot as py
import numpy as np
import scipy.fftpack as dctpack

image = py.imread("fjords.jpg")

hauteur = len(image)
largeur = len(image[0])

blocs = []

# Division

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

# Reconstruction
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

py.imshow(imageReconstruite)
py.show()

BlocImage = bloc [0:8,0:8]
blocY = bloc[:,:,0].astype('int8')
BlocDCT = np.zeros((8,8))
print('Bloc de image:\n',blocY,'\n')

#On soustrait 128 pour avoir en signal oscillant autour de zéro
blocY = blocY - 128
print('Bloc de image:\n',blocY,'\n')
#DCT en 2 étapes. La DCT est une transformation séparable. On peut appliquer en X et ensuite en Y.
BlocDCT = dctpack.dct(dctpack.dct(blocY, axis=0, norm='ortho'), axis=1, norm='ortho')
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print('Bloc après DCT:\n',BlocDCT)

Quant1= np.matrix('16 11 10 16 24 40 51 61;\
    12 12 14 19 26 58 60 55;\
    14 13 16 24 40 57 69 56;\
    14 17 22 29 51 87 80 62;\
    18 22 37 56 68 109 103 77;\
    24 35 55 64 81 104 103 92;\
    49 64 78 77 103 121 120 101;\
    72 92 95 98 112 100 103 99').astype('float')
BlocQuant1 = np.round(np.divide(BlocDCT, Quant1))
print('Bloc quantifié:\n',BlocQuant1,'\n')
#Quantification et transformation inverse
BlocDCTavecP1 = np.multiply(BlocQuant1,Quant1)
BlocImageavecP1 = dctpack.idct(dctpack.idct(BlocDCTavecP1, axis=0, norm='ortho'), axis=1, norm='ortho') + 128
print('Bloc image reconstruit:\n',BlocImageavecP1,'\n')

blocY = blocY + 128
print('Erreurs dues à la quantification:\n',np.abs(BlocImageavecP1-blocY))