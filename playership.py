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
        super().__init__("red", 40, 40, xpos, ypos)
        self.territory = Territory.SAFE
        self.xpos=xpos
        self.ypos=ypos

        self.damage=5
        self.health=20
        self.speed=1
        self.projSpeed=1
        self.ROF=1
        self.hullDamage=0
    
    def updateTerr(self,width,height):
        if width/4>self.xpos and height/3<self.ypos:
            self.territory=Territory.RAMMER
        elif 2*width/5<self.xpos and 2*height/3<self.ypos:
            self.territory=Territory.GRAPE
        elif 3*width/5<self.xpos and height/2>self.ypos:
            self.territory=Territory.JUGGERNAUT
        else:
            self.territory=Territory.ROYAL

