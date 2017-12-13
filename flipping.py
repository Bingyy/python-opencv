import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('origin',image)

flipped = cv2.flip(image,1) # 第二个参数为1表示水平翻转
cv2.imshow('Flipped Horizontally', flipped) 

flipped = cv2.flip(image,0) # 第二个参数为0表示垂直翻转
cv2.imshow('Flipped Vertically', flipped) 

flipped = cv2.flip(image,-1) # 第二个参数为-1表示水平&垂直翻转
cv2.imshow('Flipped Horizontally & Vertically ', flipped) 

cv2.waitKey(0)