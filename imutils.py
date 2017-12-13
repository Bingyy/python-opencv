import numpy as np
import cv2

# 移动
def translate(image,x,y):
	M = np.float32([[1,0,x],[0,1,y]])
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

	return shifted

# 旋转
def rotate(image,angle,center=None,scale=1.0):
	(h,w) = image.shape[:2]
	if center is None:
		center = (w // 2, h // 2) # 默认围绕图片中心旋转
	M = cv2.getRotationMatrix2D(center,angle,scale)
	rotated = cv2.warpAffine(image,M,(w,h))

	return rotated

# resize: 参数中的宽高均为新的图片的宽高
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
	dim = None
	(h,w) = image.shape[:2] # 原图片的宽高

	if width is None and height is None: # 宽高均为默认
		return image

	if width is None:
		r = height / float(h) # ratio
		dim = (int(w * r),height)# (w,h)
	if height is None:
		r = width / float(w)
		dim = (width, int(h * r)) # (w,h)
	resized = cv2.resize(image,dim,interpolation=inter)

	return resized

	
# flipping

# cropping


