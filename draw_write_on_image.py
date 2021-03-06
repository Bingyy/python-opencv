import numpy as np
import cv2

img = cv2.imread('dog.png',1) # color

# 在图像上绘图
cv2.line(img,(0,0),(150,150),(255,0,0),15)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1) # -1表示fill in

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# pts = pts.reshape(-1,1,2)
cv2.polylines(img,[pts],True, (0,255,255),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

