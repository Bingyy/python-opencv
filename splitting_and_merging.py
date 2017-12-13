import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')
args = vars(ap.parse_args())

# 显示原本的图片
image = cv2.imread(args['image']) # 读进来返回的是一个Numpy对象
cv2.imshow('origin',image)

# 拆分
B,G,R = cv2.split(image)

# 显示的是灰度图
cv2.imshow('Red',R)
cv2.imshow('Green',G)
cv2.imshow('Blue',B)


# 显示该通道但是彩色图
zeros = np.zeros(image.shape[:2],dtype='uint8') # 二维
cv2.imshow('Red_Color', cv2.merge([zeros,zeros,R]))
cv2.imshow('Green_Color', cv2.merge([zeros,G,zeros]))
cv2.imshow('Blue_Color', cv2.merge([B,zeros,zeros]))

# 组合
merged = cv2.merge([B,G,R])
cv2.imshow('Merged',merged)

cv2.waitKey(0)
cv2.destroyAllWindows() # 按q键退出