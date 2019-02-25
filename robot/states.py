class state:

    def run(self,robot):
        raise AssertionError("Using base form of State")

class initial(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
        # move motor out of corner? 
        # robot.state = robot.states['seek']

class seek(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
        #*********************************************
        #move forward
        #if reaching edge:
        #   turn, etc

        #if timer up:
        #     robot.state = states['retrace']
        #if target detected:
        #     set target
        #     robot.state = states['approach']
        #if obstacle spotted:
        #     robot.state = robot.states['avoid']

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
        
        #*********************************************
        # lift arm, deposit
        # robot.state = robot.states['seek']

class retrace(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
        #*********************************************
        # somehow head towards starting location 
        # if obstacle
        #   robot.state = robot.states['avoid']

class unload(state):
    def __init__(self):
        super().__init__(self)
    
    def run(self,robot):
        
        #*********************************************
        # dump shit 
        # call it a day

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