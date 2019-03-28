import cv2
import numpy as np
import matplotlib.pyplot as py

capture = cv2.VideoCapture("julia.avi")

ret, frame = capture.read()
index = 0

# First frame treatment
framePrec = frame
index += 1

while ret:
    if frame is not None:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # py.imshow(image)
    # py.show()
    framePrec = frame
    index += 1
    ret, frame = capture.read()

print("End of video at ", index)
capture.release()
cv2.destroyAllWindows()
