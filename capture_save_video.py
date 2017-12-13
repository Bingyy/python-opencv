import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT); 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_flipped.mp4',fourcc, 12.0,(int(w),int(h)))


while True:
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # 每帧转为灰度图，
	
	if ret == True:
		frame = cv2.flip(frame,0) # 翻转帧后存储
		out.write(frame)

		cv2.imshow('frame',frame)
		cv2.imshow('gray',gray)

	if cv2.waitKey(1) & 0xFF == ord('q'): # & 0xFF是针对64位机器
		break

cap.release() # 释放摄像头
out.release()
cv2.destroyAllWindows()


