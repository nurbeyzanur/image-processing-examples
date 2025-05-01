################################################################################################################
#                                   ÇİZGİ     ÇİZME
import cv2
import matplotlib.pyplot as plt

I=cv2.imread(r"images/cicek.jpg",1)
imagecopy=I.copy()
pointA=(200,80)
pointB=(400,80)
cv2.line(imagecopy,pointA,pointB,(0,0,255),1)
cv2.imshow('cizgi cicek',imagecopy)
cv2.imshow("orijinal cicek",I)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(I.shape)
################################################################################################################
#                                   ÇEMBER    ÇİZME
center=(200,300)
cv2.circle(imagecopy,center,100,(0,0,255),-1,lineType=cv2.LINE_AA)
cv2.imshow('cember  cicek',imagecopy)
cv2.imshow("orijinal cicek",I)
cv2.waitKey(0)
cv2.destroyAllWindows()
################################################################################################################
#                                   DAİRE    ÇİZME
cv2.circle(imagecopy,center,100,(0,0,255),-1,lineType=cv2.LINE_AA)
cv2.imshow('cember  cicek',imagecopy)
cv2.imshow("orijinal cicek",I)
cv2.waitKey(0)
cv2.destroyAllWindows()
################################################################################################################
#                                  KARE   ÇİZME
pointB=(400,160)
cv2.rectangle(imagecopy,pointA,pointB,(0,0,255),-1,)
cv2.imshow('kare cicek',imagecopy)
cv2.imshow("orijinal cicek",I)
cv2.waitKey(0)
cv2.destroyAllWindows()
################################################################################################################
#                                  ELİPS  ÇİZME
center=(200,300)
cv2.ellipse(imagecopy, center, (100, 40), 70, 0, 90, (0, 0, 255), 3)
cv2.imshow('elips cicek',imagecopy)
cv2.imshow("orijinal cicek",I)
cv2.waitKey(0)
cv2.destroyAllWindows()


###################################################################################################
import cv2

I = cv2.imread(r'images/peppers.png', 1)


imagecopy = I.copy()
print(I.shape)

# Görüntü boyutları
height, width, _ = I.shape

# Dikey çizgiler
pointA = (width // 3, 0)
pointA_1 = (width // 3, height)
line1 = cv2.line(imagecopy, pointA, pointA_1, (255, 255, 255), 3)

pointA = (2 * width // 3, 0)
pointA_1 = (2 * width // 3, height)
x = cv2.line(line1, pointA, pointA_1, (255, 255, 255), 3)

# Yatay çizgiler
pointB = (0, height // 3)
pointB_2 = (width, height // 3)
line_2 = cv2.line(x, pointB, pointB_2, (255, 255, 255), 3)

pointB = (0, 2 * height // 3)
pointB_2 = (width, 2 * height // 3)
resim = cv2.line(line_2, pointB, pointB_2, (255, 255, 255), 3)

cv2.imshow("Orijinal Cicek", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

def draw_grid(image_path, grid_size=(3, 3), color=(255, 255, 255), thickness=3):
    # Görüntüyü yükle
    image = cv2.imread(image_path)
    if image is None:
        print("Görüntü yüklenemedi.")
        return

    # Görüntü boyutlarını al
    height, width, _ = image.shape

    # Izgara çizgilerini çiz
    for i in range(1, grid_size[1]):
        x = int(i * width / grid_size[1])
        cv2.line(image, (x, 0), (x, height), color, thickness)

    for i in range(1, grid_size[0]):
        y = int(i * height / grid_size[0])
        cv2.line(image, (0, y), (width, y), color, thickness)

    # Görüntüyü göster
    cv2.imshow('Orijinal Cicek', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

draw_grid(r'images/peppers.png')