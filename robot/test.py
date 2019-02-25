import vision 
import cv2
import time

def testcircles():
    cam = cv2.VideoCapture(1)
    while(True):
        time.sleep(0.1)
        ret, image = cam.read()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        circles = vision.findCircles(gray)
        if circles is not None:
            # print(circles)
            for circle in circles[0]:
                cv2.circle(image, (circle[0],circle[1]), circle[2],(0,0,255))
        
        cv2.imshow('frame',image)
        print(image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

testcircles()