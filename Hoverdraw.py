import cv2 as cv
import numpy as np

#Setting the Color Boxes On the top of Video
def top_shapes_color(frame):
    cv.rectangle(frame,(0,0),(220,100),(0,0,0),cv.FILLED)
    cv.rectangle(frame,(220,0),(440,100),(0,0,255),cv.FILLED)
    cv.rectangle(frame,(440,0),(650,100),(255,255,255),cv.FILLED)
    cv.line(frame,(440,0),(650,100),(0,0,255),2,cv.BORDER_ISOLATED)
    cv.line(frame,(650,0),(440,100),(0,0,255),2,cv.BORDER_ISOLATED)

video=cv.VideoCapture(0)

#Setting Screen Values 
video.set(3,660)
video.set(4,612)

#Video Loop
while True:
    success,frame=video.read()
    top_shapes_color(frame)
    cv.imshow("Hover Draw",frame)
    if cv.waitKey(1) == ord('q'):
        break
video.release()