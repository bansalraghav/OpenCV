import cv2
import numpy as np

img_bgr = cv2.imread('main.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

temp = cv2.imread('template.jpg', 0)
w, h = temp.shape[::-1]

res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
threshold = 0.78
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('result',img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()


