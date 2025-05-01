import cv2

# OpenCV sürümünü yazdır
print(cv2.__version__)

# Görüntüyü yükle
I = cv2.imread(r"C:\Users\EBG\Desktop\sgi\discovery\images\peppers.png")
# eğer
# renkli isteniyorsa ,1
# gri tonlamalı isteniyorsa ,0
# yazılmalı


# Görüntüyü göster
cv2.imshow("Peppers", I)

# Kullanıcı bir tuşa basana kadar bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()

I2=I.copy()
# copy metodu parametre alamaz
cv2.imshow("Peppers", I2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#BGR formattan  gri tonlamalı fonta geçiş yapıldı.
I3=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow("Peppers", I3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#######################################################
#######----------PAGE 5----------------------##########

I=cv2.imread(r"images/peppers.png",1)
cv2.imshow("Peppers", I)


print("image properties peppers.png")
print("Type: ", type(I))
# <class 'numpy.ndarray'>
print("Shape: ", I.shape)
#  (384, 512, 3)
#  384: Görüntünün yüksekliği (satır sayısı).
# 512: Görüntünün genişliği (sütun sayısı).
# 3: Görüntünün kanal sayısı (Renkli bir görüntüde RGB kanalları olur, yani Kırmızı (Red), Yeşil (Green), Mavi (Blue)).

print("Dimensions: ", I.ndim)
# değişkeninin kaç boyutlu olduğunu gösterir.
print("Data type: ", I.dtype)
# görüntüdeki piksel değerlerinin veri tipini
print("Number of Pixels: ", I.size)
# toplam eleman sayısını (piksel sayısını) gösterir.
# Piksel sayısı, I.shape değerlerinin çarpımıdı
cv2.waitKey(0)
cv2.destroyAllWindows()

#-----------------PAGE 7-------------------#
I=cv2.imread(r"images/peppers.png",1)
print(I[50,50,:])
# Belirli noktadaki pixelin  bgr rengini alırnp dizisi olur


