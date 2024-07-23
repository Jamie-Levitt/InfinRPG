from enum import Enum

class SwordAttributes(Enum):
    Blunt = {'Rating': 1, 'Value': -1, 'Power': -1}
    Graceful = {'Rating': 2, 'Value': 1, 'Power': 0}
    Mythical = {'Rating': 5, 'Value': 3, 'Power': 3}

from random import randint

def genRandAttribute(attributeEnum:Enum):
    possibleAttributes = []
    for attribute in attributeEnum:
        for a in attributeEnum:
            if a is not attribute:
                for i in range(attribute.value['Rating'] - 1):
                    possibleAttributes.append(a)

    return possibleAttributes[randint(0, len(possibleAttributes) - 1)]