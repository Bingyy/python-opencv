import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')
args = vars(ap.parse_args())

# 显示原本的图片
image = cv2.imread(args['image']) # 读进来返回的是一个Numpy对象
cv2.imshow('origin',image)

# 转为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow('GRAY', gray)

# 转为HSV图
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)

# 转为LAB图
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB',lab)

cv2.waitKey(0)
cv2.destroyAllWindows()