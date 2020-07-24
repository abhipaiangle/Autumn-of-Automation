import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img.jpg',0)
edges = cv2.Canny(img,100,200)
edges = cv2.bitwise_not(edges)
plt.imshow(edges,cmap = 'gray')
plt.xticks([]),plt.yticks([])
plt.show()

cv2.imwrite("edges.png",edges)