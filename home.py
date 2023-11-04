import pygame

class Home(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([200, 200])
        self.image.fill("purple")
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 200
        self.rect.x = self.x
        self.rect.y = self.y
    def shiftPositionX(self, dx):
        self.x += dx
        self.rect.x = self.x
    def shiftPositionY(self, dy):
        self.y += dy
        self.rect.y = self.y

