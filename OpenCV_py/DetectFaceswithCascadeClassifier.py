import cv2 as cv

cascadefile = "datas/haar_cascade_files/haarcascade_frontalface_default.xml"
cascade_f = cv.CascadeClassifier(cascadefile)
cascadefile = "datas/haar_cascade_files/haarcascade_eye.xml"
cascade_e = cv.CascadeClassifier(cascadefile)
cascadefile = "datas/haar_cascade_files/haarcascade_mcs_nose.xml"
cascade_n = cv.CascadeClassifier(cascadefile)

#filepath = 'datas/images/kub.jpg'    # sigle human
#filepath = 'datas/images/faces1.jpg'      # few human -> one missing
filepath = 'datas/images/twice4.jpg'    # a lot human -> can't detect little bit
img = cv.imread(filepath)
# faces = cascade.detectMultiScale(img, 1.1, 4)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = cascade_f.detectMultiScale(imgGray, 1.1, 4)
n=1
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    n+=1    
print ("Detected faces :",n)
cv.imshow("Result", img)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
eyes = cascade_e.detectMultiScale(imgGray, 1.1, 4)
n=1
for (x, y, w, h) in eyes:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    n+=1    
print ("Detected eyes :",n)
cv.imshow("Result", img)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
noses = cascade_n.detectMultiScale(imgGray, 1.1, 4)
n=1
for (x, y, w, h) in noses:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    n+=1    
print ("Detected noses :",n)




cv.imshow("Result", img)




cv.waitKey(0)
cv.destroyAllWindows()
