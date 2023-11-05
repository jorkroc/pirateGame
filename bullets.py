import pygame
from numpy import arctan
from numpy import sin
from numpy import cos
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, friendly, damage, direction,xpos=0,ypos=0):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        if friendly:
            self.position=(pygame.Vector2(1280/2, 720/2))
            self.rect.center = (1280/2, 720/2)
        else:
            self.position=(pygame.Vector2(xpos, ypos))
            self.rect.center = (xpos, ypos)
        self.life=0
        self.friendly=friendly
        xspeeds=[0,-1.414,-2,-1.414,0,1.414,2,1.414]
        yspeeds=[2,1.414,0,-1.414,-2,-1.414,0,1.414]
        self.speed=speed
        if direction<8:
            self.xspeed=xspeeds[direction]*speed
            self.yspeed=yspeeds[direction]*speed
        elif direction==9:

            dx=1280/2-xpos
            dy=720/2-ypos
            self.xspeed=(dx/(((dx**2)+(dy**2))**0.5)*speed)+random.randint(-2,2)
            self.yspeed=(-dy/(((dx**2)+(dy**2))**0.5)*speed)+random.randint(-2,2)
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


