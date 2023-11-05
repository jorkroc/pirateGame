import pygame
import random
import math
from ship import Ship
from Island import Island
from playership import PlayerShip
from home import Home
from bullets import Bullet
from grape import Grape
from jugger import Jugger
from rammer import Rammer
from finalboss import FinalBoss

pygame.init()

screen_width = 1280
screen_height = 720
map_width = 1000
map_height = 1000
title = "Pirate Game"

finalbossX = 100
finalbossY = 100

minimap_width = 150
minimap_height = 100
minimap = pygame.Surface((minimap_width, minimap_height))
minimap_rect = minimap.get_rect()
minimap_rect.topleft = (10, 10)
minimap_pos_x = (screen_width/2 * (minimap_width / screen_width))/0.1
minimap_pos_y = (screen_height/2 * (minimap_width / screen_width))/0.1

num_islands = 50
num_enemies = 10
enemy_speed = 5
enemy_range = 200

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
player.health = 100

all_sprites_list.add(home)
moving_objects.append(home)

for i in range(num_islands):
    randX = random.randint(-map_width//10, map_width//10)*10
    randY = random.randint(-map_width//10, map_width//10)*10
    position = pygame.Vector2(randX, randY)*10
    island = Island(position, "yellow", random.randint(10, 100))
    while pygame.sprite.collide_rect(home, island) or pygame.sprite.collide_rect(player, island):
        randX = random.randint(-map_width//10, map_width//10)*10
        randY = random.randint(-map_width//10, map_width//10)*10
        position = pygame.Vector2(randX, randY)*10
        island = Island(position, "yellow", random.randint(10, 100))
    all_sprites_list.add(island)
    moving_objects.append(island) 

enemies = []
for i in range(num_enemies%4):
    randX = random.randint(-map_width//10, map_width//10)*10
    randY = random.randint(-map_width//10, map_width//10)*10
    enemy = Ship("orange", 40, 40, randX, randY, enemy_speed)
    while pygame.sprite.collide_rect(home, enemy) or pygame.sprite.collide_rect(player,enemy):
        randX = random.randint(-map_width//10, map_width//10)*10
        randY = random.randint(-map_width//10, map_width//10)*10
        enemy = Ship("orange", 40, 40, randX, randY, enemy_speed)
    all_sprites_list.add(enemy)
    moving_objects.append(enemy)
    enemies.append(enemy)
    
for i in range(num_enemies//4):
    randX = random.randint(-map_width//10, map_width//10)*10
    randY = random.randint(-map_width//10, map_width//10)*10
    enemy = Jugger(randX, randY, enemy_speed) 
    while pygame.sprite.collide_rect(home, enemy) or pygame.sprite.collide_rect(player,enemy):
        randX = random.randint(-map_width//10, map_width//10)*10
        randY = random.randint(-map_width//10, map_width//10)*10
        enemy = Jugger(randX, randY, enemy_speed) 
    all_sprites_list.add(enemy)
    moving_objects.append(enemy)
    enemies.append(enemy)

for i in range(num_enemies//4):
    randX = random.randint(-map_width//10, map_width//10)*10
    randY = random.randint(-map_width//10, map_width//10)*10
    enemy = Grape(randX, randY, enemy_speed) 
    while pygame.sprite.collide_rect(home, enemy) or pygame.sprite.collide_rect(player,enemy):
        randX = random.randint(-map_width//10, map_width//10)*10
        randY = random.randint(-map_width//10, map_width//10)*10
        enemy = Grape(randX, randY, enemy_speed) 
    all_sprites_list.add(enemy)
    moving_objects.append(enemy)
    enemies.append(enemy)

for i in range(num_enemies//4):
    randX = random.randint(-map_width//10, map_width//10)*10
    randY = random.randint(-map_width//10, map_width//10)*10
    enemy = Rammer(randX, randY, enemy_speed) 
    while pygame.sprite.collide_rect(home, enemy) or pygame.sprite.collide_rect(player,enemy):
        randX = random.randint(-map_width//10, map_width//10)*10
        randY = random.randint(-map_width//10, map_width//10)*10
        enemy = Rammer(randX, randY, enemy_speed) 
    all_sprites_list.add(enemy)
    moving_objects.append(enemy)
    enemies.append(enemy)

finalboss = FinalBoss(finalbossX, finalbossY, enemy_speed)
all_sprites_list.add(finalboss)
moving_objects.append(finalboss)
enemies.append(finalboss)

# PLAYER HAS TO BE THE LAST ADDED
all_sprites_list.add(player)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for sprite in moving_objects:
        try:
            sprite.speed = abs(sprite.speed) 
        except:
            pass

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
            sprite.shiftPositionX(-velocity[0])
            sprite.shiftPositionY(-velocity[1])
            sprite.speed *= -1
            # try:
            #     if player.health > sprite.health:
            #         print("collision")
            #     else:
            #         print("player dead")
            # except:
            #     print("nope")



    for enemy in enemies:
        if math.hypot((enemy.xpos-player.xpos), (enemy.ypos-player.ypos)) <= enemy_range:
            print("Chase")
            enemy.chase(player)

    velocity[0] *= 0.9
    velocity[1] *= 0.9

    screen.fill("blue")
    minimap.fill((255, 255, 255))  # Clear the minimap
    #self.position.x += shift
    #self.rect.center=self.position
    minimap_pos_x -= velocity[0] * (minimap_width / screen_width)
    minimap_pos_y -= velocity[1] * (minimap_width / screen_width)

    pygame.draw.circle(minimap, "red", (int(0.1*(minimap_pos_x + (minimap_width / screen_width))), int(0.1*(minimap_pos_y - (minimap_height / screen_height)))), 5)
    screen.blit(minimap, minimap_rect)
    
    all_sprites_list.draw(screen) 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()