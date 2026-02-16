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

    def __init__(self, primitive_meta):
        print("Created primitive:", primitive_meta["name"])
        pass