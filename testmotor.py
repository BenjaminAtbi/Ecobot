from gpiozero import Servo
from time import sleep
myGPIO = 15
#myGPIO2 = 22
myServo = Servo(myGPIO)
#myServo2 = Servo(myGPIO2)
#motor2 = motor(17)
while True:
    
    myServo.max()
    sleep(1)
    
    myServo.min()
    sleep(1)
    
    
    '''
    myServo2.max()
    sleep(1)
    myServo2.min()
    sleep(1)
    '''
    
    
#motor2.forward()
#sleep(1)