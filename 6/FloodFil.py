import cv2
import numpy as np

# Load the image in grayscale
l = cv2.imread('../images/coins.png', 0)

# Apply binary thresholding to the image
th, l2 = cv2.threshold(l, 127, 255, cv2.THRESH_BINARY)

# Get the dimensions of the image
h, w = l2.shape[:2]

# Create a copy of the thresholded image
l3 = l2.copy()

# Create a mask for the filling operation
mask = np.zeros((h+2, w+2), np.uint8)

# Apply flood fill
cv2.floodFill(l3, mask, (0, 0), 255)

# Get the inverse of the flood-filled image
l4 = cv2.bitwise_not(l3)

# Apply the "OR" operation between the original thresholded image and the inverted image
sonuc = l2 | l4

sonuc2 = np.bool_(sonuc)

# Print the shape, data type, maximum and minimum values of the result
print(sonuc2.shape)
print(sonuc2.dtype)
print(np.max(sonuc2))
print(np.min(sonuc2))
l[sonuc2] = 128

# Display the images
cv2.imshow('orj', l)
cv2.imshow('l2 binary', l2)
cv2.imshow('l3 floodFill', l3)
cv2.imshow('l4 bitwise_not', l4)
cv2.imshow('sonuc', sonuc)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

# Apply morphological close operation
l5 = cv2.morphologyEx(l4, cv2.MORPH_CLOSE,
                      cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))

# Apply morphological open operation
l5 = cv2.morphologyEx(l5, cv2.MORPH_OPEN,
                      cv2.getStructuringElement(
                          cv2.MORPH_ELLIPSE,
                          (5, 5)))

# Find the coordinates of non-zero pixels
xy = np.column_stack(np.where(l5 > 0))

# Print the shape, data type, maximum and minimum values of the coordinates
print(xy.shape)
print(xy.dtype)
print(np.max(xy))
print(np.min(xy))

# Crop the image based on the coordinates of the non-zero pixels
I6 = l[min(xy[:, 0]):max(xy[:, 0]) + 1, min(xy[:, 1]):max(xy[:, 1]) + 1]

# Display the cropped image
cv2.imshow('I6', I6)
cv2.waitKey(0)
cv2.destroyAllWindows()
