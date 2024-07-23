from enum import Enum

class Character:
    def __init__(self, className:str):
        self.className = className
        self.level = 1
    
    def getStatsRef(self) -> dict:
        return "MAX HEALTH: " + str(self.maxHealth) + "}"

    #region PROPERTIES
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name:str):
        self.__name = name
    @property
    def className(self) -> str:
        return self.__className
    @className.setter
    def className(self, className:str):
        self.__className = className

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
    
def getCharacterClasses() -> list[type[Character]]:
    classes = []
    for charClass in Character.__subclasses__():
        classes.append(charClass())
        #classes.extend(getCharacterClasses(charClass))
    return classes