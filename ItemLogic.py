from enum import Enum
from random import randint

from Attributes import genRandAttribute, SwordAttributes

pi = list('3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067')

class Item:
    def __init__(self, level:int, baseName:str, baseValue:int):
        self.baseName = baseName 
        self.level = level
        self.baseValue = baseValue
        self.genAttribute()

    def genAttribute(self):
        return

    #region PROPERTIES
    @property
    def baseName(self) -> str:
        return self.__baseName
    @baseName.setter
    def baseName(self, baseName:str):
        self.__baseName = baseName
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, attributeName:str):
        self.__name = attributeName + '' + self.baseName

    @property
    def level(self) -> int:
        return self.__level
    @level.setter
    def level(self, level:int):
        if level >= 0:
            self.__level = level

    @property
    def baseValue(self) -> int:
        return self.__baseValue
    @baseValue.setter
    def baseValue(self, baseValue:int):
        self.__baseValue = baseValue
    @property
    def value(self) -> int:
        return self.__value
    @value.setter
    def value(self, attributeValue:int):
        self.__value = self.baseValue + attributeValue
    #endregion

class Sword(Item):
    def __init__(self, roundNum:int):
        self.basePower = 2
        super().__init__(roundNum, 'Sword', 2)
    
    def genAttribute(self):
        attribute = genRandAttribute(SwordAttributes)
        self.name = attribute.name
        self.value = attribute.value['Value'] * self.level
        self.power = attribute.value['Power'] * self.level
    
    #region PROPERTIES
    @property
    def basePower(self) -> int:
        return self.__basePower
    @basePower.setter
    def basePower(self, basePower:int):
        self.__basePower = basePower
    @property
    def power(self) -> int:
        return self.__power
    @power.setter
    def power(self, attributePower:int):
        self.__power = attributePower + self.basePower
    #endregion

class Shop():
    def __init__(self, roundNum:int):
        self.nodeName = 'SHOP'
        self.coins = randint(1, 11 - int(pi[(roundNum % len(pi))])) * roundNum
        self.items = []
        for i in range(3):
            self.items.append(Sword(roundNum))