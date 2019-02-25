from gpiozero import Servo
from time import sleep
myGPIO = 4
myGPIO2 = 25
myGPIO3 = 23
myGPIO4 = 24
myGPIO5 = 22

myServo = Servo(myGPIO)
myServo2 = Servo(myGPIO2)
miniFrontGate = Servo(myGPIO3)
rightPick = Servo(myGPIO4)
leftPick = Servo(myGPIO5)

'''
myServo.mid()
myServo2.max()
sleep(1)

myServo.max()
myServo2.mid()
sleep(1)
'''

miniFrontGate.max()
sleep(1)
miniFrontGate.min()
sleep(1)

rightPick.min()
leftPick.max()
sleep(2)
rightPick.max()
leftPick.min()
sleep(2)