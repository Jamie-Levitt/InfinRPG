from RoundLogic import RoundManager

roundManager = RoundManager()

if __name__ == '__main__':
    roundManager.startUp()
    while True:
        roundManager.initNewRound()