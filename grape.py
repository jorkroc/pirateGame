from ship import Ship

class Grape(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("purple", 40, 40, xpos, ypos, speed)
        self.type=1
        self.xpos=xpos
        self.ypos=ypos

    def attack(self, player):
        pass
        #Implement