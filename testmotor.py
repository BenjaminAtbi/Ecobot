from gpiozero import Servo
from time import sleep
myGPIO1 = 4  #right wheel
myGPIO2 = 25 # left wheel
myGPIO3 = 23 # mini front gate
myGPIO4 = 24 #right pick
myGPIO5 = 22 #left pick
myGPIO6 = 17 #leftbackgate
myGPIO7 = 18 #rightbackgate
myGPIO8 = 27 #classifier 

#rightWheel = Servo(myGPIO1)
#leftWheel = Servo(myGPIO2)
miniFrontGate = Servo(myGPIO3)
#rightPick = Servo(myGPIO4)
leftPick = Servo(myGPIO5)
'''
myCorrection=0
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(myGPIO5,min_pulse_width=minPW,max_pulse_width=maxPW)
 
while True:
 
  print("Set value range -1.0 to +1.0")
  for value in range(0,21):
    value2=(float(value)-10)/10
    servo.value=value2
    print(value2)
    sleep(0.5)
 
  print("Set value range +1.0 to -1.0")
  for value in range(20,-1,-1):
    value2=(float(value)-10)/10
    servo.value=value2
    print(value2)
    sleep(0.5)

rightWheel.value = 1
leftWheel.value = -1

rightWheel.min()
leftWheel.max()
sleep(3)
miniFrontGate.max()
sleep(1)
miniFrontGate.min()
sleep(1)
'''

miniFrontGate.value = 0
miniFrontGate.max()
sleep(1)
miniFrontGate.min()
sleep(1)


sleep(3)

leftPick.value = 0
leftPick.max()
sleep(1)
leftPick.min
sleep(1)