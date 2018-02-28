import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define lower and upper blue in HSV color
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    #threshold the HSV image to obtain only the blue color
    mask = cv2.inRange(hsv, lower_blue,upper_blue)

    #bitwise_AND the mask and the original image
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 4)
    dilation = cv2.dilate(mask, kernel, iterations = 4)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
