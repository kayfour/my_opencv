import cv2 as cv
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(
                        imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(
                        imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(
                        imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        # hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(
                    imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(
                    imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver




img = cv.imread('datas/images/kub.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgYuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
imgXyz = cv.cvtColor(img, cv.COLOR_BGR2XYZ)
imgHls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
print(img.shape)
imgResize = cv.resize(img,(135,203))
imgHor = np.hstack((img,img,img))
cv.imshow("Horizontal",imgHor)

imgVer = np.vstack((imgResize,imgResize,imgResize,imgResize,imgResize))
cv.imshow("Vertical",imgVer)

imgStack = stackImages(0.5, ([imgYuv, imgGray, imgHsv], [img, imgXyz, imgHls]))
cv.imshow("ImageStack", imgStack)

cv.waitKey(0)
cv.destroyAllWindows()
