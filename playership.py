import ship

class PlayerShip(ship.Ship):
    def __init__(self, xpos, ypos):
        super().__init__("red", 40, 40, xpos, ypos)
