import numpy as np
from PIL import ImageGrab
import cv2
#import winsound

while(True):
    screen1 =  np.array(ImageGrab.grab(bbox=(0,40,500,400)))
    screen2 =  np.array(ImageGrab.grab(bbox=(0,40,500,400)))
    diff = cv2.absdiff(screen1,screen2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dialated = cv2.dilate(thresh,None,iterations=3)
    contours,_ = cv2.findContours(dialated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(screen1,contours,-1,(0,255,0),2)
    for c in contours:
    	if cv2.contourArea(c) < 5000:
    		continue
    	x,y,w,h = cv2.boundingRect(c)
    	cv2.rectangle(screen1,(x,y),(x+w,y+h),(0,255,0),2)
    	#winsound.Beep(500,200)
    cv2.imshow('Screen',screen1)    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

