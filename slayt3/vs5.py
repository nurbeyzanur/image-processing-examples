##########################################################
# Renk   dönüşümü
import cv2
import matplotlib.pyplot as plt

I=cv2.imread(r"images/cicek.jpg",1)
#           GRİ RENGE ÇEVİRME
I2=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('image Gray',I2)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(I2)
plt.show()

#BGR OLAN RESMİ RGB HALE ÇEVİRME
I2=cv2.cvtColor(I,cv2.COLOR_BGR2RGB)
cv2.imshow('image Gray',I2)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(I2)
plt.show()

#   HSV RENK DÖNÜŞÜMÜ
I2=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('image Gray',I2)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(I2)
plt.show()

# Resmi kaydet
cv2.imwrite(r"createimg/peppers_new1.tif", I2)



