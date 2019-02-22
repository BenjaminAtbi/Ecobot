from gpiozero import Motor
from time import sleep

motor1 = Motor(forward = 4, backward = 2)
#motor2 = motor(17)

motor1.forward()
sleep(5)
#motor2.forward()
#sleep(1)