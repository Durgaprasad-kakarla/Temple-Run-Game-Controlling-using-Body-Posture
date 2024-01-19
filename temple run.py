import time

import cv2
import mediapipe as mp
import PostEstimationModule as pem
from pynput.keyboard import Key,Controller
cap=cv2.VideoCapture(0)
detector=pem.poseDetector()
keyboard=Controller()
delayCounter=0
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    detector.findPose(img,draw=False)
    lmList=detector.getPosition(img,draw=False)
    if lmList:
        p1,p2=lmList[1][1:],lmList[23][1:]
        left,right=lmList[18][1:],lmList[19][1:]
        l, _, _ = detector.findDistance(p1, p2,)
        l1, _, _ = detector.findDistance(left, right)
        print(p1[1],l1)
        if left[0]<200 and right[0]>500:
            keyboard.press(Key.space)
        if l1<80:
            if delayCounter==0:
                keyboard.press(Key.up)
                keyboard.release(Key.up)
        if left[0]<200:
               keyboard.press(Key.left)
        if right[0]>500:
            keyboard.press(Key.right)
        if l<250:
            keyboard.press(Key.down)
        else:
            keyboard.release(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.space)
            keyboard.release(Key.down)
        # print(lmList)
        delayCounter+=1
    if delayCounter==10:
        delayCounter=0
    cv2.imshow("Temple Run",img)
    cv2.waitKey(1)