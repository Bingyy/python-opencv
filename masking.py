import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')
args = vars(ap.parse_args())


# 显示原本的图片
image = cv2.imread(args['image']) # 读进来返回的是一个Numpy对象
cv2.imshow('origin',image)

mask = np.zeros(image.shape[:2],dtype='uint8')
cX,cY = image.shape[1] // 2, image.shape[0] // 2
cv2.circle(mask, (cX,cY),100, 255,-1) # white circle

masked = cv2.bitwise_and(image,image,mask=mask)
# masked = cv2.bitwise_and(image,mask) # wrong

cv2.imshow('mask',masked)

cv2.waitKey(0)