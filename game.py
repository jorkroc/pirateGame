import pygame
from ship import Ship
from Island import Island

pygame.init()

screen_width = 1280
screen_height = 720
title = "Pirate Game"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True
dt = 0
shift = 10

all_sprites_list = pygame.sprite.Group() 

player = Ship("red", 40, 40)
#         Up     Down   Left   Right
moving = [False, False, False, False]

all_sprites_list.add(player) 
island = Island(pygame.Vector2(50, 50), "yellow", 100)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    pygame.draw.circle(screen, island.color, island.position, 30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        moving[0] = True
        island.shiftPositionY(shift)
    if keys[pygame.K_s]:
        moving[1] = True
        island.shiftPositionY(-shift)
    if keys[pygame.K_a]:
        moving[2] = True
        island.shiftPositionX(shift)
    if keys[pygame.K_d]:
        moving[3] = True
        island.shiftPositionX(-shift)

    all_sprites_list.draw(screen) 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()