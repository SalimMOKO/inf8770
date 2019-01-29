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

LUToctetsdispo = [True] * 256
dictsymb = [Message[0]]
LUToctetsdispo[ord(Message[0])] = False
nbsymboles = 1
for i in range(1, len(Message)):
    if Message[i] not in dictsymb:
        dictsymb += [Message[i]]
        LUToctetsdispo[ord(Message[i])] = False  # Octet utilisé
        nbsymboles += 1

longueurOriginale = np.ceil(np.log2(nbsymboles)) * len(Message)

dictsymb = []  # Dictionnaire des substitutions
debut = ord(Message[0])  # Origine trouver un code de substitution. Et pour avoir des caractères imprimables...

remplacementpossible = True
while remplacementpossible:
    # Recherche des paires
    paires = []
    for i in range(0, len(Message) - 1):
        temppaire = Message[i] + Message[i + 1]
        if not list(filter(lambda x: x[0] == temppaire, paires)):  # Si la liste retournée par filter est vide.
            # au lieu de ; len(re.findall(temppaire, Message, overlapped=True))
            occurences = Message.count(temppaire)
            paires += [[temppaire, occurences]]

    # Trouve la paire avec le plus de répétitions.
    paires = sorted(paires, key=lambda x: x[1], reverse=True)

    if paires[0][1] > 1:
        # Remplace la paire
        print(paires)
        print("La paire ", paires[0][0], " est la plus fréquente avec ", paires[0][1], "répétitions")
        # Cherche un octet non utilisé
        while debut < 256 and LUToctetsdispo[debut] == False:
            debut += 1
        if debut < 256:
            # On substitut
            Message = Message.replace(paires[0][0], chr(debut))
            LUToctetsdispo[debut] = False
            dictsymb += [[paires[0][0], chr(debut)]]
        else:
            # Bien sûr, ce n'est pas exact car la recherche commence à Message[0]
            print("Il n'y a plus d'octets disponible!")

        print(Message)
        print(dictsymb)
    else:
        remplacementpossible = False

print("Longueur = {0}".format(np.ceil(np.log2(nbsymboles))*len(Message)))
print("Longueur originale = {0}".format(longueurOriginale))
