import pygame
import random

class Island(pygame.sprite.Sprite):

    def __init__(self, position, color, treasure):
        super().__init__()
        self.image = pygame.Surface([80,80])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.position = position
        self.color = color
        self.treasure = treasure
        
        width=1000
        height=1000
        if (width/4>self.position.x and height/3<self.position.y) or \
            (2*width/5<self.position.x and 2*height/3<self.position.y) or \
            (3*width/5<self.position.x and height/2>self.position.y):
            self.treasure=random.randint(70, 170)

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition
        
    def shiftPositionX(self, shift):
        self.position.x += shift
        self.rect.center=self.position
    
    def shiftPositionY(self, shift):
        self.position.y += shift
        self.rect.center=self.position

    def getTreasure(self):
        return self.treasure
    
    def setTreasure(self, newTreasure):
        self.treasure = newTreasure