import time 
import snake
import ledboard
import apple

class Game :
    def __init__(self):
        self.score = 0
        self.snake = snake.Snake()
        self.ledboard = ledboard.LEDBoard()
        self.apple = apple.Apple()

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
        

    def addpoint(self) :
        self.score += 1

    def gameLoop(self) :
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
