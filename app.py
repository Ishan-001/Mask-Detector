import cv2
from matplotlib import pyplot as plt
import numpy as np

#load image
img=cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

#save image
#cv2.imwrite('gray.png', img)

#configure window
cv2.namedWindow('Output', cv2.WINDOW_NORMAL)

#Output
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()