from time import sleep

class state():
    # def __init__(self):
    #     i = 1

    def run(self,robot):
        raise AssertionError("Using base form of State")

class initial():
    
    def run(self,robot):
        try:
            robot.motor.armDown()
            robot.motor.forward(.5)
            # robot.motor.AngleRight(45)
            robot.runnum = robot.runnum + 1
            
            print("inital")
            # leave bay
        except Exception as e: 
            print(e)
        robot.state = seek()

class seek():
    # def __init__(self):
    #     super().__init__(self)
    
    def run(self,robot):
        try:
            robot.motor.gateOpen()
            robot.motor.forwardDist(robot.runnum * robot.rundist + 6)
            robot.motor.gateClose()
            robot.motor.load(robot)
            robot.motor.armDown()
            robot.motor.AngleLeft(135)
            robot.motor.gateOpen()
            
            print("seek")
        except Exception as e: 
            print(e)
        robot.state = retrace()
        # turn into the ring
        # go forward

class retrace():
    # def __init__(self):
    #     super().__init__(self)
    
    def run(self,robot):
        try:
            robot.motor.forwardDist(((robot.runnum * robot.rundist +6)* 0.7) - robot.armlength )
            robot.motor.gateClose()
            robot.motor.load(robot)
            robot.motor.forwardDist(robot.armlength)
            robot.motor.backDist(robot.width)
            robot.motor.AngleRight(90)
            robot.motor.backDist(((robot.runnum * robot.rundist +6) * 0.7) + .5)
            
            print("retrace")
        except Exception as e: 
            print(e)
        robot.state = unload()
class unload():
    # def __init__(self):
    #     super().__init__(self)
    
    def run(self,robot):
        try:
            robot.motor.leftGateOpen()
            robot.motor.rightGateOpen()
            sleep(2)
            robot.motor.leftGateClose()
            robot.motor.rightGateClose()
            
            print("unload")
        except Exception as e: 
            print(e)
        robot.state = initial()