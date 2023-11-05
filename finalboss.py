from ship import Ship

class FinalBoss(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("white", 100, 100, xpos, ypos, speed)
        self.type=4
        self.xpos=xpos
        self.ypos=ypos
        self.health=50
    def attack(self, player):
        pass
        #Implement
