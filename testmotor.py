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

for i in range(0, 2):
    myServo.mid()
    myServo2.max()
    sleep(1)
    myServo.max()
    myServo2.mid()
    sleep(1)
 
miniFrontGate.mid()
sleep(1)
miniFrontGate.min()

rightPick.max()
leftPick.max()

rightPick.min()
leftPick.min()