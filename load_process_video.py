import numpy as np
import cv2

# 从输入的视频源进行捕捉
cap = cv2.VideoCapture('output.mp4')

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT); 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_gray.mp4',fourcc, 12.0,(int(w),int(h)))

while(cap.isOpened()):
    ret, frame = cap.read()
    # 变成灰度显示
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray) # not passed

    # cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()