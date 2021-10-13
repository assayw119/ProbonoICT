import cv2
import numpy as np

cap = cv2.VideoCapture('videos/train_video.mp4')

count = 0

while(cap.isOpened()):
    ret, image = cap.read()

    if(int(cap.get(1)) % 2 == 0):
        print('saved frame number : ' + str(int(cap.get(1))))

        cv2.imwrite('imgs/img%d.jpg' % count, image)

        print('saved frame%d.jpg' % count)
        
        count += 1
    
cap.release()