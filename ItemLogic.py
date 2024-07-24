from enum import Enum
from random import randint

from Attributes import genRandAttribute, SwordAttributes

pi = list('3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067')

class Item:
    def __init__(self, level:int, baseName:str, value:int, stat:str):
        self.baseName = baseName 
        self.level = level
        self.value = value
        self.stat = stat
        self.genAttribute()

    def genAttribute(self):
        att = genRandAttribute(SwordAttributes)
        self.name = att.name
        self.value = att.value['Value']
        self.statAmount = att.value['Power']
        return
    
    def getStatsRef(self) -> str:
        return "NAME: {" + self.name + "} LEVEL: {" + str(self.level) + "} " + self.stat.upper() + ": {" + str(self.statAmount) + "} PRICE: {" + str(self.value) + "}"

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
        self.__name = attributeName + ' ' + self.baseName

    @property
    def classCode(self) -> str:
        return self.__classCode
    @classCode.setter
    def classCode(self, classCode:str):
        self.__classCode = classCode

    @property
    def level(self) -> int:
        return self.__level
    @level.setter
    def level(self, level:int):
        if level >= 0:
            self.__level = level

    @property
    def value(self) -> int:
        return self.__value
    @value.setter
    def value(self, attributeValue:int):
        try:
            self.__value += attributeValue
        except:
            self.__value = attributeValue

    @property
    def stat(self) -> str:
        return self.__stat
    @stat.setter
    def stat(self, stat:str):
        self.__stat = stat
    @property
    def statAmount(self) -> int:
        return self.__statAmount
    @statAmount.setter
    def statAmount(self, attributeStatAmount:int):
        try:
            self.__statAmount += attributeStatAmount
        except:
            self.__statAmount = 2 + attributeStatAmount
    #endregion

class Shop():
    def __init__(self, roundNum:int):
        self.nodeName = 'SHOP'
        self.coins = randint(1, 11 - int(pi[(roundNum % len(pi))])) * roundNum
        self.items = []
        for i in range(3):
            self.items.append(Item(roundNum, 'Sword', 2, 'Power'))
    
    def initNodeFunc(self, playerPurse:int):
        print("\nYour Purse: {" + str(playerPurse) + "} ----------------------------------\n")
        print("Welcome to my shop, let me show you my wares ----------------------------\n")

        itemNums = []
        inpOptions = 'CHOOSE AN OPTION ('
        for i, item in enumerate(self.items):
            itemNums.append(str(i))
            inpAddon = '[' + str(i) + '],' if i < len(self.items) - 1 else '[' + str(i) + '],[INVENTORY],[LEAVE])'
            inpOptions += inpAddon
            print('[' + str(i) + ']: ' + item.getStatsRef())

        chosen = False
        while chosen is False:
            playerChoice = input(inpOptions).lower()
            if playerChoice == 'leave':
                return 'EXIT'
            elif playerChoice in itemNums:
                item = self.items[i]
                if item.value <= playerPurse:
                    return item
                else:
                    print("You can't afford that, please choose another item")
            else:
                print("THAT IS NOT A VALID CHOICE, PLEASE RETRY:")