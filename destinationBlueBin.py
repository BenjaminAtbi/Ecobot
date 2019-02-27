import numpy as np
import cv2
from imutils.video import VideoStream
import imutils
import math
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (Optional) video file")
args = vars(ap.parse_args())

blueBinLower = np.array([10, 150, 165], dtype="uint8")
blueBinHigher = np.array([35, 230, 230], dtype="uint8")

if args.get("video", None) is None:
    camera = VideoStream(src=0).start()
    time.sleep(2.0)

# otherwise, we are reading from a video file
else:
    camera = cv2.VideoCapture(args["video"])

firstFrame = None

while True:

    frame = camera.read()

    frame = frame if args.get("video", None) is None else frame[1]

    if frame is None:
        break

    bluebin = cv2.inRange(frame, blueBinLower, blueBinHigher)
    bluebin = cv2.GaussianBlur(bluebin, (3, 3), 0)

    (cnts, _) = cv2.findContours(bluebin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        # sort the contours and find the largest one that fits the description.
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)

        for i in range(len(cnts)):
            area = cv2.contourArea(cnt[i])
            perimeter = cv2.arcLength(cnt[i], True)

        # Good place to place some restriction on size/ shape.

            if (math.sqrt(area) > (perimeter / 4.5)) and (area > 100):
                (x, y), radius = cv2.minEnclosingCircle(cnt[i])
                center = (int(x), int(y))
                radius = int(radius)
                cv2.circle(bluebin, center, radius, (0, 255, 0), 2)

                break

    # Use the x,y cordinate values.
    x_cordinate = center[0]
    y_cordinate = center[1]

    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", bluebin)

camera.release()
cv2.destroyAllWindows()
