'''
This object defines the primitives of the semantic world
and specifies how each primitive transforms the world state.
A primitive is an atomic transformation within the world
and serves as an axiom from which all higher-level
behaviors are constructed.

For example, it may include an action such as Place,
which defines how ownership of a participant is 
transferred between world participants. These primitives
form the foundational operations of the world.

Primitives are composed into behaviors, and behaviors
are composed into the state machine along with the
control flow and world participants. In this way, 
all state transitions within the design are constructed
from explicitly defined transformations.
'''
class Primitive():

    def __init__(self, primitiveMeta, primitiveType):
        self.meta = primitiveMeta
        self.primitiveType = primitiveType
        print("Created primitive:", primitiveMeta["name"])

    def getName(self):
        if "name" in self.meta:
            return self.meta["name"]
        else:
            return None        

    def transform(self, world, args):
        '''
        Perform the transformation on the world given the args.
        
        :param self: Reference to self.
        :param world: World Participants. 
        :param args: Transformation arguments.
        '''
        print("Initial world state", world)
        print("Transformation args:", args)