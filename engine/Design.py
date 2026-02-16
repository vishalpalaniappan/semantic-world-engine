import json
from pathlib import Path

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
            print("Loaded design meta:", getattr(self, key))
        else:
            raise Exception("Design is missing initial world state specification")
            