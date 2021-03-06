import numpy as np
import matplotlib.pyplot as py
import time
import codage_huffman as huffman


def rgb2gray(rgb):
    return np.dot(rgb[:, :], [0.299, 0.587, 0.114])


def toASCII(element):
    return chr(int(element))


start = time.time()
nomImage = 'Image01hyp03.jpg'

fig1 = py.figure(figsize=(10, 10))
imagelue = py.imread(nomImage)
image = imagelue.astype('float')
image = rgb2gray(image)
imageout = image.astype('uint8')

col = image[:, 0]
image = np.column_stack((col, image))
col = image[:, len(image[0])-1]
image = np.column_stack((col, image))
row = image[0, :]
image = np.row_stack((row, image))
row = image[len(image)-1, :]
image = np.row_stack((row, image))

matpred = [[0.33, 0.33], [0.33, 0.0]]

imagepred = np.zeros((len(image)-2, len(image[0])-2))
for i in range(1, len(image)-2):
    for j in range(1, len(image[0])-2):
        imagepred[i][j] = image[i-1][j-1]*matpred[0][0]+image[i-1][j]*matpred[0][1]+image[i][j-1]*matpred[1][0]

imageout = imagepred.astype('uint8').astype('str').flatten()

# Application de Huffman
imageout = list(map(toASCII, imageout))
Message = ''.join(imageout)
huffman.codage(Message)

end = time.time()

print('Temps d\'execution du programme', end - start, 'secondes')
