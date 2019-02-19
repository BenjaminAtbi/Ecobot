from gpiozero import Robot, DistanceSensor
from time import sleep

class MotorControl:
    def Cur_State(self, state):
        motor1 = motor(4, 14)
        motor2 = motor(17, 18)
        if state == 1:
            motor1.forward()
            motor2.forward()
        elif state == 2:
            motor1.backward()
            motor2.backward()
        elif state == 3:
            motor1.left()
            motor2.left()
        elif state == 4:
            motor1.right()
            motor2.right()






