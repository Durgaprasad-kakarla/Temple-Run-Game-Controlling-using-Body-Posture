import time

import cv2
import mediapipe as mp
import PostEstimationModule as pem
from pynput.keyboard import Key,Controller
cap=cv2.VideoCapture(0)
detector=pem.poseDetector()
keyboard=Controller()
# delayCounter=0
counter=0
while True:
    success,img=cap.read()
    img=cv2.resize(img,(750,550))
    img=cv2.flip(img,1)
    detector.findPose(img,draw=False)
    lmList=detector.getPosition(img,draw=False)
    if lmList:
        p1,p2=lmList[1][1:],lmList[23][1:]
        left,right=lmList[18][1:],lmList[19][1:]
        l, _, _ = detector.findDistance(p1, p2)
        l1, _, _ = detector.findDistance(left, right)
        # print(p1[1],l1)
        # print(left[0],right[0])
        # if left[0]<250 and right[0]>500:
        #     keyboard.press(Key.space)
        #     keyboard.release(Key.space)
        if l1<80:
            if counter==0:
                keyboard.press(Key.up)
                keyboard.release(Key.up)
        if p1[1]> 250:
            if counter==0:
                keyboard.press(Key.down)
                keyboard.release(Key.down)
        if left[0]<150:
               keyboard.press(Key.left)
               keyboard.release(Key.left)
        if right[0]>600:
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        # print(lmList)
        counter+=1
    #     delayCounter+=1
    # if delayCounter==8:
    #     delayCounter=0
    if counter==11:
        counter=0
    cv2.imshow("Temple Run",img)
    cv2.waitKey(1)
