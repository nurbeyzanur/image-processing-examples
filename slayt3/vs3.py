###############################################
## GÖRÜNTÜDEKİ PİXEL DEĞERLERİNE ERİŞİM
import cv2
import matplotlib.pyplot as plt
import numpy as np
from astropy.utils.metadata.utils import dtype
from colorcet import m_rainbow_r

I=cv2.imread(r"images/peppers.png",1)
print(I.shape)
# bgr daki tüm renklerin kodu
px=I[50,50]
print(px)

# sadece kırmızı olan renge erişim için
px_r=I[50,50,2]
print(px_r)

########################################################
# bgr olan resmi rgb haliine çevirmek
I=cv2.imread(r"images/peppers.png",1)
m_new=np.zeros((384,512,3),dtype=np.uint8)
o_b=I[:,:,0]
o_g=I[:,:,1]
o_r=I[:,:,2]
m_new[:,:,0]=o_r
m_new[:,:,1]=o_g
m_new[:,:,2]=o_b
cv2.imshow("eski hali",I)
cv2.imshow("resmi rgb hale cevirmek",m_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(m_new)
plt.show()


