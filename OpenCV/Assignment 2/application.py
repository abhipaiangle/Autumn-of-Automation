import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("img2.png")

img_1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask_white = cv2.inRange(img,(180, 180, 180) , (255, 255, 255))
img_3 = cv2.bitwise_and(img, img, mask=mask_white)

img_4 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_5 = cv2.GaussianBlur(img,(5,5),3)

img_6 = cv2.GaussianBlur(img_4,(5,5),3)

rows,cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
L = cv2.getRotationMatrix2D((cols/2,rows/2),100,1)
P = cv2.getRotationMatrix2D((cols/2,rows/2),150,1)
O = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)

img_7 = cv2.warpAffine(img_1,O,(cols,rows),1)

img_8 = cv2.warpAffine(img,M,(cols,rows),1)

img_9 = cv2.warpAffine(img,L,(cols,rows),1)

img_10 = cv2.warpAffine(img_6,P,(cols,rows),1) 

a = [img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10]

for i in range(len(a)):
    name = "img_"+ f"{i}" +".png"
    cv2.imwrite(name,a[i])

cv2.imshow("Images",img_8)

cv2.waitKey(0) 



