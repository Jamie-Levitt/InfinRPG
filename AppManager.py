from FileLogic import DataLoader
from RoundLogic import RoundManager
from CharacterLogic import Character, Class
from ItemLogic import Item
from MapLogic import genPaths

global dataLoader
dataLoader = DataLoader()

global roundManager
roundManager = RoundManager()

class AppManager:
    def __init__(self):
        roundManager.setAppManager(self)
        self.affirmFiles()
        self.beginGameplayLoop()

    def affirmFiles(self):
        dataLoader.checkFileStructure()
        dataLoader.checkIgnore()
        dataLoader.checkBASE()
        dataLoader.loadData()

    def beginGameplayLoop(self):
        classInfo = dataLoader.getClasses()
        playerINFO = roundManager.getPlayer(classInfo)
        self.player = Character(playerINFO[0], self.getClassByCode(playerINFO[1]))

        self.round = 0

        while True:
            self.round = self.round + 1
            playerChoice = roundManager.initNewRound(genPaths(self.round, dataLoader.getItems()))
            
            if playerChoice[0] == 'shop':
                response = playerChoice[1].initNodeFunc(self.player.purse)
                if type(response) is Item:
                    self.player.addToInventory(response)

    #region STATIC METHODS
    @staticmethod
    def getClassByCode(classCode:str) -> Class:
        for classItem in dataLoader.getClasses():
            if classItem.code == classCode:
                return classItem
    @staticmethod
    def newCharFromClass(classInfo:list, charName:str) -> Character:
        classData = classInfo[1]

        charClass = Class(classInfo[0], classData['Name'], classData['Base Health'], classData['Stat'])
        return Character(charName, charClass)
    #endregion

    #region PROPERTIES
    @property
    def round(self) -> int:
        return self.__round
    @round.setter
    def round(self, round:int):
        if round >= 0:
            self.__round = round
        else:
            return ValueError
        
    @property
    def player(self) -> Character:
        return self.__player
    @player.setter
    def player(self, player:Character):
        self.__player = player

    #endregion