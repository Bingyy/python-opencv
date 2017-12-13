from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument('-i','--image',required=True,help='Path to the image')

args = vars(ap.parse_args())

img = cv2.imread(args['image'])

print('Width: {} pixels'.format(img.shape[1]))
print('Height: {} pixels'.format(img.shape[0]))
print('Channels: {} pixels'.format(img.shape[2]))

cv2.imshow('Image',img)
cv2.waitKey(0)