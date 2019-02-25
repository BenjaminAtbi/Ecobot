import numpy as np
import math

class vector:
    def __init__(self,xorigin,yorigin,x,y):
        self.x = x
        self.y = y
        self.xorigin = xorigin
        self.yorigin = yorigin
        self.length = math.sqrt(math.pow(x,2) + math.pow(y,2))

def safediv(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

# class timermanager:
#     def __init__(self):
#          activetimers = 