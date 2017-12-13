'''
bitwise操作共有四种：
- AND : is true only if both pixels are greater than 0
- OR : is true if either of two pixels are greater than 0
- XOR : is true if and only if one pixel > 0 and the other = 0
- NOT : inverts the 'on' and 'off' pixel in an image
这四个操作对于image processing来说是至关重要的

a given pixel is on : if it has a value  > 0
off: if it has a value = 0

'''

import numpy as np
import cv2

rectCanvas = np.zeros((300,300),dtype='uint8') # 300x300 black
cv2.rectangle(rectCanvas,(25,25),(275,275),255,-1) # fill in white 
# cv2.imshow('Rect', rectCanvas)

circleCanvas = np.zeros((300,300),dtype='uint8')
cv2.circle(circleCanvas,(150,150),150,255,-1)
# cv2.imshow('Circle',circleCanvas)

bitwiseAnd = cv2.bitwise_and(rectCanvas,circleCanvas)
cv2.imshow('AND',bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectCanvas,circleCanvas)
cv2.imshow('OR',bitwiseOr)

bitwiseXOR = cv2.bitwise_xor(rectCanvas,circleCanvas)
cv2.imshow('XOR',bitwiseXOR)

bitwiseNOT = cv2.bitwise_not(rectCanvas,circleCanvas)
cv2.imshow('NOT',bitwiseNOT)

cv2.waitKey(0)