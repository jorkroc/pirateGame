import pygame
from Ship import Ship

pygame.init()

screen_width = 1280
screen_height = 720
title = "Pirate Game"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True
dt = 0

player = Ship()
#         Up     Down   Left   Right
moving = [False, False, False, False]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    pygame.draw.circle(screen, "red", player.position, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        moving[0] = True
    if keys[pygame.K_s]:
        moving[1] = True
    if keys[pygame.K_a]:
        moving[2] = True
    if keys[pygame.K_d]:
        moving[3] = True

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()