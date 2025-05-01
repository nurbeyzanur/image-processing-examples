import cv2
import matplotlib.pyplot as plt
import numpy as np
##############################################
# görüntü boyutlarını arama syf12
I=cv2.imread(r"images/cicek.jpg",1)
bgr_cicek = I.copy()

I_r=bgr_cicek[2] # Kırmızı boyutu ifade etmektedir.
I_g=bgr_cicek[1]
I_b=bgr_cicek[0]

bgr_cicek[0]= I_r
bgr_cicek[2]= I_b

I_rgb = cv2.merge(bgr_cicek) # resim yeniden oluşturuluyor

I_b, I_g, I_r = cv2.split(I)
I_rgb = cv2.merge((I_r, I_g, I_b)) # resim yeniden oluşturuyor

cv2.imshow('RGB goruntunun R kanali', I_r)
cv2.imshow('RGB goruntunun G kanali', I_g)
cv2.imshow('RGB goruntunun B kanali', I_b)
cv2.imshow('RGB goruntu', I)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(I_rgb)
plt.show()
plt.imshow(I_r)
plt.show()
plt.imshow(I_g)
plt.show()
plt.imshow(I_b)
plt.show()

###################################################################
# Her bir kanal ve RGB görüntüsünü alt grafiklerde göster
plt.figure(figsize=(10, 10))

# RGB görüntüsü
plt.subplot(2, 2, 1)
plt.imshow(I_rgb)
plt.title('RGB Görüntüsü')
plt.axis('off')

# Kırmızı kanal
plt.subplot(2, 2, 2)
plt.imshow(I_r, cmap='Reds')  # Kırmızı kanalı göster
plt.title('Kırmızı Kanal')
plt.axis('off')

# Yeşil kanal
plt.subplot(2, 2, 3)
plt.imshow(I_g, cmap='Greens')  # Yeşil kanalı göster
plt.title('Yeşil Kanal')
plt.axis('off')

# Mavi kanal
plt.subplot(2, 2, 4)
plt.imshow(I_b, cmap='Blues')  # Mavi kanalı göster
plt.title('Mavi Kanal')
plt.axis('off')

# Göster
plt.show()




