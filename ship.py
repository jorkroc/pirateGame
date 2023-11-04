import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, color, width, height, xpos, ypos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xpos - width / 2
        self.rect.y = ypos - height / 2
        self.rotation = 0
