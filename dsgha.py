import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,360)

while(1):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([0,0 , 200])
    upper_blue = np.array([30, 255, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('Blue', res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
    
    