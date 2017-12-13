import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')
args = vars(ap.parse_args())


# 显示原本的图片
image = cv2.imread(args['image']) # 读进来返回的是一个Numpy对象
cv2.imshow('origin',image)

M = np.ones(image.shape, dtype='uint8') * 100
added = cv2.add(image,M) # 调用cv2.add， 大于255时就定格在255，小于0时定格在0
cv2.imshow('Added', added)

M = np.ones(image.shape, dtype='uint8') * 50
sub = cv2.subtract(image, M)
cv2.imshow('Subtract', sub)


cv2.waitKey(0)