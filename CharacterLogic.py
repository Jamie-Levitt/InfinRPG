from enum import Enum

from ItemLogic import Item

class Class:
    def __init__(self, jsonDATA:list):
        self.code = jsonDATA[0]
        jsonDATA = jsonDATA[1]
        self.name = jsonDATA['Name']
        self.baseHealth = jsonDATA['Base Health']
        self.statName = jsonDATA['Stat']
        self.statAmount = 1

    def getStatsRef(self) -> str:
        return "BASE HEALTH: {" + str(self.baseHealth) + "}, " + self.statName.upper() + " {" + str(self.statAmount) + "}"
        
    #region PROPERTIES
    @property
    def code(self) -> str:
        return self.__code
    @code.setter
    def code(self, code:str):
        self.__code = code
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name:str):
        self.__name = name
        
    @property
    def baseHealth(self) -> int:
        return self.__baseHealth
    @baseHealth.setter
    def baseHealth(self, baseHealth:int):
        self.__baseHealth = baseHealth

    @property
    def statName(self) -> str:
        return self.__statName
    @statName.setter
    def statName(self, statName:str):
        self.__statName = statName

    @property
    def statAmount(self) -> int:
        return self.__statAmount
    @statAmount.setter
    def statAmount(self, statAmount:int):
        self.__statAmount = statAmount
    #endregion

class Character:
    def __init__(self, name:str, charClass:Class):
        self.name = name
        self.charClass = charClass
        self.level = 1
        self.maxHealth = charClass.baseHealth
        self.purse = 5
        self.inventory = []

    def buyItem(self, item:Item):
        self.purse = -item.value
        self.addToInventory(item)

    #region PROPERTIES
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name:str):
        self.__name = name
    @property
    def charClass(self) -> Class:
        return self.__charClass
    @charClass.setter
    def charClass(self, charClass:Class):
        self.__charClass = charClass

    @property
    def purse(self) -> int:
        return self.__purse
    @purse.setter
    def purse(self, purse:int):
        self.__purse = purse
    @property
    def inventory(self) -> list[type[Item]]:
        return self.__inventory
    @inventory.setter
    def inventory(self, inventory:list[type[Item]]):
        self.__inventory = inventory
    def addToInventory(self, item:Item):
        self.__inventory.append(item)

    @property
    def level(self) -> int:
        return self.__level
    @level.setter
    def level(self, level:int):
        if level > 0:
            self.__level = level
            
    @property
    def maxHealth(self) -> int:
        return self.__maxHealth
    @maxHealth.setter
    def maxHealth(self, health:int):
        self.__maxHealth = health
        self.health = health
    @property
    def health(self) -> int:
        return self.__health
    @health.setter
    def health(self, health:int):
        self.__health = health
    #endregion

from FileLogic import loadClasses

def getClassesInfo() -> list[type[Class]]:
    classInfoList = []
    for classItem in loadClasses():
        classInfoList.append(Class(classItem))
    return classInfoList

def getClassByCode(classCode:str) -> Class:
    for classItem in loadClasses():
        if classItem[0] == classCode:
            return Class(classItem)

def newCharFromClass(classInfo:list, charName:str) -> Character:
    classData = classInfo[1]

    charClass = Class(classInfo[0], classData['Name'], classData['Base Health'], classData['Stat'])
    return Character(charName, charClass)