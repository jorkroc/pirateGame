import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x=400
        self.rect.y=400

