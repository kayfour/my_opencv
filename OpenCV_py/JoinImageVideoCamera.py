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

cap = cv.VideoCapture(0)
cap1= cv.VideoCapture("datas/videos/[Ohys-Raws] Dungeon ni Deai o Motomeru no wa Machigatte Iru Darouka Familia Myth III - 10 (BS11 1280x720 x264 AAC).mp4")

try:
    while cap.isOpened() & cap1.isOpened():
       
        ret, frame = cap.read()
        success, video = cap1.read()
        img = cv.imread('datas/images/kub.jpg')
        imgStack = stackImages(0.7, ([frame, img, video],[img, video, frame],[video,frame,img]))
        cv.imshow("ImageStack", imgStack)       
        if cv.waitKey(1) == 27:
            break
except :
    pass
finally:
        # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

print('End....')
