from gpiozero import Servo
from time import sleep
myGPIO = 4
myGPIO2 = 25
myServo = Servo(myGPIO)
myServo2 = Servo(myGPIO2)

for i in range(0, 2):
    myServo.mid()
    myServo2.mid()
    sleep(1)
    myServo.max()
    myServo2.max()
    sleep(1)
