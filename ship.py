import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, color, width, height, xpos, ypos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.rect.x = xpos - width / 2
        self.rect.y = ypos - height / 2
        self.rotation = 0

    def shiftPositionX(self, shift):
        self.xpos += shift
        self.rect.x = self.xpos - self.width / 2
    
    def shiftPositionY(self,shift):
        self.ypos += shift
        self.rect.y = self.ypos - self.height / 2
