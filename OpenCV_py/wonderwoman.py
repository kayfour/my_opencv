import cv2 as cv

w= 870 
h= 960

img = cv.imread("./datas/images/wonderwoman.jpg")
img = cv.resize(img, (w,h))

# cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv.rectangle(img,(0,0),(250,350),(0,0,255),2)


x, y, w, h = 310, 150, 150, 160
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.putText(img," Hair  ",(300,200),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

x, y, w, h = 550, 100, 150, 160
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.putText(img," Tiara  ",(500,200),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

x, y, w, h = 690, 300, 170, 450
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.putText(img," Shield  ",(700,700),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

x, y, w, h = 280, 750, 150, 160
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.putText(img," Rope  ",(300,700),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


x, y, w, h = 310, 320, 150, 160
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.putText(img,"altong", (x-10,y-10), cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv.imshow("wonderwoman",img)
cv.waitKey(0)
