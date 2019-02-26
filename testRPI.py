import RPi.GPIO as GPIO
from time import sleep

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(4, True)
    GPIO.output(25, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(4, False)
    GPIO.output(25, True)
	pwm.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

pwm=GPIO.PWM(4, 50)
pwm2=GPIO.PWM(25, 50)
pwm.start(0)
pwm2.start(0)
SetAngle(90) 
pwm.stop()
pwm2.stop()
GPIO.cleanup()