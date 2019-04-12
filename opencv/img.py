import cv2
img = cv2.imread('Screenshot (60).png')
cv2.imshow("image",img)
img1 = cv2.imread('Screenshot (60).png',0)
cv2.imshow("imagegray",img1)
cv2.waitkey(0)
