import cv2
import numpy as np

I=cv2.imread('../images/contour.jpg',0)

th,I2=cv2.threshold(I,127,255,cv2.THRESH_BINARY)
combined = np.hstack((I,I2))

# Pencereyi göster
cv2.imshow("Yan Yana Resimler", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()