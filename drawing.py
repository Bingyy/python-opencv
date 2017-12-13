import numpy as np
import cv2

canvas = np.zeros((300,300,3),dtype = 'uint8')

green = (0,255,0) # BGR
cv2.line(canvas,(0,0),(300,300),green)
# cv2.imshow('canvas',canvas)

red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3) # 最后一个参数表示线条粗细

# rectangle
cv2.rectangle(canvas,(200,50),(225,125),red,-1)
# circle
centerX,centerY = canvas.shape[1] // 2, canvas.shape[0] // 2
white = (255,255,255)
# for i in range(0,175,25):
# 	cv2.waitKey(200)
# 	cv2.circle(canvas,(centerX,centerY),i, white)

# 动画并未出现 -- 
# r = 1
# while(True):
# 	cv2.circle(canvas,(centerX,centerY),r, white)
# 	cv2.waitKey(30)
# 	r = r + 25

for i in range(0,25):
	radius = np.random.randint(5,high=200) # [5,200)
	color = np.random.randint(0,high=256,size=(3,)).tolist() # 三维
	pt = np.random.randint(0,high=300,size=(2,)) # point, 二维
	cv2.circle(canvas,tuple(pt),radius,color,-1)


cv2.imshow('canvas',canvas)
cv2.waitKey(0)






