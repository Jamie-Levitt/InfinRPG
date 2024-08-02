from enum import Enum

class SwordAttributes(Enum):
    Blunt = {'Rating': 1, 'Value': -1, 'Power': -1}
    Graceful = {'Rating': 2, 'Value': 1, 'Power': 0}
    Mythical = {'Rating': 5, 'Value': 3, 'Power': 3}

class Attribute:
    def __init__(self, jsonDATA:dict):
        self.rating = jsonDATA['Rating']
        pass

def loadAttributes(jsonDATA:dict, targetCODE:str) -> Enum:
    dataREF = jsonDATA[targetCODE]
    attribute_template = """
    @unique
    class {attributeType}Attributes(Enum)
    {enumBody}
    """
    attributes = '\n'.join([f"    {key} = '{attRef}'" for (key, attRef) in dataREF])
    return attribute_template.format(attributeType = targetCODE, attributeBody = attributes)

from random import randint

class Attributable:
    def __init__(self, selfTargetCODE:str):
        self.selfTargetCode = selfTargetCODE

    def genAttribute(self):
        genRandAttribute(loadAttributes())

    @property
    def selfTargetCode(self) -> str:
        return self.__selfTargetCode
    @selfTargetCode.setter
    def selfTargetCode(self, selfTargetCODE:str):
        self.__selfTargetCode = selfTargetCODE

def genRandAttribute(attributeEnum:Enum):
    possibleAttributes = []
    for attribute in attributeEnum:
        for a in attributeEnum:
            if a is not attribute:
                for i in range(attribute.value['Rating'] - 1):
                    possibleAttributes.append(a)

    return possibleAttributes[randint(0, len(possibleAttributes) - 1)]