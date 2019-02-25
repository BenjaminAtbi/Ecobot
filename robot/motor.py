from gpiozero import Robot, DistanceSensor
from time import sleep
import numpy as np

# controls motor functions
class Motor:

    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    def __init__(self):
        #hook wheel motors into abstract controller
        self.chasis = Robot(left=(4, 14), right=(17, 18))
        
        # requires input of importnat angles
        # *********************************
        self.scoop = AngleMotor( angles )
        self.feeder = AngleMotor( angles )
        self.sortswitch = AngleMotor( angles )
        self.bay1 = AngleMotor( angles )
        self.bay2 = AngleMotor( angles )

    def setChasis(self, state, speed=1):

        if state == 1:
            self.chasis.forward(speed)
        elif state == 2:
            self.chasis.backward(speed)
        elif state == 3:
            self.chasis.left(speed)
        elif state == 4:
            self.chasis.right(speed)
 
#represents a motor designed to swap between various pre-set angles
#base angle is first index of angles
class AngleMotor():
    # points should be an array of angles as floats
    def __init__(self, angles=[]):
        assert angles is not empty
        self.angles = angles
        self.targetAngle = None
        # initialize motor controller (unimplemented)
        # **********************************
    
    def setTargetAngle(self, angle):
        # set motor to angle (unimplemented)
        # **********************************
    
    def getTargetAngle(self):
        return self.targetAngle

    




