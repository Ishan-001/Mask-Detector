import numpy as np
import cv2

video=cv2.VideoCapture(0)
capture=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi', capture, 20.0, (640,480))

while(True):
    ret,frame=video.read()
    out.write(frame)
    cv2.imshow('Output', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()