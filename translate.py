'''
这部分是图像处理环节的练习
1. basic image transformations
	- translation
	- rotation
	- resizing
	- flipping
	- cropping
	
	以及：
	- image arithmetic
	- bitwise operations
	- masking
	
	最后：

	- split an image into respective channels
	- merge channels back together

'''

import numpy as np
import cv2
import argparse
import imutils # 自己实现的模块

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')

args = vars(ap.parse_args())

#---以上是从命令行读取文件路径的标准方法---
image = cv2.imread(args['image'])

cv2.imshow('Original',image)
 
# 通过矩阵的方式旋转
# [1,0,t_x] : 向左或者向右，左负右正
# [0,1,t_y] : 向上或者向下，上负下正
# M = np.float32([[1,0,25],[0,1,50]]) # 2x3矩阵
# shifted = cv2.warpAffine(image,M,(image.shape[0],image.shape[1]))
shifted = imutils.translate(image,25,50)
cv2.imshow('Shifted down and right', shifted)

# M = np.float32([[1,0,-50],[0,1,-90]])
# shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
shifted = imutils.translate(image,-50,-90)
cv2.imshow('Shifted up and Left',shifted)



# cv2.imshow('canvas',canvas)
cv2.waitKey(0)



