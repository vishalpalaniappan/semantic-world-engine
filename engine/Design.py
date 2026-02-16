import json
from pathlib import Path
from engine.Participant import Participant
from engine.Behavior import Behavior
from engine.Primitive import Primitive
from engine.StateMachine import StateMachine

'''
This class represents the design. It accepts a root design JSON
file and loads the metadata from the relevant files. It then intializes
the state machine and accepts the inputs from the user while performing
the necessary world transformations as described by the semantic primitives
that build the behavior.
'''
class Design():

    def __init__(self, designPath):
        self.designPath = designPath
        self.loadDesign()

    def loadDesign(self):
        '''
        Loads the design from the specified file. It loads
        the meta data from each of the relevant files.
        
        :param self: Reference to instantiated object.
        '''
        with open(self.designPath) as f:
            self.designMeta = json.loads(f.read())

        for file in self.designMeta["files"]:
            self.loadDesignMeta(file)
        
        self.processMetadata()
        
    def loadDesignMeta(self, key):
        '''
        Loads the metadata for the specified key.
        
        :param self: Reference to instantiated object.
        :param key: Key of metadata being loaded.
        '''
        if key in self.designMeta["files"]:
            original_path = Path(self.designPath)
            new_path = original_path.parent / self.designMeta["files"][key]
            with open(new_path) as f:
                setattr(self, key, json.loads(f.read()))
            # print("Loaded design meta:", getattr(self, key))
        else:
            raise Exception("Design is missing initial world state specification")
        
    def processMetadata(self):
        '''
        Processes the metadata and creates the relevant objects
        by calling the relevant functions.
        
        :param self: Reference to instantiated object.
        :param key: Key of metadata being processed.
        '''
        self.processParticipants()
        self.processPrimitives()
        self.processBehaviors()
        self.processWorldState()
        self.processStateMachine()

    def processParticipants(self):
        '''
        Create participants from the metadata.
        
        :param self: Reference to instantiated object.
        '''
        if "data" not in getattr(self, "participants_meta"):
            raise Exception("Participants metadata doesn't contain data key")
        
        self.participant_types = {}
        for participant in self.participants_meta["data"]:
            self.participant_types[participant["name"]] = participant

    def processBehaviors(self):
        '''
        Create behaviors from the metadata.
        
        :param self: Reference to instantiated object.
        '''
        if "data" not in getattr(self, "behaviors_meta"):
            raise Exception("Behaviors metadata doesn't contain data key")
        
        self.behaviors = []
        for behavior in self.behaviors_meta["data"]:
            obj = Behavior(behavior, self.primitives)
            self.behaviors.append(obj)

    def processPrimitives(self):
        '''
        Create primitives from the metadata.
        
        :param self: Reference to instantiated object.
        '''
        if "data" not in getattr(self, "primitives_meta"):
            raise Exception("Primitives metadata doesn't contain data key")
        
        self.primitives = []
        for primitive in self.primitives_meta["data"]:
            obj = Primitive(primitive)
            self.primitives.append(obj)

    def processWorldState(self):
        '''
        Create the world state from the metadata. It intializes
        objects with the specified participants.
        
        :param self: Reference to instantiated object.
        '''
        if "data" not in getattr(self, "initial_world_state_meta"):
            raise Exception("Initial world state doesn't contain data key")
        
        self.world = []
        for entry in self.initial_world_state_meta["data"]:

            if entry["participant"] not in self.participant_types:
                raise Exception("World state contains ambiguous participant")
            
            participant = Participant(self.participant_types[entry["participant"]])
            self.world.append(participant)

        # Display the world state
        for paritcipant in self.world:
            print(paritcipant.name)

    def processStateMachine(self):
        '''
        Initializes the state machine.
        
        :param self: Reference to instantiated object.
        '''
        self.stateMachine = StateMachine(
            getattr(self, "state_machine_meta")
        )