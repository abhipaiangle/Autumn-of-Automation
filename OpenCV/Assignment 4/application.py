import cv2

img = cv2.imread("img.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img, contours, -1, (0,255,0), 1)
for i in (range(len(contours))):
    cnt = contours[i]
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    img = cv2.circle(img, (cx,cy), radius=0, color=(255, 0, 0), thickness=2)

cv2.imwrite("Contours.png",img)
cv2.imshow("Display",img)
cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()
