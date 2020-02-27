from enum import Enum

class Output(Enum):
    json = 1
    csv = 2

    @staticmethod
    def GetEnumAsList():
        return [e.name for e in Output]
