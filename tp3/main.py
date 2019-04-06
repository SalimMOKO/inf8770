import cv2
import image_slicer
import os
import numpy as np
import matplotlib.pyplot as py
from PIL import Image

capture = cv2.VideoCapture("julia.avi")

ret, frame = capture.read()
index = 0

# First frame treatment
framePrec = frame
index += 1

# Division en plus petites images
nom = "test"
ext = ".png"
cv2.imwrite(nom + ext, frame)
image_slicer.slice(nom + ext, 4)

# Do something with files
# nom = test => test_01_01, test_01_02, test_02_01, test_02_02

# Haut gauche
nom_image_01_01 = nom + "_01_01" + ext
# Haut droite
nom_image_01_02 = nom + "_01_02" + ext
# Bas gauche
nom_image_02_01 = nom + "_02_01" + ext
# Bas droite
nom_image_02_02 = nom + "_02_02" + ext

image_01_01 = py.imread(nom_image_01_01)
image_01_02 = py.imread(nom_image_01_02)
image_02_01 = py.imread(nom_image_02_01)
image_02_02 = py.imread(nom_image_02_02)

# Remove all png files
filelist = [f for f in os.listdir(".") if f.endswith(".png")]
for f in filelist:
    os.remove(os.path.join(".", f))

py.imshow(image_01_01)
py.show()

py.imshow(image_01_02)
py.show()

py.imshow(image_02_01)
py.show()

py.imshow(image_02_02)
py.show()

# while ret:
#     if frame is not None:
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # py.imshow(image)
#     # py.show()
#     framePrec = frame
#     index += 1
#     ret, frame = capture.read()

print("End of video at ", index)
capture.release()
cv2.destroyAllWindows()
