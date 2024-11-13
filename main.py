import neopixel
import time
import machine
import random
import Snake

class Snake :
    def __init__(self):
        self.Snake_pos = [[0,0]]
        self.Direction = "LEFT"
    
    def change_direction(self,button) :
        if button == buttonRIGHT :
            self.Direction = "RIGHT"
        elif button == buttonDOWN :
            self.Direction = "DOWN"
        elif button == buttonLEFT :
            self.Direction = "LEFT"
        elif button == buttonUP :
            self.Direction = "UP"
        else : 
            print("problème de Direction coco")
    
    def update_position(self) :
        if self.Direction == "UP" :    
            if self.Snake_pos[0][1] == 0 :
                self.Snake_pos[0][1] = 7
            else :
                self.Snake_pos[0][1] -= 1
        if self.Direction == "DOWN" :    
            if self.Snake_pos[0][1] == 7 :
                self.Snake_pos[0][1] = 0
            else :
                self.Snake_pos[0][1] += 1
        if self.Direction == "LEFT" :    
            if self.Snake_pos[0][0] == 0 :
                self.Snake_pos[0][0] = 7
            else :
                self.Snake_pos[0][0] -= 1
        if self.Direction == "RIGHT" :    
            if self.Snake_pos[0][0] == 7 :
                self.Snake_pos[0][0] = 0
            else :
                self.Snake_pos[0][0] += 1


global grid
grid = [[0,1,2,3,4,5,6,7], [15,14,13,12,11,10,9,8], [16,17,18,19,20,21,22,23], [31,30,29,28,27,26,25,24], [32,33,34,35,36,37,38,39], [47,46,45,44,43,42,41,40], [48,49,50,51,52,53,54,55], [63,62,61,60,59,58,57,56]]
np = neopixel.NeoPixel(machine.Pin(3), 64)
buttonLEFT = machine.Pin(4, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
buttonRIGHT = machine.Pin(5, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
buttonDOWN = machine.Pin(6, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
buttonUP = machine.Pin(7, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
score = 0

def generate_apple() :
    apple = random.randint(0,63)
    while apple == grid[snake.Snake_pos[0][0]][snake.Snake_pos[0][1]] :
        apple = random.randint(0,63)
    np[apple] = (0,5,0)
    np.write()
    return apple

def verify_apple(snake, apple) :
    global score
    if snake == apple :
        score += 1
        return True


snake = Snake()
print(snake.Snake_pos, snake.Direction)
global apple_pos
apple_pos = generate_apple()
buttonLEFT.irq(trigger = machine.Pin.IRQ_FALLING, handler = snake.change_direction)
buttonRIGHT.irq(trigger = machine.Pin.IRQ_FALLING, handler = snake.change_direction)
buttonDOWN.irq(trigger = machine.Pin.IRQ_FALLING, handler = snake.change_direction)
buttonUP.irq(trigger = machine.Pin.IRQ_FALLING, handler = snake.change_direction)
        
def clear() :
    for i in range (64) :
        if (i != apple_pos) :
            np[i] = (0,0,0)

def win():
    n = np.n
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (5, 5, 5)
        np.write()
        time.sleep_ms(25)
    np.write()



while True :
    clear()
    if score == 3 :
        win()
        break
    for i in range (len(snake.Snake_pos)) :
        np[grid[snake.Snake_pos[0][0]][snake.Snake_pos[0][1]]] = (5, 0, 0)
    np.write()
    if verify_apple(grid[snake.Snake_pos[0][0]][snake.Snake_pos[0][1]], apple_pos) :
        apple_pos = generate_apple()
    snake.update_position()
    time.sleep(0.3)




