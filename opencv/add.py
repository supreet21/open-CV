import numpy as np
import cv2

img1 = cv2.imread('Screenshot (60).png',cv2.IMREAD_COLOR)
img2 = cv2.imread('Screenshot (46).png',cv2.IMREAD_COLOR)

#add = img1+img2
#add  = cv2.add(img1,img2)
weighted = cv2.addWeighted(img1,0.2, img2,0.8,0)
cv2.imshow('add',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
