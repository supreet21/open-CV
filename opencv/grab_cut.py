import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pandey.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgModel = np.zeros((1,65) , np.float64) #np.zeros keeps the tupple with the given range and others zero
fgModel = np.zeros((1,65) , np.float64)

rect = (50, 0 , 150, 250) #size of the area of image in foreground

cv2.grabCut(img, mask , rect, bgModel , fgModel , 5 ,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask == 0), 0 ,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
