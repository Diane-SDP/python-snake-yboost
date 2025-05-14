class Upgrades :
    def __init__(self):
        self.goldDrop = 0
        self.appleValue = 0
        self.reborn = False

        self.rebornPrice = 200
        self.goldDropPrice = [25, 45, 70, 100, 135, 175, 220, 270, 325, 385]
        self.appleValuePrices = [10, 20, 35, 55, 80, 110, 145, 185, 230]

    def upGoldDrop(self) :
        self.goldDrop += 1

    def upAppleValue(self) :
        self.appleValue += 1

    def buyReborn(self) :
        self.reborn = True

