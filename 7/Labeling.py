import cv2
import numpy as np
I = cv2.imread('../images/coins_filled.jpg',0)
thresh,I2 = cv2.threshold(I, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
numLabels, labels, stats, centroids = cv2.connectedComponentsWithStats(I2)
print('numLabels:', numLabels)
print('stats:',stats)
print('centroids:',centroids)
cv2.imshow('Orj',I)
cv2.imshow('1. goruntu',np.uint8(labels==1)*255)
cv2.imshow('2. goruntu',np.uint8(labels==2)*255)
cv2.waitKey(0)
cv2.destroyAllWindows()
