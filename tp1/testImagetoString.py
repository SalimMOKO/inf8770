import numpy as np
import regex as re
import matplotlib.pyplot as py


def rgb2gray(rgb):
    return np.dot(rgb[:, :], [0.299, 0.587, 0.114])


def toASCII(element):
    return chr(int(element))


fig1 = py.figure(figsize=(10, 10))
imagelue = py.imread('test4.jpg')
image = imagelue.astype('float')
image = rgb2gray(image)
imageout = image.astype('uint8').astype('str').flatten()
imageout = list(map(toASCII, imageout))

Message = ''.join(imageout)

# Message to image :

imageRecons = list(map(int, list(Message))).astype('float')

py.imsave('output.jpg', imageRecons)





