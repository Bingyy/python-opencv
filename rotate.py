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

# h,w = image.shape[:2]
# center = (w // 2, h // 2)
# M = cv2.getRotationMatrix2D(center,45,0.5) # 旋转中心，旋转角度，图片尺寸比例
# rotated = cv2.warpAffine(image,M,(w,h))

rotated = imutils.rotate(image,90)

cv2.imshow('Rotated by 45 degrees ',rotated)
cv2.waitKey(0)

