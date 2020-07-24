import cv2

img = cv2.imread("img.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_img.jpg",gray)

cv2.imshow("Display",gray)
cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()
