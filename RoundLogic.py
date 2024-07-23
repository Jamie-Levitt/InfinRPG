from CharacterLogic import Character, getCharacterClasses
from MapLogic import genPaths

class RoundManager:
    def __init__(self):
        self.round = 0
        print(self.round)

    def startUp(self):
        inpStr = 'Choose your class ('
        classList = []
        classRef = getCharacterClasses()
        print('Classes Info:')
        for i, charClass in enumerate(classRef):
            classList.append(charClass.className.lower())
            inpAddon = '[' + charClass.className + ']/' if i < len(classRef) - 1 else '[' + charClass.className + ']) '
            inpStr += inpAddon
            print('[' + charClass.className + ']')
            print(charClass.getStatsRef())

        chosenClass = input(inpStr).lower()
        if chosenClass in classList:
            self.player = classRef[classList.index(chosenClass)]
        else:
            print('THAT IS NOT A VALID CLASS NAME, PLEASE RETRY:')
            self.startUp()

        self.player.name = input('What is your name? ')

        print('And thus begins the journy of ' + self.player.name + ' the ' + self.player.className)

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

            playerPathPick = input(pPPstr)
            if playerPathPick in pathNames:
                chosenNode = paths[pathNames.index(playerPathPick)]
                chosen = True
            else:
                print('THAT IS NOT A VALID PATH NAME, PLEASE RETRY:')
        print(chosenNode.items)

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