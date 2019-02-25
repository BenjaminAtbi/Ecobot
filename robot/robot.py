from motor import Motor
from field import Field
from vision import sorter
import states as st

class robot: 


    def __init__(self): 
        #initialize modules
        self.motor = Motor()
        self.field = Field(20)
        self.sorter = sorter()
        self.initializeStates()
        
    #initialize state options
    def initializeStates(self):
        self.states = dict()
        self.states['initial'] = st.initial()
        self.states['seek'] = st.seek()
        self.states['approach'] = st.approach()
        self.states['load'] = st.load()
        self.states['retrace'] = st.retrace()
        self.states['unload'] = st.unload()
        self.states['avoid'] = st.avoid()

        self.state = self.states['initial']

    #main program loop
    def coreloop(self):
        while(True):
            
            self.field.read()
            self.state.run(self)


bot = robot()