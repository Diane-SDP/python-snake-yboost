import neopixel
import machine
import time

class LEDBoard :
    def __init__(self):
        self.grid = [[0,1,2,3,4,5,6,7], [15,14,13,12,11,10,9,8], [16,17,18,19,20,21,22,23], [31,30,29,28,27,26,25,24], [32,33,34,35,36,37,38,39], [47,46,45,44,43,42,41,40], [48,49,50,51,52,53,54,55], [63,62,61,60,59,58,57,56]]
        self.np = neopixel.NeoPixel(machine.Pin(3), 64)

    def clear(self, apple) :
        for i in range (64) :
            self.np[i] = (0,0,0)    
                
    def drawapple(self, apple) :
        if apple.golden :
            self.np[apple.apple_pos] = (8,5,0)
        else :
            self.np[apple.apple_pos] = (0,5,0)
        self.np.write()

    def drawsnake(self, snakepos) :
        for i in range(0, len(snakepos)) :
                if i%2 == 0 :
                    self.np[self.grid[snakepos[i][0]][snakepos[i][1]]] = (10, 1, 1)
                else :
                    self.np[self.grid[snakepos[i][0]][snakepos[i][1]]] = (10, 0, 0)
        self.np[self.grid[snakepos[0][0]][snakepos[0][1]]] = (10, 5, 5)
        self.np.write()

    def GOScreeen(self): 
        n = self.np.n
        for i in range(3 * n):
            for j in range(n):
                self.np[j] = (0, 0, 0)
            self.np[i % n] = (5, 5, 5)
            self.np.write()
            time.sleep_ms(25)
        self.np.write()

    def drawCollision(self, headPos) :
        for i in range(4):
            self.np[self.grid[headPos[0]][headPos[1]]] = (20, 0, 0)
            self.np.write()
            time.sleep_ms(200)
            self.np[self.grid[headPos[0]][headPos[1]]] = (10, 5, 5)
            self.np.write()
            time.sleep_ms(200)