import pygame
from ship import Ship
from playership import PlayerShip
from Island import Island
from math import sqrt

pygame.init()

screen_width = 1280
screen_height = 720
title = "Pirate Game"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True
dt = 0

shift = 1
velocity = [0,0]

all_sprites_list = pygame.sprite.Group() 

player = PlayerShip(screen_width / 2, screen_height / 2)

all_sprites_list.add(player)
island = Island(pygame.Vector2(50, 50), "yellow", 100)
all_sprites_list.add(island)

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

    island.shiftPositionX(velocity[0])
    island.shiftPositionY(velocity[1])

    velocity[0] *= 0.9
    velocity[1] *= 0.9
    
    all_sprites_list.draw(screen) 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()