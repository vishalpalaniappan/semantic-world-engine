'''
This class represents a behavior, defined
as a semantic unit within the world. It
formally specifies the participants involved,
the semantic primitives it invokes, and the
precise transformation it applies to
the world state.
'''
class Behavior():

    def __init__(self, behavior_meta, primitives):
        self.primitives = primitives
        self.behavior = behavior_meta
        print("Created behavior:", behavior_meta["name"])
        pass

    def getName(self):
        return self.behavior["name"]