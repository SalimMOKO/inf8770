import cv2
import numpy as np
import matplotlib.pyplot as py

capture = cv2.VideoCapture("julia.avi")

for i in range(2):
    ret, frame = capture.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    py.imshow(image)
    py.show()

capture.release()
cv2.destroyAllWindows()
