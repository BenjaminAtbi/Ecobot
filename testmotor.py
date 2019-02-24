from gpiozero import Servo
from time import sleep
myGPIO = 4
myGPIO2 = 25
myServo = Servo(myGPIO)
myServo2 = Servo(myGPIO2)
#motor2 = motor(17)
for i in range(0, 2):
    myServo.mid()
    sleep(1)
    myServo.max()
    sleep(1)
    myServo2.mid()
    sleep(1)
    myServo2.max()
    sleep(1)

    
    
    
    '''
    myServo2.max()
    sleep(1)
    myServo2.min()
    sleep(1)
    '''
    
    
#motor2.forward()
#sleep(1)