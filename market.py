import upgrade
from machine import Pin
import time 
class Market :
    def __init__(self, dir):
        self.coins = 0
        self.upgrades = upgrade.Upgrades()
        self.restart = Pin(6, Pin.IN, Pin.PULL_UP)
        self.direction = dir

    def printMarket(self):
        print("\n" * 50)
        print("\n" + "=" * 60)
        print("                      MARCHÉ DES AMÉLIORATIONS                      ")
        print("                         Budget : " + str(self.coins) + "                         ")
        print("=" * 60 + "\n")

        # Haut
        print(" " * 37 + "↑")
        print(" " * 20 + "Augmenter la valeur des pommes")
        if self.upgrades.appleValue < 9:
            prix = self.upgrades.appleValuePrices[self.upgrades.appleValue]
            actuel = self.upgrades.appleValue + 1
            print(" " * 20 + "Prix : " + str(prix) + "  (actuel : " + str(actuel) + ")\n")
        else:
            print(" " * 20 + "(maximum atteint)\n")

        # Gauche et droite
        print("← Acheter une deuxième vie" + " " * 20 + "Plus de pommes dorées →")

        if self.upgrades.goldDrop == 10 and self.upgrades.reborn:
            print("Déjà acheté !" + " " * 35 + "(maximum atteint)")
        elif self.upgrades.goldDrop == 10:
            prix = self.upgrades.rebornPrice
            print("Prix : " + str(prix) + " " * 35 + "(maximum atteint)\n")
        elif self.upgrades.reborn:
            prix = self.upgrades.goldDropPrice[self.upgrades.goldDrop]
            taux = self.upgrades.goldDrop * 10
            print("Déjà acheté !" + " " * 35 + "Prix : " + str(prix) + " (Taux actuel : " + str(taux) + "%)\n")
        else:
            prixReborn = self.upgrades.rebornPrice
            prix = self.upgrades.goldDropPrice[self.upgrades.goldDrop]
            taux = self.upgrades.goldDrop * 10
            print("Prix :" + str(prixReborn) + " " * 35 + "Prix : " + str(prix) + " (Taux actuel : " + str(taux) + "%)\n")

        # Bas
        print(" " * 27 + "Relancer une partie")
        print(" " * 37 + "↓\n")

        print("-" * 60)
        print("Utilisez le joystick pour choisir une amélioration, cliquez dessus pour réinitialiser la partie.")


    def marketChoice(self) :
        self.printMarket()
        while True :
            if self.direction.getDirection() == "UP" and self.upgrades.appleValue < 9:
                if self.coins < self.upgrades.appleValuePrices[self.upgrades.appleValue] :
                    print("Tu n'as pas assez de pommes ! Rejoue pour en récolter")
                    time.sleep(1)
                else :
                    self.coins -= self.upgrades.appleValuePrices[self.upgrades.appleValue]
                    self.upgrades.upAppleValue()   
                    self.printMarket()
                
            if self.direction.getDirection() == "RIGHT" and self.upgrades.goldDrop < 10 :
                if self.coins < self.upgrades.goldDropPrice[self.upgrades.goldDrop] :
                    print("Tu n'as pas assez de pommes ! Rejoue pour en récolter")
                    time.sleep(1)
                else :
                    self.coins -= self.upgrades.goldDropPrice[self.upgrades.goldDrop]
                    self.upgrades.upGoldDrop()  
                    self.printMarket()

            if self.direction.getDirection() == "LEFT" and self.upgrades.reborn == False:
                if self.coins < self.upgrades.rebornPrice:
                    print("Tu n'as pas assez de pommes ! Rejoue pour en récolter")
                    time.sleep(1)
                else :
                    self.coins -= self.upgrades.rebornPrice
                    self.upgrades.buyReborn() 
                    self.printMarket()

            if self.direction.getDirection() == "DOWN" :
                return "restart"
            
            if self.restart.value() == 0 :
                return "reinit"
