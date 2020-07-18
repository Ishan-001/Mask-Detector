import numpy as np
import cv2

img=cv2.imread('image.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('Output', cv2.WINDOW_NORMAL)

cv2.rectangle(img, (900,600), (1200,1500), (0,0,255), 15)

cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()