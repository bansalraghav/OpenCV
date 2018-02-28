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

    kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75,75)


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cv2.imshow('smooth',smooth)
    #cv2.imshow('blur',blur)
    #cv2.imshow('median',median)
    #cv2.imshow('bilateral',bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
