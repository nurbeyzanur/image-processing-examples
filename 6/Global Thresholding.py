import cv2
import numpy as np

# Load the image in grayscale.
I = cv2.imread('../images/threshold.jpg', 0)
cv2.imshow('I', I)

# Apply binary thresholding to the image
th ,I2= cv2.threshold(I, 0, 255, cv2.THRESH_BINARY)
cv2.imshow('I2', I2)

# Apply fixed thresholding (127)
th1,I3=cv2.threshold(I, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('I3', I3)

# Apply different fixed thresholding (0-128)
th2,I4=cv2.threshold(I, 0, 128, cv2.THRESH_BINARY)
cv2.imshow('I4', I4)

# Apply Otsu's thresholding.
th3,I5=cv2.threshold(I,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('I5', I5)

cv2.waitKey(0)
cv2.destroyAllWindows()

