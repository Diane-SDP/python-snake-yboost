import buttons

class Snake :
    def __init__(self):
        self.Snake_pos = [[0,0]]
        self.justAte = False
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
        if button == self.turnRIGHT.pin and self.Direction != "LEFT" :
            self.Direction = "RIGHT"
        elif button == self.turnDOWN.pin and self.Direction != "UP"  :
            self.Direction = "DOWN"
        elif button == self.turnLEFT.pin and self.Direction != "RIGHT" :
            self.Direction = "LEFT"
        elif button == self.turnUP.pin and self.Direction != "DOWN" :
            self.Direction = "UP"
    
    def update_position(self) :
        new_head_pos = [self.Snake_pos[0][0], self.Snake_pos[0][1]] 
        if self.Direction == "UP" :    
            if new_head_pos[1] == 0 :
                new_head_pos[1] = 7
            else :
                new_head_pos[1] -= 1
        if self.Direction == "DOWN" :    
            if new_head_pos[1] == 7 :
                new_head_pos[1] = 0
            else :
                new_head_pos[1] += 1
        if self.Direction == "LEFT" :    
            if new_head_pos[0] == 0 :
                new_head_pos[0] = 7
            else :
                new_head_pos[0] -= 1
        if self.Direction == "RIGHT" :    
            if new_head_pos[0] == 7 :
                new_head_pos[0] = 0
            else :
                new_head_pos[0] += 1
        self.movebody(new_head_pos)

    def movebody(self, head_pos) :
        self.Snake_pos.insert(0, head_pos)
        if not self.justAte :
            self.Snake_pos.pop()
        self.justAte = False    

    def verifycolision(self) :
        for elt in self.Snake_pos[1:] :
            if self.Snake_pos[0] == elt :
                return True
        return False
