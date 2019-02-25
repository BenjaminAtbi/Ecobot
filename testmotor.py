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
#miniFrontGate = Servo(myGPIO3)
#rightPick = Servo(myGPIO4)
leftPick = Servo(myGPIO5)

leftPick.value = -1

'''
rightWheel.min()
leftWheel.min()
sleep(3)


miniFrontGate.max()
sleep(1)
miniFrontGate.min()
sleep(1)
'''

leftPick.max()
sleep(2)

leftPick.min()
sleep(2)

