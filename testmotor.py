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
rightPick = Servo(myGPIO4)
leftPick = Servo(myGPIO5)

'''
for i in range(0, 2):
    rightWheel.min()
    leftWheel.max()


miniFrontGate.max()
sleep(1)
miniFrontGate.min()
sleep(1)
'''


#rightPick.max()
leftPick.max()
sleep(2)
#rightPick.min()
leftPick.min()
sleep(2)
