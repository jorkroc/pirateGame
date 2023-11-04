import pygame
import random
from ship import Ship
from Island import Island
from playership import PlayerShip
from home import Home
from bullets import Bullet
import bullets

pygame.init()

screen_width = 1280
screen_height = 720
map_width = 1000
map_height = 1000
title = "Pirate Game"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True
dt = 0

shift = 1
velocity = [0,0]

all_sprites_list = pygame.sprite.Group() 
bulletList = []
moving_objects = []

player = PlayerShip(screen.get_width()/2, screen.get_height()/2)
home = Home()

all_sprites_list.add(home)
moving_objects.append(home)

all_sprites_list.add(player)
for i in range(50):
    island = Island(pygame.Vector2(random.randint(-map_width//10,map_width//10)*10, random.randint(-map_height//10,map_height//10))*10, "yellow", random.randint(10, 100))
    all_sprites_list.add(island)
    moving_objects.append(island) 
    








def bulletFire():
    global bulletList
    global moving_objects
    global all_sprites_list
    bullet = Bullet(0,0)
    bulletList.append(bullet)
    moving_objects.append(bullet)
    all_sprites_list.add(bullet)

def bulletUpdate():
    global bulletList
    for bullet in bulletList:
        bullet.update()
        count=0
        if bullet.life>100:
            count+=1
            bullet.kill()
            del bullet
        bulletList=bulletList[count:]

    
    
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    pygame.draw.circle(screen, island.color, island.position, 30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        velocity[1] += shift
    if keys[pygame.K_s]:
        velocity[1] -= shift
    if keys[pygame.K_a]:
        velocity[0] += shift
    if keys[pygame.K_d]:
        velocity[0] -= shift
    
    
    if keys[pygame.K_SPACE]:
        bulletFire()

    bulletUpdate()
        
        
    

    for sprite in moving_objects:
        sprite.shiftPositionX(velocity[0])
        sprite.shiftPositionY(velocity[1])

    velocity[0] *= 0.9
    velocity[1] *= 0.9
    
    all_sprites_list.draw(screen) 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()