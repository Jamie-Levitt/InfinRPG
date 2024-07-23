from ItemLogic import Shop

def genPaths(roundNum:int) -> list:
    return [genNewShop(roundNum)]

def genNewShop(roundNum:int) -> Shop:
    return Shop(roundNum)