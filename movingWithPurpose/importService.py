from presets import Presets
import json

class ImportService:

    def __init__(self):
        super().__init__()

    def setFile(self, file):
        self.file = file

    def getPresets(self):
        config = json.load(open(self.file))
        presets = Presets()
        presets.startLocation = config['start']
        presets.endLocation = config['goal']
        presets.maxVelocity = config['maxVelocity']
        presets.maxSteeringAngle = config['maxSteeringAngle']
        presets.facingDirection = presets.startLocation[2]
        return presets
