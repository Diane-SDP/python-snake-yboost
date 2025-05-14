from machine import ADC, Pin

class Direction :
    def __init__(self):
        self.xAxis = ADC(Pin(4, Pin.IN))
        self.xAxis.atten(self.xAxis.ATTN_11DB)
        self.yAxis = ADC(Pin(5, Pin.IN))
        self.yAxis.atten(self.yAxis.ATTN_11DB)
        self.dirSTR = "UP"

    def getX(self) :
        return self.xAxis.read()
    
    def getY(self) :
        return self.yAxis.read()

    def get_new_head_pos(self, new_head_pos) :
        if self.dirSTR == "UP" :    
            if new_head_pos[1] == 0 :
                new_head_pos[1] = 7
            else :
                new_head_pos[1] -= 1
        if self.dirSTR == "DOWN" :    
            if new_head_pos[1] == 7 :
                new_head_pos[1] = 0
            else :
                new_head_pos[1] += 1
        if self.dirSTR == "LEFT" :    
            if new_head_pos[0] == 0 :
                new_head_pos[0] = 7
            else :
                new_head_pos[0] -= 1
        if self.dirSTR == "RIGHT" :    
            if new_head_pos[0] == 7 :
                new_head_pos[0] = 0
            else :
                new_head_pos[0] += 1
        return new_head_pos
    
    def change_direction(self) :
        if self.getX() > 3800 and self.dirSTR != "UP" :
            self.dirSTR = "DOWN"
        elif self.getY() > 4000 and self.dirSTR != "RIGHT"  :
            self.dirSTR = "LEFT"
        elif self.getX() < 70 and self.dirSTR != "DOWN" :
            self.dirSTR = "UP"
        elif self.getY() < 70 and self.dirSTR != "LEFT" :
            self.dirSTR = "RIGHT"

    def getDirection(self) :
        if self.getX() > 4000 :
            return "DOWN"
        if self.getY() > 4000 :
            return "LEFT"
        if self.getX() < 70 :
            return "UP"
        if self.getY() < 70 :
            return "RIGHT"