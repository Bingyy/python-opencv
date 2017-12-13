import numpy as np
import cv2
import argparse
import imutils # 自己实现的模块

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original',image)

# r = 150. / image.shape[1] # 计算比例：新图片的宽除原先的图片的宽度得到倍数
# dim = (150,int(image.shape[0] * r)) # 新的w,h
# resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) # 第三个参数指定插值类型

resized = imutils.resize(image,150) # 150是新的图片的宽度

cv2.imshow('Resized(Width)',resized)
cv2.waitKey(0)

