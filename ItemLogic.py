from Attributes import genRandAttribute, SwordAttributes

class Attribute:
    def __init__(self, jsonDATA:list):
        pass

class Item:
    def __init__(self, jsonDATA:list):
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
    def minLevel(self) -> int:
        return self.__minLevel
    @minLevel.setter
    def minLevel(self, minLevel:int):
        if minLevel >= 0:
            self.__minLevel = minLevel

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

    @property
    def rating(self) -> int:
        return self.__rating
    @rating.setter
    def rating(self, rating:int):
        if rating >= 0:
            self.__rating = rating
    #endregion