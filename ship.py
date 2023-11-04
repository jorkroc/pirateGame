import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(400, 400)
    
    def draw(screen):
        screen.blit(self.image, (400, 400))


