import pygame
import random
from ship import Ship
from Island import Island
from playership import PlayerShip
from home import Home

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
moving_objects = []

player = PlayerShip(screen.get_width()/2, screen.get_height()/2)
home = Home()

all_sprites_list.add(home)
moving_objects.append(home)

all_sprites_list.add(player)

for i in range(50):
    randX = random.randint(-map_width//10, map_width//10)*10
    randY = random.randint(-map_width//10, map_width//10)*10
    position = pygame.Vector2(randX, randY)*10
    island = Island(position, "yellow", random.randint(10, 100))
    all_sprites_list.add(island)
    moving_objects.append(island) 

for i in range(50):
    randX = random.randint(-map_width//10, map_width//10)*10
    randY = random.randint(-map_width//10, map_width//10)*10
    enemy = Ship("orange", 40, 40, randX, randY)
    all_sprites_list.add(enemy)
    moving_objects.append(enemy)
    
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

    for sprite in moving_objects:
        sprite.shiftPositionX(velocity[0])
        sprite.shiftPositionY(velocity[1])
        if pygame.sprite.collide_rect(player, sprite):
            print("collision")

    velocity[0] *= 0.9
    velocity[1] *= 0.9
    
    all_sprites_list.draw(screen) 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()