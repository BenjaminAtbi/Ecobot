from time import sleep

class state():
    def __init__(self):
        i = 1

    def run(self,robot):
        raise AssertionError("Using base form of State")

class initial(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        robot.AngleRight(45)
        robot.runnum = robot.runnum + 1
        robot.state = seek()
        # leave bay

class seek(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        robot.motor.gateOpen()
        robot.motor.forwardDist(robot.runnum * robot.rundist)
        robot.motor.gateClose()
        robot.motor.load(robot)
        robot.motor.armDown()
        robot.motor.AngleLeft(135)
        robot.motor.gateOpen()
        robot.state = retrace()

        # turn into the ring
        # go forward

class retrace(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
       robot.motor.forwardDist((robot.runnum * robot.rundist * 0.7) - robot.armlength )
       robot.motor.gateClose()
       robot.motor.load(robot)
       robot.motor.forwardDist(robot.armlength)
       robot.motor.backwardDist(robot.width)
       robot.motor.AngleRight(90)
       robot.motor.BackDist(robot.runnum * robot.rundist * 0.7)
       robot.state = unload()


class unload(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
        robot.motor.leftGateOpen()
        robot.motor.RightGateOpen()
        sleep(2)
        robot.motor.leftGateClose()
        robot.motor.RightGateClose()
        robot.state = initial()