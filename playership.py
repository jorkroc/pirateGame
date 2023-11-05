import ship
from enum import Enum
import pygame

class Territory(Enum):
    SAFE = 0
    ROYAL = 1
    RAMMER = 2
    GRAPE = 3
    JUGGERNAUT = 4

class PlayerShip(ship.Ship):
    def __init__(self, xpos, ypos):
        super().__init__("red", 40, 40, xpos, ypos, 0)
        self.health = 100
        self.max_health = 100
        self.ramming = False
        self.gold = 0
        self.territory = Territory.SAFE
        self.direction=0
        self.damage=1
        self.bullet_speed=5
        self.speed = 1
        self.image = pygame.image.load('images/boat.png').convert_alpha()

    def updateTerr(self,width,height):
        if width/4>self.xpos and height/3<self.ypos:
            self.territory=Territory.RAMMER
        elif 2*width/5<self.xpos and 2*height/3<self.ypos:
            self.territory=Territory.GRAPE
        elif 3*width/5<self.xpos and height/2>self.ypos:
            self.territory=Territory.JUGGERNAUT
        else:
            self.territory=Territory.ROYAL


    def updateDir(self,direction):
        self.direction=direction
        if (self.direction == 7) or (self.direction == 1) or (self.direction == 0):
            self.image = pygame.image.load('images/boat.png').convert_alpha()
        elif((self.direction == 3) or (self.direction == 4) or (self.direction == 5)):
            self.image = pygame.image.load('images/boat_left.png').convert_alpha()