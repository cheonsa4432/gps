import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,360)


while True :
    ret, frame = cap.read()

    mask1=cv2.inRange(hsv_frame, low_red, hight_red)

    low_red=np.array([150,120,70])
    high_red=np.array([180,255, 255])
    mask2=cv2.inRange(hsv_frame, low_red, high_red)


    red_mask = mask1+mask2
    red=cvv2.bitwise_and(hsv_frame, hsv_frame, mask=red_mask)
    cv2.imshow("Red", red)


    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_binary = cv2.threshold(frame_gray, 90, 225, 0)
    #언더바는 받긴 받는데 사용하지 않는 것을 의미
    
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    maxArea = [0, 0]
    for cut in contours :
        # cv2.drawContours(frame, [cnt], 0, (255, 0, 0), 3)   #blue

        size = cv2.contourArea(cnt)
        
        if size > MaxArea [0] :
            maxArea[0] = size
            maxArea[1] = cnt

    if maxArea[0]!=0 :
        cv2.drawContours(frame, [maxarea[1]], 0, (255, 255, 0), 3)  #blue

    print("area", maxArea[0])
    cv2.imshow("binary", img_binary)
    cv2.imshow("VideoFrame", frame)
    
    if cv2.waitKey(1) > 0 : break

cap.release()
cv2.destroyAllwindows()