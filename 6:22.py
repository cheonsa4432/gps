import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,360)

while(1):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([150, 50, 50])
    upper_blue = np.array([180, 255, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('Blue', res)
    
    img_color = res
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    contours_xy = np.array(contours)
    contours_xy.shape
    
    for cnt in contours:
        cv2.drawContours(img_color, [cnt], 0, (0, 255, 0), 3)  # blue

        cv2.imshow("result", img_color)

        


    for cnt in contours:

        hull = cv2.convexHull(cnt)
        cv2.drawContours(img_color, [hull], 0, (255, 0, 255), 5)
        # x의 min과 max 찾기
        x_min, x_max = 0,0
        value = list()
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                value.append(contours_xy[i][j][0][0]) #네번째 괄호가 0일때 x의 값
                x_min = min(value)
                x_max = max(value)
        print(x_min)
        print(x_max)
 
# y의 min과 max 찾기
        y_min, y_max = 0,0
        value = list()
        for i in range(len(contours_xy)):
            for j in range(len(contours_xy[i])):
                value.append(contours_xy[i][j][0][1]) #네번째 괄호가 0일때 x의 값
                y_min = min(value)
                y_max = max(value)
        print(y_min)
        print(y_max)

        


    cv2.imshow("result", img_color)
    
    
   
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()