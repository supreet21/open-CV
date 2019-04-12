import numpy as np
import cv2

img = cv2.imread('sou2.jpg', cv2.IMREAD_COLOR)

face = img[300:640,390:720]
img[0:340,0:330]=face

img[330:440,500:740]=[0,0,0]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
