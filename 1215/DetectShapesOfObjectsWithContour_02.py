import cv2 as cv
import numpy as np

img_color = cv.imread ('datas/images/shapes.png')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray,127,255,0)
contours, _ = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv.contourArea(cnt)
    cv.drawContours(img_color,[cnt],0,(255,0,0),2) #blue, thickness=2

for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    print(x,y,w,h)
    epsilon = 0.02 * cv.arcLength(cnt,True) #try 0.1
    approx = cv.approxPolyDP(cnt,epsilon,True)
    print(len(approx))
    cv.drawContours(img_color,[approx],0,(0,255,255),2)

cv.imshow("result", img_color)    

cv.waitKey(0)
cv.destroyAllWindows()
