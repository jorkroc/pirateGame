import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = pygame.Vector2(x_pos, y_pos)

