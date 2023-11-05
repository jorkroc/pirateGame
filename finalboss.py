from ship import Ship
import pygame

class FinalBoss(Ship):
    def __init__(self, xpos, ypos, speed):
        super().__init__("white", 100, 100, xpos, ypos, speed)
        self.type=4
        self.xpos=xpos
        self.ypos=ypos
        self.health=50
        self.image = pygame.image.load('images/final_boss.png').convert_alpha()
    def attack(self, player):
        pass
        #Implement
