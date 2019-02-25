from gpiozero import Robot, DistanceSensor
from time import sleep

class MotorControl:
    def Cur_State(self, state, tf):
        motor1 = motor(4, 14)
        motor2 = motor(17, 18)
        
        if state == 'f':
            motor1.forward()
            motor2.forward()
            sleep(tf)
        elif state == 'b':
            motor1.backward()
            motor2.backward()
            sleep(tf)
        elif state == 'l':
            motor1.left()
            motor2.left()
            sleep(tf)
        elif state == 'r':
            motor1.right()
            motor2.right()
            sleep(tf)
        elif state == 'u':
            motor1.right()
            motor2.left()
            sleep(tf)







