from ship import Ship

class Jugger(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("green", 40, 40, xpos, ypos, speed)
        self.type=2
        self.xpos=xpos
        self.ypos=ypos

    def attack(self, player):
        pass
        #Implement
        