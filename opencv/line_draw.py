import numpy as np
import cv2

img  = cv2.imread('Screenshot (60).png',cv2.IMREAD_COLOR)

cv2.line(img, (0,0) ,(150,150),(255,245,55),15)
cv2.rectangle(img, (300,200),(500,400),(0,255,0),5)
cv2.circle(img, (200,74),66,(0,0,255),-1)

pts = np.array([[10,15],[20,15],[30,28],[44,10],[12,12]], np.int32)
cv2.polylines(img, [pts], True, (255,0,255),4)

font = cv2.FONT_HERSHEY_SIMPLEX
#Hershey Script Complex
cv2.putText(img, 'Opencv tuts!', (0,250),font,1,(200,20,250),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
