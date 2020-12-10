import cv2 as cv
import os

directoryname = os.getcwd() + '/datas/images/imageframes'
def hasdir():
    hasdir = False
    if not os.path.exists(directoryname):
        os.mkdir(directoryname)
    hasdir = os.path.exists(directoryname)
    return hasdir

files = list()
if hasdir():
    files = os.listdir(directoryname)

# Once get shape information 
filename = directoryname+"/image_0.png"
img = cv.imread(filename)
height, width, layers = img.shape
size = (width, height) #size를 height, width로 순서 바꾸면 파일 생성 안됨.
filename_output = directoryname + '/output_video.avi'
fps = 5
out_avi = cv.VideoWriter(filename_output, cv.VideoWriter_fourcc(*'DIVX'), fps, size)

# reading each files
for count in range(len(files)):
    filename = directoryname+"/image_"+str(count)+".png"
    # reading each files
    img = cv.imread(filename)
    if img is not None:
        #cv.imshow('image_'+str(count), img) # same title if you want one window.
        out_avi.write(img)    

out_avi.release()    

