from __future__ import annotations
from random import randint

from ItemLogic import Item

def genPaths(roundNum:int, itemList:list[type[Item]]) -> list[type[Node]]:
    return [genNewShop(roundNum, itemList)]

class Node:
    def __init__(self, nodeName:str):
        self.nodeName = nodeName

    def initNodeFunc(self):
        pass

def rollItemList(roundNum:int, itemList:list[Item]) -> list[type[Item]]:
    legalItems = [item for item in itemList if item.minLevel <= roundNum]
    possibleItems = []
    for item in legalItems:
        for ite in legalItems:
            if ite is not item:
                for i in range(item.rating):
                    ite.level = roundNum
                    ite.genAttribute()
                    possibleItems.append(ite)

    itemList = []
    print(len(possibleItems))
    for i in range(3):
        iRef = randint(0, len(possibleItems) - 1)
        itemList.append(possibleItems[iRef])
        possibleItems.remove(possibleItems[iRef])
    return itemList

pi = list('3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067')

class Shop(Node):
    def __init__(self, roundNum:int, itemList:list[Item]):
        super().__init__('SHOP')
        self.coins = randint(1, 11 - int(pi[(roundNum % len(pi))])) * roundNum
        self.items = rollItemList(roundNum, itemList)
    
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


def genNewShop(roundNum:int, itemList:list[Item]) -> Shop:
    return Shop(roundNum, itemList)