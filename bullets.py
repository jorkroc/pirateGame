import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, friendly, damage, direction):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255,255,255))
        self.position=(pygame.Vector2(1280/2, 720/2))
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 720/2)
        self.life=0
        self.friendly=friendly
        xspeeds=[0,-1.414,-2,-1.414,0,1.414,2,1.414]
        yspeeds=[2,1.414,0,-1.414,-2,-1.414,0,1.414]
        self.xspeed=xspeeds[direction]*speed
        self.yspeed=yspeeds[direction]*speed
        self.damage=damage
        self.active=True
        self.direction=direction


    def update(self):
        self.rect.x+=self.xspeed
        self.position.x+=self.xspeed
        self.rect.y+=self.yspeed
        self.position.y-=self.yspeed
        self.life+=1


    def shiftPositionX(self, shift):
        self.position.x += shift
        self.rect.center=self.position
   
    def shiftPositionY(self, shift):
        self.position.y += shift
        self.rect.center=self.position


