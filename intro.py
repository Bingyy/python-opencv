import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('dog.png',0) # grayscale

# show image with plt
# plt.imshow(img, cmap='gray',interpolation='bicubic')
# # draw a line
# plt.plot([50,100],[80,100],'c',linewidth=5)
# plt.show()

# show image with cv2
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('dog.jpg',img)