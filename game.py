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
shift = 500

all_sprites_list = pygame.sprite.Group()
playerGroup = pygame.sprite.GroupSingle() 

player = Ship("red", 40, 40, screen_width / 2, screen_height / 2)
playerGroup.add(player)
#         Up     Down   Left   Right
moving = [False, False, False, False]

island = Island(pygame.Vector2(50, 50), "yellow", 100)
all_sprites_list.add(island)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    moving = [False, False, False, False]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        moving[0] = True
    if keys[pygame.K_s]:
        moving[1] = True
    if keys[pygame.K_a]:
        moving[2] = True
    if keys[pygame.K_d]:
        moving[3] = True
    
    displacement = pygame.Vector2(moving[2] - moving[3], moving[0] - moving[1])
    #pygame.math.Vector2.normalize_ip(displacement)
    island.shiftPositionX(displacement.x * shift * dt)
    island.shiftPositionY(displacement.y * shift * dt)


    playerGroup.draw(screen)
    all_sprites_list.draw(screen) 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()