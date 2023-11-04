from ship import Ship

class Rammer(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("black", 40, 40, xpos, ypos, speed)

    def attack(self, player):
        pass
        #Implement
