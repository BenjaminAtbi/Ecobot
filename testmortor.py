from gpiozero import Robot, DistanceSensor
from time import sleep

motor1 = Motor(4, 6)
#motor2 = motor(17)

motor1.forward()
sleep(1)
#motor2.forward()
#sleep(1)