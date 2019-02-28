from motor import MotorController
import states as st

class robot: 


# ultrasonic 20,21

    def __init__(self): 
        #initialize modules
        self.motor = MotorController()
        # self.field = Field(20)
        # self.sorter = sorter()
        self.initializeStates()
        self.runnum = 0
        self.diagonal = False

        self.rundist = 4
        self.armlength = 2
        self.width = 1
        
    #initialize state options
    def initializeStates(self):

        self.state = st.initial()

    #main program loop
    def coreloop(self):
        while(True):
            
            # self.field.read()
            self.state.run(self)


bot = robot()
bot.coreloop()
