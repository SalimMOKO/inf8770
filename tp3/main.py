import cv2
import numpy as np
import math
from matplotlib import pyplot as py

DETECTION_FONDU = 10000
DETECTION_COUPURE = 21882


def main():
    fondus = []
    differencesHist = []
    indexImage = 1
    quantification = []
    quantificationArray = []
    capture = cv2.VideoCapture("julia.avi")
    ret, frame = capture.read()
    print('Traitement des images en cours ...')
    while ret:
        if frame is not None:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        masks = createMasks(img)
        current = createHists(masks,img)
        for i in range(0, len(current), 32):
            quantification.append(current[i:i + 32].sum())
        quantificationArray.append(quantification)
        if(indexImage >1 ):
            difference = getMasksDifference(np.array(quantificationArray[indexImage-1]), np.array(quantificationArray[indexImage-2]))
            differencesHist.append(difference)
            fondus = checkMaskDifferences(difference,indexImage,fondus)

        indexImage=indexImage+1
        quantification = []
        ret, frame = capture.read()
    print("End of video at ", indexImage)
    fondus,coupures = filter(fondus,differencesHist)
    print('Tableau des fondus : ')
    print(fondus)
    print('________________________________________________________')
    print('Tableau des coupures : ')
    print(coupures)
    print('________________________________________________________')
    py.plot(differencesHist)
    py.show()
    capture.release()
    cv2.destroyAllWindows()


def createMasks(img):
    masks = []
    for i in range(0,8):
        for j in range(0,8):
            mask = np.zeros(img.shape[:2], np.uint8)
            mask[math.floor(img.shape[0] * i / 8):math.floor((i + 1) * img.shape[0] / 8),
            math.floor(j * img.shape[1] / 8):math.floor((j + 1) * img.shape[1] / 8)] = 255
            masks.append(mask)
    return masks


def createHists(masks,img):
    hists = []
    for i in range(0,len(masks)):
        hists.append(cv2.calcHist([img], [0], masks[i], [256], [0, 256]))
        hists.append(cv2.calcHist([img], [1], masks[i], [256], [0, 256]))
        hists.append(cv2.calcHist([img], [2], masks[i], [256], [0, 256]))
    total = np.concatenate(hists)
    return total


def getMasksDifference(current,previous):
    difference = math.sqrt((np.square(current - previous)).sum())
    return difference


def checkMaskDifferences(difference,indexImage,fondus):
    if difference >= DETECTION_FONDU :
        fondus.append(indexImage)
    return fondus


def filter(fondus,differenceHists):
    fonduArray = []
    potentialCut = []
    coupures = []
    for i in range(0,len(fondus)-1):
        if(fondus[i+1] - fondus[i] == 1 ):
            if(fondus[i] not in fonduArray):
                fonduArray.append(fondus[i])
            fonduArray.append(fondus[i+1])
        else :
            potentialCut.append(fondus[i])
    if(fondus[len(fondus)-1]-fondus[len(fondus)-2] != 1):
        potentialCut.append(fondus[len(fondus)-1])
    for i in range(0,len(potentialCut)):
        if(differenceHists[potentialCut[i]-2]>DETECTION_COUPURE):
            coupures.append(potentialCut[i])
    return fonduArray,coupures

def printSolutionImages(coupures, fondus):
    capture = cv2.VideoCapture("julia.avi")
    ret, frame = capture.read()
    indexImage = 1
    while ret:
        if frame is not None:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if indexImage in  coupures or indexImage in fondus:
            py.plot(img)
            py.show()

def printSolutionImages(coupures, fondus):
    capture = cv2.VideoCapture("julia.avi")
    ret, frame = capture.read()
    indexImage = 1
    while ret:
        if frame is not None:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if indexImage in  coupures or indexImage in fondus:
            py.plot(img)
            py.show()

main()
