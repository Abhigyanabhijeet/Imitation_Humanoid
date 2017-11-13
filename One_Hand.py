import cv2
import numpy as np
import math
import serial
import sys
import time


#ssc32 = serial.Serial('COM9', 115200, timeout=1)
time.sleep(2)
palm = cv2.CascadeClassifier('palm.xml')
fist = cv2.CascadeClassifier('fist.xml')
up_cascade = cv2.CascadeClassifier('haarcascade_mcs_upperbody.xml')
##face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

lk_params = dict( winSize  = (15,15),maxLevel = 2,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

cap=cv2.VideoCapture(1)   

def arduino_map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def initialize():
    y=0
    h=0
    pcx=0
    pcy=0
    fcx=0
    fcy=0
    rsx=0
    lsx=0
    sy=0
    ebx=0
    eby=0
    nfx=0
    nfy=0
    nx=0
    ny=0
    oebx=0
    oeby=0
    refx=0
    refy=0
    
while(1):
    
    initialize()
    ret, old_frame = cap.read()
    img=old_frame
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)


    up =up_cascade.detectMultiScale(old_gray ,1.3,5)
    for (x,y,w,h) in up:
        lsx=x+w//6
        sy=y+3*h//4
        refx=lsx
        refy=y+3*h//2
        cv2.circle(img,(lsx,sy), 3, (0,0,255), -1)
        cv2.circle(img,(rsx,sy), 3, (0,0,255), -1)

    mask = np.zeros_like(old_frame)

    
    
    fistnew =fist.detectMultiScale(old_gray ,1.3,5)
    for (x,y,w,h) in fistnew:
        cv2.rectangle(img ,(x,y),(x+w,y+h),(255,0,0),2)
        fcx= x+w//2
        fcy= y+h//2
        oebx =fcx
        oeby =y+7*h//2
          

    p0 = np.array([[[fcx,fcy]],[[lsx,sy]],[[oebx,oeby]],[[refx,refy]]], np.float32)    

    if(p0[0][0][0]!=0 and lsx!=0 and oebx!=0 and refx!=0) :
               while(1):
                ret,frame = cap.read()
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
                p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
                px=p1[0][0][0]
                py=p1[0][0][1]
                ex=p1[2][0][0]
                ey=p1[2][0][1]
                sx=p1[1][0][0]
                sy=p1[1][0][1]
                fx=p1[3][0][0]
                fy=p1[3][0][1]
                
                cv2.line(frame,(px,py),(ex,ey),(120,110,225),5)
                cv2.line(frame,(sx,sy),(ex,ey),(120,110,225),5)
                cv2.line(frame,(sx,sy),(fx,fy),(120,110,225),5)
                cv2.line(frame,(px,py),(ex,ey),(120,110,225),5)


                b=math.sqrt(math.pow((px - ex),2) + math.pow((py - ey),2))
                a=math.sqrt(math.pow((px - sx),2) + math.pow((py - sy),2))
                c=math.sqrt(math.pow((ex - sx),2) + math.pow((ey - sy),2))
                b1=math.sqrt(math.pow((ex - sx),2) + math.pow((ey - sy),2))
                a1=math.sqrt(math.pow((fx - sx),2) + math.pow((fy - sy),2))
                c1=math.sqrt(math.pow((ex - fx),2) + math.pow((ey - fy),2))

                angle = int(math.acos((math.pow(b,2)+math.pow(c,2)-math.pow(a,2))/(2*b*c))*180/math.pi)
                angle2 = int(math.acos((math.pow(b1,2)+math.pow(a1,2)-math.pow(c1,2))/(2*a1*b1))*180/math.pi)

                  
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,str(angle),(ex,ey), font, 1,(255,255,255),2,cv2.LINE_AA)
                cv2.putText(frame,str(angle2),(sx,sy), font, 1,(255,255,255),2,cv2.LINE_AA)



        # Select good points
                good_new = p1[st==1]
                good_old = p0[st==1]
    
        # draw the tracks
        
                for i,(new,old) in enumerate(zip(good_new,good_old)):
                    a,b = new.ravel()
                    c,d = old.ravel()

                    frame = cv2.circle(frame,(a,b),5,(0,0,255),-1)

                img = cv2.add(frame,mask)
    
                cv2.imshow('frame',img)
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break

                
        
        # Now update the previous frame and previous points
                old_gray = frame_gray.copy()
                p0 = good_new.reshape(-1,1,2)
    p0[0][0][0]=0   
      
    
     
           
    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break    
        

cap.release()
cv2.destroyAllWindows()




