import buttons

class Snake :
    def __init__(self):
        self.Snake_pos = [[0,0]]
        self.Direction = "UP"
        self.turnLEFT = buttons.Buttons(4)
        self.turnRIGHT = buttons.Buttons(5)
        self.turnDOWN = buttons.Buttons(6)
        self.turnUP = buttons.Buttons(7)
        self.turnLEFT.triggerPin(self)
        self.turnRIGHT.triggerPin(self)
        self.turnDOWN.triggerPin(self)
        self.turnUP.triggerPin(self)
    
    def change_direction(self,button) :
        if button == self.turnRIGHT.pin :
            self.Direction = "RIGHT"
        elif button == self.turnDOWN.pin :
            self.Direction = "DOWN"
        elif button == self.turnLEFT.pin :
            self.Direction = "LEFT"
        elif button == self.turnUP.pin :
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

