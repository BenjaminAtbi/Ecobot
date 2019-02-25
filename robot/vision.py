import numpy as np
import cv2
import math

#Return array of circle values
#image must be greyscale
def findCircles(image):
    image = cv2.medianBlur(image,5)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT,3,50,maxRadius=50)
    return circles



# triggered once an object is deposited in the sorting container.
# runs parallel to other functions
class sorter():
    __init__(self):
    





