import time 
import snake
import ledboard
import buzzer
import apple
from machine import Pin

class Game :
    def __init__(self):
        self.score = 0
        self.snake = snake.Snake()
        self.ledboard = ledboard.LEDBoard()
        self.apple = apple.Apple()
        self.restart = Pin(6, Pin.IN, Pin.PULL_UP)
        self.buzzer = buzzer.Buzzer()


    def GameOver(self):
        print("Ton score :", self.score)
        n = self.ledboard.np.n
        for i in range(4 * n):
            for j in range(n):
                self.ledboard.np[j] = (0, 0, 0)
            self.ledboard.np[i % n] = (5, 5, 5)
            self.ledboard.np.write()
            time.sleep_ms(25)
        self.ledboard.np.write()
        while True :
            if self.restart.value() == 0 :
                self.restartGame()
            time.sleep(0.3)
            
    def restartGame(self) :
        self.score = 0
        self.snake = snake.Snake()
        self.ledboard = ledboard.LEDBoard()
        self.apple = apple.Apple() 
        print("je restart")
        self.gameLoop()       

    def addpoint(self) :
        self.score += 1

    def gameLoop(self) :
        self.buzzer.start()
        while True :

            # Clear et dessine le jeu
            self.ledboard.clear(self.apple.apple_pos)
            self.ledboard.drawapple(self.apple.apple_pos)
            self.ledboard.drawsnake(self.snake.Snake_pos)

            # Vérifie si GO
            if self.snake.verifycolision() :
                self.GameOver()
                break

            # Vérifie si mange une pomme
            if self.apple.verify_apple(self.ledboard.grid[self.snake.Snake_pos[0][0]][self.snake.Snake_pos[0][1]], self.apple.apple_pos) :
                self.addpoint()
                self.ledboard.drawapple(self.apple.apple_pos)
                self.snake.justAte = True
                
            # Change la position du snake
            self.snake.update_position()

            time.sleep(0.3)
