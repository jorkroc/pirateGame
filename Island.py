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
        
        if (random.randint(0, 1) == 1):
            self.image = pygame.image.load('images/island.png').convert_alpha()
        else:
            self.image = pygame.image.load('images/island_left.png').convert_alpha()

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

    def direction(self):
        return