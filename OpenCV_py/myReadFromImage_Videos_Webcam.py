import cv2 as cv


######################## READ IMAGE ############################
def R_image():
    img = cv.imread("./datas/images/lena.png")
    cv.imshow("READ",img)
    cv.waitKey(0)

######################### READ VIDEO #############################
def R_video():
    frameWidth = 640
    frameHeight = 480
    cap = cv.VideoCapture("datas/videos/Armbot.mp4")
    while True:
        success, img = cap.read()
        img = cv.resize(img, (frameWidth, frameHeight))
        # frameWidth = frameWidth + 20
        # frameHeight = frameHeight + 20
        cv.imshow("READ", img)
        
        if cv.waitKey(20) == ord('q'):   
            cap.release()
            cv.destroyAllWindows()  
        elif cv.waitKey(20) == ord('i'):
            R_image()
        elif cv.waitKey(20) == ord('w'):
            break       
    cap = cv.VideoCapture(0)

######################### READ WEBCAM  ############################
def R_webcam():
    frameWidth = 640
    frameHeight = 480
    cap = cv.VideoCapture(0)

    cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
    cap.set(cv.CAP_PROP_BRIGHTNESS,150)
    while cap.isOpened():
        success, img = cap.read()
        cv.imshow("READ", img)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    cap = cv.VideoCapture(0)
    

cap = cv.VideoCapture(0)

try:
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv.imshow('READ', frame)
        if cv.waitKey(1) == 27 or cv.waitKey(30) == ord('q'):
            break
        elif cv.waitKey(30) == ord('i'):
            R_image()
        elif cv.waitKey(30) == ord('v'):
            R_video()
        elif cv.waitKey(30) == ord('w'):
            R_webcam()        

except :
    pass
finally:
    cap.release()
    cv.destroyAllWindows()  