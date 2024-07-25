from __future__ import annotations
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from AppManager import AppManager
    from MapLogic import Node

class RoundManager:
    def __init__(self):
        pass

    def setAppManager(self, appManager:AppManager):
        self.appManager = appManager

    def getPlayer(self, classRefList:list) -> list:
        inpStr = 'Choose your class ('
        classList = []
        classCodeList = []
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
        if chosenClass not in classList:
            print('THAT IS NOT A VALID CLASS NAME, PLEASE RETRY:')
            self.getPlayer()
        playerName = input('What is your name? ')
        print('And thus begins the journy of ' + playerName.upper() + ' the ' + chosenClass.upper())
        return([playerName, classCodeList[classList.index(chosenClass)]])
    
    def initNewRound(self, paths:list) -> list[Union[str, Node]]:
        print(str(self.appManager.round) + ' | ' + str(self.appManager.player.inventory))
        chosen = False
        while chosen is False:
            pathNames = []
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
        return [playerPathPick, chosenNode]