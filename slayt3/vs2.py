import cv2
from matplotlib import pyplot as plt
I=cv2.imread(r"images/peppers.png",1)

plt.figure()
#Yeni bir şekil (figure) oluşturur. Bu, bir pencere açılmasını sağlar.
plt.title('Image Peppers Orj')
# Grafiğin üstüne "Image Peppers Orj" başlığını ekler.
plt.imshow(I)
plt.show()
#  Matplotlib (plt.imshow) görüntüleri RGB formatında bekler.
# Ancak OpenCV (cv2.imread) görüntüleri varsayılan olarak BGR formatında yükler.
# cv2.cvtColor(I, cv2.COLOR_BGR2RGB) bunu kullanarak düzeltebilirz
plt.waitforbuttonpress()
# Kullanıcı bir tuşa basana kadar pencerenin açık kalmasını sağlar.
plt.close()
# Açık olan Matplotlib penceresini kapatır.

plt.xticks([]), plt.yticks([])
#Eksenleri kaldırmak için kullanılır.
plt.imshow(I, cmap='gray', interpolation='nearest')
plt.show()
plt.close()
plt.imshow(I, cmap='binary')
plt.show()
plt.close()

plt.figure()
plt.title('Binary Image-1')
plt.xticks([]), plt.yticks([])
plt.imshow(I, cmap='viridis', interpolation='nearest')
plt.show()


