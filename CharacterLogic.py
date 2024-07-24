from enum import Enum

class Stat:
    def __init__(self, name:str):
        self.name = name
        self.amount = 1
    
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def amount(self) -> int:
        return self.__amount
    @amount.setter
    def amount(self, amount:int):
        self.__amount = amount

class Class:
    def __init__(self, code:str, name:str, baseHealth:int, stat:Stat):
        self.code = code
        self.name = name
        self.baseHealth = baseHealth
        self.stat = stat
        
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
    def stat(self) -> Stat:
        return self.__stat
    @stat.setter
    def stat(self, stat:Stat):
        self.__stat = stat
    #endregion

class Character:
    def __init__(self, name:str, charClass:Class):
        self.name = name
        self.charClass = charClass
        self.level = 1
        self.maxHealth = charClass.baseHealth
    
    def getStatsRef(self) -> dict:
        return "MAX HEALTH: {" + str(self.maxHealth) + "}, " + self.stat.name.upper() + " {" + str(self.stat.amount) + "}"

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

class Warrior(Character):
    def __init__(self):
        super().__init__('Warrior')
        self.maxHealth = 1
        self.strength = 1

    def getStatsRef(self) -> dict:
        return "MAX HEALTH: {" + str(self.maxHealth) + "} STRENGTH: {" + str(self.maxHealth) + "}"

    #region PROPERTIES
    @property
    def strength(self) -> int:
        return self.__strength
    @strength.setter
    def strength(self, strength:int):
        self.__strength = strength
    #endregion

class Wizard(Character):
    def __init__(self):
        super().__init__('Wizard')
        self.maxHealth = 1
        self.mana = 1

    def getStatsRef(self) -> dict:
        return "MAX HEALTH: {" + str(self.maxHealth) + "} MANA: {" + str(self.mana) + "}"

    #region PROPERTIES
    @property
    def mana(self) -> int:
        return self.__mana
    @mana.setter
    def mana(self, mana:int):
        self.__mana = mana
    #endregion

from FileLogic import loadClasses

def getClassesInfo() -> list:
    classInfoList = []
    for classItem in loadClasses():
        classData = classItem[1]
        classStat = Stat(classData['Stat'])
        classInfoList.append([classData['Name'], "BASE HEALTH: {" + str(classData['Base Health']) + "}" + classStat.name + ": {" + str(classStat.amount) + "}"])
    return classInfoList

def newCharFromClass(classInfo:list, charName:str) -> Character:
    classCode = classInfo[0]
    classData = classInfo[1]

    classStat = Stat(classData['Stat'])
    charClass = Class(classCode, classData['Name'], classData['Base Health'], classStat)
    return Character(charName, charClass)