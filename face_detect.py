import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier('face_detection_cascade.xml')

video=cv2.VideoCapture(0)

while True:
    ret,img=video.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Face Detector',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()