from ship import Ship

class FinalBoss(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("white", 100, 100, xpos, ypos, speed)

    def attack(self, player):
        pass
        #Implement
