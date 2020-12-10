import cv2 as cv
import numpy as np

img = cv.imread("datas/images/marvel1.png")
print(img.shape)

imgResize = cv.resize(img,(2384,1340))
print(imgResize.shape)
#cv.imshow("Image Resize",imgResize)

imgCropped = img[75:155, 500:580] #세로시작점: 세로끝점, 가로시작점:가로끝점

cv.imshow("Image",img)
cv.imshow("Hulk",imgCropped)

imgCropped = img[210:280, 560:610]
cv.imshow("Ironman",imgCropped)


cv.waitKey(0)
cv.destroyAllWindows()