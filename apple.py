import random
import ledboard

class Apple :
    def __init__(self):
        self.apple_pos = self.generate_apple([[0,0]], 0)
        self.golden = False
    
    def generate_apple(self, snake, goldDrop) :
        self.golden = False
        randgold = random.randint(1, 10)
        if randgold <=  goldDrop :
            self.golden = True
        grid = [[0,1,2,3,4,5,6,7], [15,14,13,12,11,10,9,8], [16,17,18,19,20,21,22,23], [31,30,29,28,27,26,25,24], [32,33,34,35,36,37,38,39], [47,46,45,44,43,42,41,40], [48,49,50,51,52,53,54,55], [63,62,61,60,59,58,57,56]]
        apple = random.randint(0,63)
        for i in range (0, len(snake)) :
            if grid[snake[i][0]][snake[i][1]] == apple :
                apple = random.randint(0,63)
                i = 0
        return apple

    def verify_apple(self, snake) :
        if snake == self.apple_pos :
            return True
