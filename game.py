import time 
import snake
import ledboard
import buzzer
import direction
import market
import apple
from machine import Pin

class Game :
    def __init__(self):
        self.direction = direction.Direction()
        self.snake = snake.Snake(self.direction)
        self.ledboard = ledboard.LEDBoard()
        self.apple = apple.Apple()
        self.buzzer = buzzer.Buzzer()
        self.market = market.Market(self.direction)


    def GameOver(self):
        # self.ledboard.GOScreeen()
        choice = self.market.marketChoice()
        if choice == "reinit" :
            self.reInitGame()
        else :
            self.restartGame()
            
    def reInitGame(self) :
        self.direction = direction.Direction()
        self.snake = snake.Snake(self.direction)
        self.ledboard = ledboard.LEDBoard()
        self.apple = apple.Apple() 
        self.market = market.Market(self.direction)
        print("Réinitialisation...")
        self.gameLoop()     
            
    def restartGame(self) :
        self.direction = direction.Direction()
        self.snake = snake.Snake(self.direction)
        self.ledboard = ledboard.LEDBoard()
        self.apple = apple.Apple() 
        print("Lancement de la partie...")
        self.gameLoop()

    def addpoint(self) :
        if self.apple.golden :
            self.market.coins += (self.market.upgrades.appleValue + 1) * 3
        else :
            self.market.coins += (self.market.upgrades.appleValue + 1) 

    def gameLoop(self) :
        self.buzzer.start()
        while True :

            # Clear et dessine le jeu
            self.ledboard.clear(self.apple.apple_pos)
            self.ledboard.drawapple(self.apple)
            self.ledboard.drawsnake(self.snake.Snake_pos)

            # Vérifie si GO
            if self.snake.verifycolision() :
                self.ledboard.drawCollision(self.snake.getHeadPos())
                if not self.market.upgrades.reborn :
                    self.GameOver()
                    break
                self.market.upgrades.reborn = False 

            # Vérifie si mange une pomme
            if self.apple.verify_apple(self.ledboard.grid[self.snake.Snake_pos[0][0]][self.snake.Snake_pos[0][1]]) :
                self.apple.apple_pos = self.apple.generate_apple(self.snake.Snake_pos, self.market.upgrades.goldDrop)
                self.addpoint()
                self.ledboard.drawapple(self.apple)
                self.snake.justAte = True
                
            # Change la position du snake
            self.snake.update_position()

            time.sleep(0.3)
