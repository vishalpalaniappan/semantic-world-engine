import json

class Design():

    def __init__(self, desighPath):
        self.designPath = desighPath
        self.loadDesign()

    def loadDesign(self):
        with open(self.designPath) as f:
            print(json.dumps(f.read()))