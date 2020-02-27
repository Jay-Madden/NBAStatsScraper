from enum import Enum
class Output(Enum):
    json = 0
    csv = 1

    @staticmethod
    def GetEnumAsList():
        return [e.name for e in Output]
