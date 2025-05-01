import cv2
import numpy as np

# Görüntüyü gri tonlamalı olarak yükle
l=cv2.imread('../images/coins.png',0)

# Görüntüye ikili eşikleme uygula
th,l2=cv2.threshold(l,127,255,cv2.THRESH_BINARY)

# Görüntünün boyutlarını al
h, w = l2.shape[:2]

# Eşiklenmiş görüntünün bir kopyasını oluştur
l3=l2.copy()

# Dolgu için maske oluştur
mask = np.zeros((h+2, w+2), np.uint8)

# Dolgu uygula
cv2.floodFill(l3, mask, (0,0), 255)

# Dolgu uygulanmış görüntünün tersini al
l4 = cv2.bitwise_not(l3)

# Orijinal eşiklenmiş görüntü ile tersi alınmış görüntüyü "veya" işlemine tabi tut
sonuc = l2 | l4

sonuc2=np.bool_(sonuc)

print(sonuc2.shape)
print(sonuc2.dtype)
print(np.max(sonuc2))
print(np.min(sonuc2))
l[sonuc2]=128

# Görüntüleri göster
cv2.imshow('orj',l)
cv2.imshow('l2 binary',l2)
cv2.imshow('l3 floodFill',l3)
cv2.imshow('l4 bitwise_not',l4)
cv2.imshow('sonuc',sonuc)

# Herhangi bir tuşa basılmasını bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()

l5 = cv2.morphologyEx(l4, cv2.MORPH_CLOSE,
                      cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))
l5 = cv2.morphologyEx(l5, cv2.MORPH_OPEN,
                      cv2.getStructuringElement(
                          cv2.MORPH_ELLIPSE,
                          (5, 5)))

xy = np.column_stack(np.where(l5 > 0))
print(xy.shape)
print(xy.dtype)
print(np.max(xy))
print(np.min(xy))
I6=l[min(xy[:,0]):max(xy[:,0])+1 , min(xy[:,1]):max(xy[:,1])+1]
cv2.imshow('I6',I6)
cv2.waitKey(0)
cv2.destroyAllWindows()
