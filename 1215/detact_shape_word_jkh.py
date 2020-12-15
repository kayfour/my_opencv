import cv2 as cv, numpy as np
import matplotlib.pyplot as plt
import os,time
import pytesseract
from pytesseract import Output

def get_name(img,x,y,len):
    if len == 3:
        cv.putText(img,"Triangle",(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    elif len == 4 :
        cv.putText(img,"rectangle",(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    else :
        cv.putText(img,"circle",(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    
def nothing():
    pass


def get_word(img,approx,w,h):

    hei,wid,_ = img.shape 
    if approx[0][0][0] > approx[2][0][0]:
        pts1 =np.float32((approx[3][0],approx[0][0],approx[2][0],approx[1][0]))   # PTS 1에 이미지에서 틀어짐 부분을 보정하기 위한 단계.
    else :
        pts1 =np.float32((approx[0][0],approx[1][0],approx[3][0],approx[2][0]))

    pts2 =np.float32([[0,0],[wid,0],[0,hei],[wid,hei]])                 # 변환하고 싶은 이미지사이즈 결정
    matrix = cv.getPerspectiveTransform(pts1,pts2)                      # 각 4개 포인트에 대한 원근각을 계산

   
    imgOut = cv.warpPerspective(img,matrix,(wid,hei))                   # 소스 이미지로부터 얻은 원근각 매트릭스를 비교하여 회전된 이미지로 생성
    
    # pytessract 로 영문 인식 
    custom_config = r'--oem 3 --psm 6 -l eng'
    word_strings = pytesseract.image_to_string(imgOut)
    words = pytesseract.image_to_data(imgOut,config=custom_config,output_type=Output.DICT)

    print(words['text'])
    n_boxes = len(words['text'])
    for i in range(n_boxes):
        if int(words['conf'][i])>60:
            (x,y,w,h) = (words['left'][i],words['top'][i],words['width'][i],words['height'][i])
            imgOut = cv.rectangle(imgOut,(x,y),(x+w,y+h),(0,255,0),3)
    
    return imgOut
 

if __name__ == "__main__":

    plt.figure()
    dir = os.getcwd()+"/datas/images/namecard_01.jpg"
    img_color = cv.imread(dir)
    img = cv.cvtColor(img_color,cv.COLOR_BGR2GRAY)
    _,img = cv.threshold(img,100,255,cv.THRESH_OTSU) #Threshold 를 통해 윤곽선을 얻기 쉬운상태로 변환 
    img = cv.bitwise_not(img)   # 흰색 사각형은 전부 255로 채워져있어 이를 masking 하면 내부가 채워지며 내부 도형이 지워짐
                                #  invert 를 해서 바탕을 0으로 하여 이를 방지 
    hei,wid = img.shape 

    plt.imshow(img);plt.show(); cv.waitKey(0)
    contour,_ = cv.findContours(img,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) # 윤곽선을 찾음
    for cnt in contour :
        x,y,w,h = cv.boundingRect(cnt)
        epsilon = 0.005 * cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,epsilon,True) 
        if(len(approx)==4 and w>200 and y>200):
            print(x,y,w,h)            
            cv.drawContours(img_color,[approx],0,(0,0,255),2)
            # set_value(approx,w,h)
            print(approx)
            imgOut = get_word(img_color,approx,w,h)
            plt.subplot(1,2,2)
            plt.imshow(imgOut)


    plt.subplot(1,2,1)
    plt.imshow(img_color)
    plt.show()
    cv.waitKey(0)