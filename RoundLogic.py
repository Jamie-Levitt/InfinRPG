from CharacterLogic import Character, Class, getClassesInfo, getClassByCode
from MapLogic import genPaths

class RoundManager:
    def __init__(self):
        self.round = 0
        print(self.round)

    def startUp(self):
        inpStr = 'Choose your class ('
        classList = []
        classCodeList = []
        classRefList = getClassesInfo()
        print('Classes Info:')
        for i, classRef in enumerate(classRefList):
            className = classRef.name.upper()
            classList.append(className.lower())
            classCodeList.append(classRef.code)
            inpAddon = '[' + className.upper() + ']/' if i < len(classRefList) - 1 else '[' + className.upper() + ']) '
            inpStr += inpAddon
            print('[' + className.upper() + ']')
            print(classRef.getStatsRef())

        chosenClass = input(inpStr).lower()
        if chosenClass in classList:
            playerClass = getClassByCode(classCodeList[classList.index(chosenClass)])
        else:
            print('THAT IS NOT A VALID CLASS NAME, PLEASE RETRY:')
            self.startUp()

        playerName = input('What is your name? ')
        self.player = Character(playerName, playerClass)        
        print('And thus begins the journy of ' + self.player.name + ' the ' + self.player.charClass.name)

    def initNewRound(self):
        self.round = self.round + 1
        chosen = False
        while chosen is False:
            pathNames = []
            paths = genPaths(self.round)
            pPPstr = 'Choose a path to follow: ('
            for i, node in enumerate(paths):
                pathNames.append(node.nodeName.lower())
                pPPAppend = '[' + node.nodeName + ']/' if i < len(paths) - 1 else '[' + node.nodeName + ']) '
                pPPstr += pPPAppend

            playerPathPick = input(pPPstr).lower()
            if playerPathPick in pathNames:
                chosenNode = paths[pathNames.index(playerPathPick)]
                chosen = True
            else:
                print('THAT IS NOT A VALID PATH NAME, PLEASE RETRY:')
        for statref in chosenNode.items: print(statref.getStatsRef())

    #region PROPERTIES
    @property
    def round(self) -> int:
        return self.__round
    @round.setter
    def round(self, round:int):
        if round >= 0:
            self.__round = round

    @property
    def player(self) -> Character:
        return self.__player
    @player.setter
    def player(self, player:Character):
        self.__player = player
    #endregion