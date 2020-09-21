import cv2 as cv
import numpy as np

#Setting the Color Boxes On the top of Video
def top_shapes_color(frame):
    cv.rectangle(frame,(0,0),(220,100),(0,0,0),cv.FILLED)
    cv.rectangle(frame,(220,0),(440,100),(0,0,255),cv.FILLED)
    cv.rectangle(frame,(440,0),(650,100),(255,255,255),cv.FILLED)
    cv.line(frame,(440,0),(650,100),(0,0,255),2,cv.BORDER_ISOLATED)
    cv.line(frame,(650,0),(440,100),(0,0,255),2,cv.BORDER_ISOLATED)

#detecting the Hand
def hand_detection(frame):
    newPoints=[]
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
    imgHSV=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_skin = np.array([98,23,0], dtype=np.uint8)
    upper_skin = np.array([179,255,142], dtype=np.uint8)
    mask=cv.inRange(imgHSV,lower_skin,upper_skin)
    mask = cv.dilate(mask,kernel,iterations = 4)
    mask = cv.GaussianBlur(mask,(5,5),100) 
    x,y=getContours(mask)
    cv.circle(imgResult,(x,y),10,(0,0,255),cv.FILLED,cv.BORDER_ISOLATED)
    if x!=0 and y>=100:
        newPoints.append([x,y])
    return newPoints

#getting contours around the hand
def getContours(frame):
    contours,hierarchy = cv.findContours(frame,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500:
            cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv.boundingRect(approx)
    return x+h//2,y

#To Draw on the Screen
def DrawOnScreen(myPoints):
    for point in myPoints:
        cv.circle(imgResult, (point[0], point[1]), 10, (0,0,255), cv.FILLED,cv.BORDER_ISOLATED)

video=cv.VideoCapture(0)

#Setting Screen Values 
video.set(3,1060)
video.set(4,812)

myPoints =  [] 
#Video Loop
while True:
    success,frame=video.read()
    imgResult=frame.copy()
    top_shapes_color(imgResult)
    newPoints=hand_detection(frame)
    if len(newPoints)!=0:
        for x in newPoints:
            myPoints.append(x)
    if len(myPoints)!=0:
        DrawOnScreen(myPoints)
    cv.imshow("Hover Draw",imgResult)
    if cv.waitKey(1) == ord('q'):
        break
video.release()
# cv.distroyAllWindows()