
'''
This class implements the state machine that defines
the control flow and state transformations of the design.
It consists of an ordered composition of behaviors, where
transitions are selected in response to environmental
input through the defined control flow.

Through this execution, the specified transformations are 
applied to the semantic world. Any transformation that 
cannot be realized is flagged, indicating that the design
is internally inconsistent, underspecified, or incomplete.

When a design is realized, it is this state machine that
is ultimately implemented. The substrate on which the
design executes may impose constraints, introducing 
environmental invariants that the design must satisfy.

This engine serves as the authoritative model for
validating implementations, ensuring that execution
conforms precisely to the defined semantic world.
'''
class StateMachine():

    def __init__(self, stateMachine, behaviors, world):
        self.stateMachine = stateMachine
        self.behaviors = behaviors
        self.world = world
        self.currPosition = 1 # Not zero indexed


    def step(self):
        '''
        Executes the current step in the state machine.
        
        :param self: Reference to self.
        '''
        currStep = self.stateMachine["data"][self.currPosition - 1]
        behavior = self.getBehavior(currStep["behavior"])
        if (behavior["acceptsInput"]):
            print("")
            acceptedInput = input(currStep["prompt"])

        print(currStep)
        print(behavior.getName(), behavior.primitive.getName())

        if ("goto" in currStep):
            self.currPosition = int(currStep["goto"])
            self.step()

    def getBehavior(self, behaviorName):
        '''
        Gets the specified behavior from the list given
        the behavior name.
        
        :param self: Reference to self
        :param behaviorName: Name of behavior in step.
        '''
        for behavior in self.behaviors:
            if (behavior.getName() == behaviorName):
                return behavior

    def run(self):
        '''
        Run the state machine.
        
        :param self: Reference to self.
        '''
        self.step()