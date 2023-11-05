import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, color, width, height, xpos, ypos, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.ramming = True
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.rect.x = xpos - width / 2
        self.rect.y = ypos - height / 2
        self.health = 20
        self.speed = 0
        self.bullet_speed = 0
        self.rate_of_fire = 0
        self.damage = 0
        self.bullet_range = 1
        self.direction = 0

    def shiftPositionX(self, shift):
        self.xpos += shift
        self.rect.x = self.xpos - self.width / 2
    
    def shiftPositionY(self,shift):
        self.ypos += shift
        self.rect.y = self.ypos - self.height / 2

    def chase(self, sprite):
        dx = sprite.xpos - self.xpos
        dy = sprite.ypos - self.ypos
        self.shiftPositionX(dx*self.speed/1000)
        self.shiftPositionY(dy*self.speed/1000)

    def attack(self, sprite):
        pass
        #Implement