from machine import Pin
from machine import PWM
from time import sleep


class Buzzer: 
    def __init__(self):
        self.pwm = PWM(Pin(7, Pin.OUT))
        self.pwm.duty(0)
        
    def play(self, freq, wait):
        self.pwm.duty(200)
        self.pwm.freq(freq)
        sleep(wait)
        self.pwm.duty(0)
    
    def start(self) :
        # PART 1
        self.play(293, 0.15)
        self.play(293, 0.15)
        self.play(587, 0.3)
        self.play(440, 0.5)
        self.play(415, 0.3)
        self.play(391, 0.3)
        self.play(349, 0.3)
        self.play(293, 0.15)
        self.play(349, 0.15)
        self.play(391, 0.15)
        # PART 2
        self.play(261, 0.15)
        self.play(261, 0.15)
        self.play(587, 0.3)
        self.play(440, 0.5)
        self.play(415, 0.3)
        self.play(391, 0.3)
        self.play(349, 0.3)
        self.play(293, 0.15)
        self.play(349, 0.15)
        self.play(391, 0.15)
        # PART 3
        self.play(246, 0.15)
        self.play(246, 0.15)
        self.play(587, 0.3)
        self.play(440, 0.5)
        self.play(415, 0.3)
        self.play(391, 0.3)
        self.play(349, 0.3)
        self.play(293, 0.15)
        self.play(349, 0.15)
        self.play(391, 0.15)
        # PART 4
        self.play(233, 0.15)
        self.play(233, 0.15)
        self.play(587, 0.3)
        self.play(440, 0.5)
        self.play(415, 0.3)
        self.play(391, 0.3)
        self.play(349, 0.3)
        self.play(293, 0.15)
        self.play(349, 0.15)
        self.play(391, 0.15)
       
