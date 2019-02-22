from gpiozero import Servo
from time import sleep

myServo = Servo(4)
#motor2 = motor(17)
while True:
    myServo.mid()
    sleep(1)
    myServo.min()
    sleep(1)
    myServo.mid()
    sleep(1)
    myServo.max()
    sleep(1)
    
#motor2.forward()
#sleep(1)