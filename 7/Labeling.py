import cv2
import numpy as np

# Read the image in grayscale
I = cv2.imread('../images/coins_filled.jpg', 0)

# Apply Otsu's thresholding to binarize the image
thresh, I2 = cv2.threshold(I, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Perform connected components analysis
numLabels, labels, stats, centroids = cv2.connectedComponentsWithStats(I2)

# Print analysis results
print('numLabels:', numLabels)  # Total number of connected components (including background)
print('stats:', stats)          # Statistics of each component: [x, y, width, height, area]
print('centroids:', centroids)  # Centroids (center of mass) of each component

# Show original grayscale image
cv2.imshow('Orj', I)

# Show component labeled as 1
cv2.imshow('1. goruntu', np.uint8(labels == 1) * 255)  # Only component 1 in white, others black

# Show component labeled as 2
cv2.imshow('2. goruntu', np.uint8(labels == 2) * 255)  # Only component 2 in white, others black

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
