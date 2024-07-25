from enum import Enum
from random import randint

from Attributes import genRandAttribute, SwordAttributes
from FileLogic import DataLoader

pi = list('3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067')

class Attribute:
    def __init__(self, jsonDATA:list):
        pass

class Item:
    def __init__(self, jsonDATA:list):
        print(jsonDATA)
        self.refCODE = jsonDATA[0]
        jsonDATA = jsonDATA[1]
        self.baseName = jsonDATA['Name']
        self.value = jsonDATA['Value']
        self.stat = jsonDATA['Stat']
        self.rating = jsonDATA['Rating']
        self.minLevel = jsonDATA['Min Level']

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
    def refCode(self) -> str:
        return self.__refCode
    @refCode.setter
    def refCode(self, refCode:str):
        self.__refCode = refCode
        
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

'''def rollItemList(itemList:list[type[Item]]) -> list[type[Item]]:
    legalItems = [item for item in itemList if item.]
    possibleItems = []
    for item in itemList:
        for a in attributeEnum:
            if a is not attribute:
                for i in range(attribute.value['Rating'] - 1):
                    possibleAttributes.append(a)

    items = []

    return possibleAttributes[randint(0, len(possibleAttributes) - 1)]
    for i in range(3):
        fro'''

class Shop():
    def __init__(self, roundNum:int, itemList:list[type[Item]]):
        self.nodeName = 'SHOP'
        self.coins = randint(1, 11 - int(pi[(roundNum % len(pi))])) * roundNum
        self.items = rollItemList(itemList)
    
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