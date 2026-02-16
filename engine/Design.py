import json

class Design():

    def __init__(self, desighPath):
        self.designPath = desighPath
        self.loadDesign()

    def loadDesign(self):
        with open(self.designPath) as f:
            self.designMeta = json.loads(f.read())

        for file in self.designMeta["files"]:
            self.loadDesignMeta(file)
        
    def loadDesignMeta(self, key):
        if key in self.designMeta["files"]:
            self.state_machine = self.designMeta["files"]["initial_world_state"]
            print("Loaded design meta:", key)
        else:
            raise Exception("Design is missing initial world state specification")
            