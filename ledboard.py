import neopixel
import machine

class LEDBoard :
    def __init__(self):
        self.grid = [[0,1,2,3,4,5,6,7], [15,14,13,12,11,10,9,8], [16,17,18,19,20,21,22,23], [31,30,29,28,27,26,25,24], [32,33,34,35,36,37,38,39], [47,46,45,44,43,42,41,40], [48,49,50,51,52,53,54,55], [63,62,61,60,59,58,57,56]]
        self.np = neopixel.NeoPixel(machine.Pin(3), 64)

    def clear(self, apple) :
        for i in range (64) :
            if (i != apple) :
                self.np[i] = (0,0,0)
                
    def drawapple(self, apple) :
        self.np[apple] = (0,5,0)
        self.np.write()

    def drawsnake(self, snakepos) :
        for elt in snakepos :
                self.np[self.grid[elt[0]][elt[1]]] = (5, 0, 0)
        self.np.write()