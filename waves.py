import pygame
import random

class Waves(pygame.sprite.Sprite):

    def __init__(self, position, color):
        super().__init__()
        self.image = pygame.Surface([160,20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.position = position

        self.image = pygame.image.load('images/wave.png').convert_alpha()

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