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
    
    def updateTerr():
        self.territory= Territory.SAFE