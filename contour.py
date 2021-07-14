import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    img2 = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    
    lower_blue = np.array([150, 50, 50])
    upper_blue = np.array([180, 255, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    

    contours, heiarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, 
                                         cv2.CHAIN_APPROX_SIMPLE)
    cntr = contours[0]
    cv2.drawContours(frame, [cntr], -1, (0, 255,0), 1)

    print(cv2.isContourConvex(cntr), cv2.isContourConvex(hull))

    hull2 = cv2.convexHull(cntr, returnPoints=False)
    # 볼록 선체 결함 찾기 ---⑥
    defects = cv2.convexityDefects(cntr, hull2)
    # 볼록 선체 결함 순회
    for i in range(defects.shape[0]):
    # 시작, 종료, 가장 먼 지점, 거리 ---⑦
        startP, endP, farthestP, distance = defects[i, 0]
    # 가장 먼 지점의 좌표 구하기 ---⑧
        farthest = tuple(cntr[farthestP][0])
    # 거리를 부동 소수점으로 변환 ---⑨
        dist = distance/256.0
    # 거리가 1보다 큰 경우 ---⑩
        if dist > 1 :
        # 빨강색 점 표시 
            cv2.circle(img2, farthest, 3, (0,0,255), -1)
# 결과 이미지 표시
    cv2.imshow('frame', frame)
    cv2.imshow('Blue', res)
    cv2.imshow('contour', frame)
    cv2.imshow('convex hull', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()