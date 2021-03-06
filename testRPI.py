import RPi.GPIO as GPIO
from time import sleep

def SetAngle(angle):
	duty = (angle / 18) + 2
	GPIO.output(4, True)
    pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(4, False)
    pwm.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)
pwm=GPIO.PWM(4, 50)
pwm.start(0)

def SetAngle(angle):
	duty = (angle / 18) + 2
	GPIO.output(4, True)
    pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(4, False)
    pwm.ChangeDutyCycle(0)

SetAngle(90) 
pwm.stop()
GPIO.cleanup()