import pygame

class Endwall(pygame.sprite.Sprite):

    def __init__(self, position, color):
        super().__init__()
        self.image = pygame.Surface([80,80])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.position = position
        self.color = color

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