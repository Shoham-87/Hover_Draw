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
    kernel = np.ones((5,5),np.uint8)
    imgHSV=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_skin = np.array([0,2,40], dtype=np.uint8)
    upper_skin = np.array([173,49,127], dtype=np.uint8)
    mask=cv.inRange(imgHSV,lower_skin,upper_skin)
    mask = cv.dilate(mask,kernel,iterations = 4)
    mask = cv.GaussianBlur(mask,(5,5),100) 
    cv.imshow("Hand",mask)

video=cv.VideoCapture(0)

#Setting Screen Values 
video.set(3,1060)
video.set(4,812)

#Video Loop
while True:
    success,frame=video.read()
    top_shapes_color(frame)
    hand_detection(frame)
    cv.imshow("Hover Draw",frame)
    if cv.waitKey(1) == ord('q'):
        break
video.release()
# cv.distroyAllWindows()