'''
This class specifies a participant in this
semantic world. The participants are involved in
behavior and make up the world state. The world
is initialized with participants and as the state
machine iterates, the state of the participants
are modified.
'''
class Participant:

    def __init__(self, participant):
        self.name = participant["name"]
        print ("Created participant:", participant["name"])
        pass