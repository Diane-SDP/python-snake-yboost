import machine

class Buttons :
    def __init__(self, npin):
        self.npin = npin
        self.pin = self.createButton()

    def createButton(self) :
        return machine.Pin(self.npin, mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)
    
    def triggerPin(self, snake) :
        self.pin.irq(trigger = machine.Pin.IRQ_FALLING, handler = snake.change_direction)
