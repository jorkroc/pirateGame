class Island:

    def __init__(self, position, color, treasure):
        self.position = position
        self.color = color
        self.treasure = treasure

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition

    def getTreasure(self):
        return self.treasure
    
    def setTreasure(self, newTreasure):
        self.treasure = newTreasure