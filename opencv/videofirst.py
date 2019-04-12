import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_screen60.avi',fourcc, 20.0, (640,480))
#for storing an image
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   this shows up the image in a window named frame
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('color',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #it waits for any key be pressed twice or once q
cap.release()
out.release()
cv2.destroyAllWindows()
