import random

class Apple :
    def __init__(self):
        self.apple_pos = self.generate_apple(0)
    
    def generate_apple(self, snake) :
        apple = random.randint(0,63)
        while apple == snake:
            apple = random.randint(0,63)
        return apple

    def verify_apple(self, snake, apple) :
        if snake == apple :
            self.apple_pos = self.generate_apple(snake)
            return True
