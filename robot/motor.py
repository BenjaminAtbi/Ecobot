from gpiozero import Robot, DistanceSensor
from gpiozero import Servo
from gpiozero import AngularServo 
from time import sleep
import numpy as np
from enum import Enum

# RIGHT BACK GATE
# closed ->  max()
# open -> mid() 

# LEFT BACK GATE
# closed -> min() 
# open -> mid() 

# SORTER
# left -> min()
# middle -> .value = -0.5
# right -> .value = 0

# RIGHT ARM
# up -> .value = 0.2
#        sleep .5
#       .value = -0.2
# down -> .value = -0.5
#       sleep .7
#       .value = -0.2

# LEFT MOTOR
# forward -> .value = 0.2
# bakcward -> .value = -0.6
# stop -> .value = -0.2

# RIGHT MOTOR
# forward -> .value = -0.6
# backward -> .value = 0.2
# stop -> .value = -0.2


leftArmGPIO = 17 # leftArm 
rightArmGPIO = 18 # rightArm
leftBackGateGPIO = 27 # LeftBackGate
leftWheelGPIO = 22 # leftWheel
rightBackGateGPIO = 23 # rightBackGate
sorterGPIO = 24 # sorter
rightWheelGPIO = 25 # rightWheel
frontGateGPIO = 4  # frontGate

# controls motor functions
class MotorController:

    

    def __init__(self):
        
        self.leftArm = Servo(leftArmGPIO)
        self.leftWheel = Servo(leftWheelGPIO)
        self.leftBackGate = Servo(leftBackGateGPIO)
        self.rightArm = Servo(rightArmGPIO)
        self.rightWheel = Servo(rightWheelGPIO)
        self.rightBackGate = Servo(rightBackGateGPIO)
        self.sorter = Servo(sorterGPIO)
        self.frontGate = Servo(frontGateGPIO)

        # requires input of angles
        # *********************************

    
    # RIGHT BACK GATE
# closed ->  max()
# open -> mid() 
    def rightGateClose(self):
        self.rightBackGate.max()

    def rightGateOpen(self):
        self.rightBackGate.mid()

# LEFT BACK GATE
# closed -> min() 
# open -> mid()     

    def leftGateClose(self):
        self.leftBackGate.min()

    def leftGateOpen(self):
        self.leftBackGate.mid()

# SORTER
# left -> min()
# middle -> .value = -0.5
# right -> .value = 0

    def sorterLeft(self):
        self.sorter.min()

    def sorterRight(self):
        self.sorter.value = 0

    def sorterMid(self):
        self.sorter.value = -0.5


# RIGHT ARM
# up -> .value = 0.2
#        sleep .5
#       .value = -0.2
# down -> .value = -0.5
#       sleep .7
#       .value = -0.2


    def armUp(self):
        self.rightArm.value = 0.2
        sleep(.5)
        self.value = -0.2

    def armDown(self):
        self.rightArm.value = -0.5
        sleep(.7)
        self.value = -0.2 

# LEFT MOTOR
# forward -> .value = 0.2
# bakcward -> .value = -0.6
# stop -> .value = -0.2

# RIGHT MOTOR
# forward -> .value = -0.6
# backward -> .value = 0.2
# stop -> .value = -0.2

    def pause(self):
        self.leftWheel.value = -0.2
        self.rightWheel.value = -0.2
        sleep(0.1)

    def forward(self,length):
        self.leftWheel.value = 0.2
        self.rightWheel.value = -0.6
        sleep(length)
        self.pause()

    def backward(self,length):
        self.leftWheel.value = -0.6
        self.rightWheel.value = 0.2
        sleep(length)
        self.pause()

    def left(self, length):
        self.leftWheel.value = -0.6
        self.rightWheel.value = -0.6
        sleep(length)
        self.pause()

    def gateOpen(self):
        self.frontGate.max()

    def gateClose(self):
        self.frontGate.min()


m = MotorController()
m.armDown()
m.gateOpen()
m.forward(1)
m.backward(1)
m.gateClose()
m.armUp()


#represents a motor designed to swap between various pre-set angles


#Arms
#wheels
# class continuousServo()

