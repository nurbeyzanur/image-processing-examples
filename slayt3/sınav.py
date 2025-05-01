import cv2
import numpy as np
I=cv2.imread(r'images/peppers.png', 1)
# Görüntüyü BGR kanallarına ayır
r = cv2.split(I)

I_small = cv2.resize(I, (200, 200))
cv2.imshow('200x200 boyutuna getirilmis resim', I_small)
cv2.waitKey(0)
cv2.destroyAllWindows()


I_small2 = cv2.resize(I, (200, 200), interpolation = cv2.INTER_CUBIC)
vertical= np.concatenate((I_small, I_small2), axis = 0)
cv2.imshow('Bilinear vs bicubic', vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped_image = I[80:280, 150:330]
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
##########################################################################3
import cv2
import numpy as np

# Örnek: 45 derece döndürme, merkezi (200, 200) ve ölçek faktörü 1
center = (200, 200)  # Döndürme merkezi
angle = 45  # Döndürme açısı
scale = 1  # Ölçek faktörü

# Döndürme matrisi oluşturma
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Görüntüyü döndürme (örneğin, bir görüntü yükleyip)
image =cv2.imread(r'images/peppers.png', 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Döndürülmüş görüntüyü gösterme
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
######################################################################################3
import cv2
import numpy as np

image = cv2.imread('images/peppers.png')
height, width = image.shape[:2]

input_pts = np.float32([[0,0], [width-1,0], [0,height-1]])
output_pts = np.float32([[width-1,0], [0,0], [width-1,height-1]])

M = cv2.getAffineTransform(input_pts, output_pts)
print(M)
new_image = cv2.warpAffine(image, M, (width, height))

cv2.imshow('Original image', image)
cv2.imshow('new image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
###############################################################3
import cv2
import numpy as np
image = cv2.imread('images/peppers.png')
height, width = image.shape[:2]

M = np.float32([[0.5,0,0],[0,2,0]])
new_image = cv2.warpAffine(image, M, (width//2, height*2))

cv2.imshow('Original image', image)
cv2.imshow('new image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################3
import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('images/peppers.png') # Lütfen doğru dosya yolunu belirtin
import cv2
import numpy as np

# Görüntüyü yükle (Lütfen doğru dosya yolunu belirtin)
image = cv2.imread('ornek_resim.jpg')

# Görüntü boyutlarını al
height, width = image.shape[:2]

# Afin dönüşüm matrisini oluştur
M = np.float32([[0.5, 1, 0], [0.5, -2, 1]])

# Afin dönüşümü uygula
new_image = cv2.warpAffine(image, M, (width, height))  # Çıkış boyutu aynı kalıyor

# Görüntüleri göster
cv2.imshow('Ori', image)
cv2.imshow('Di', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

I_small = cv2.resize(I, (200, 200))
cv2.imshow('200x200 boyutuna getirilmis resim', I_small)
cv2.waitKey(0)
cv2.destroyAllWindows()


I_small2 = cv2.resize(I, (200, 200), interpolation = cv2.INTER_CUBIC)
vertical= np.concatenate((I_small, I_small2), axis = 0)
cv2.imshow('Bilinear vs bicubic', vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
