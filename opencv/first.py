import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Screenshot (60).png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("screen60_gray.png",img)
