import ship
from enum import Enum

class Territory(Enum):
    SAFE = 0
    ROYAL = 1
    RAMMER = 2
    GRAPE = 3
    JUGGERNAUT = 4

class PlayerShip(ship.Ship):
    def __init__(self, xpos, ypos):
        super().__init__("red", 40, 40, xpos, ypos, 0)
        self.health = 100
        self.max_health = 100
        self.territory = Territory.SAFE
    
    def updateTerr(self,width,height):
        if width/4>self.xpos and height/3<self.ypos:
            self.territory=Territory.RAMMER
        elif 2*width/5<self.xpos and 2*height/3<self.ypos:
            self.territory=Territory.GRAPE
        elif 3*width/5<self.xpos and height/2>self.ypos:
            self.territory=Territory.JUGGERNAUT
        else:
            self.territory=Territory.ROYAL