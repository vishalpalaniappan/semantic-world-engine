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
        self.primitive = self.getPrimitive(behavior_meta["primitive"])
        self.behavior = behavior_meta
        print("Created behavior:", behavior_meta["name"])
        pass

    def getName(self):
        return self.behavior["name"]

    def getPrimitive(self, name):
        '''
        Returns the primitive given its name.
        
        :param self: Reference to self.
        '''

        for primitive in self.primitives:
            if (name == primitive.getName()):
                return primitive