import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')

args = vars(ap.parse_args())

# 显示原本的图片
image = cv2.imread(args['image']) # 读进来返回的是一个Numpy对象
cv2.imshow('origin',image)

cropped = image[30:150,240:360]
cv2.imshow('cropped', cropped)

cv2.waitKey(0)