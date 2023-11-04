from ship import Ship

class Grape(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("purple", 40, 40, xpos, ypos, speed)

    def attack(self, player):
        pass
        #Implement