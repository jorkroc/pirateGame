from ship import Ship

class Jugger(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("green", 40, 40, xpos, ypos, speed)

    def attack(self, player):
        pass
        #Implement
        