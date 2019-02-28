import time import sleep

class state:

    def run(self,robot):
        raise AssertionError("Using base form of State")

class initial(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        robot.AngleRight(45)
        robot.runnum = robot.runnum + 1
        robot.state = robot.states["seek"]
        # leave bay

class seek(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        robot.gateOpen()
        robot.forwardDist(robot.runnum * robot.rundist)
        robot.gateClose()
        robot.load()
        robot.armDown()
        robot.AngleLeft(135)
        robot.gateOpen()
        robot.state = robot.states["retrace"]

        # turn into the ring
        # go forward

class approach(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):

        #*********************************************       
        #line up with target 
        #move forward correct amount
        # robot.state = robot.states['load']

class load(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
    #    robot.gateClose()
    #    robot.armUp()
    #    sleep(2)
    #    robot.armDown()

    #    if(robot.diagonal){
    #        robot.state = robot.states["retrace"]
    #    } else {

    #    }



class retrace(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
       robot.forwardDist((robot.runnum * robot.rundist * 0.7) - robot.armlength )
       robot.gateClose()
       robot.load()
       robot.forwardDist(robot.armlength)
       robot.backwardDist(robot.width)
       robot.AngleRight(90)
       robot.BackDist(robot.runnum * robot.rundist * 0.7)
       robot.state = robot.states["unload"]


class unload(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
        robot.leftGateOpen()
        robot.RightGateOpen()
        sleep(2)
        robot.leftGateClose()
        robot.RightGateClose()
        robot.state = robot.states["initial"]

class avoid(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
        #*********************************************
        # avoid obstacles
        # if directive is seek
        #   robot.state = robot.states['seek']
        # if directive is retrace
        #   robot.state = robot.states['retrace]