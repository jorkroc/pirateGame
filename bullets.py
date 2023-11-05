import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255,255,255))
        self.position=(pygame.Vector2(1280/2, 720/2))
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 720/2)
        self.life=0
        print("heyo")

    def update(self):
        self.rect.x+=5
        self.position.x+=5
        self.life+=1
        print(self.life)

    def shiftPositionX(self, shift):
        self.position.x += shift
        self.rect.center=self.position
    
    def shiftPositionY(self, shift):
        self.position.y += shift
        self.rect.center=self.position
