from gpiozero import Servo
from time import sleep
myGPIO = 17
myServo = Servo(myGPIO)
#motor2 = motor(17)
while True:
    myServo.max()
    sleep(1)
    myServo.min()
    sleep(1)
    
    
#motor2.forward()
#sleep(1)