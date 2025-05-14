import direction 

class Snake :

    def __init__(self, dir):
        self.Snake_pos = [[0,0]]
        self.justAte = False
        self.direction = dir
    
    def update_position(self) :
        self.direction.change_direction()
        head_pos = [self.Snake_pos[0][0], self.Snake_pos[0][1]] 
        head_pos = self.direction.get_new_head_pos(head_pos)
        self.movebody(head_pos)

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

    def getHeadPos(self) :
        return self.Snake_pos[0]