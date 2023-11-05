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
import time
import numpy as np


pygame.init()

screen_width = 1280
screen_height = 720
map_width = 1000
map_height = 1000
title = "Pirate Game"

finalbossX = 100
finalbossY = 100

minimap_width = 100
minimap_height = 100
minimap = pygame.Surface((minimap_width, minimap_height))
minimap_rect = minimap.get_rect()
minimap_rect.topleft = (10, 10)
minimap_pos_x = (screen_width/2 * (minimap_width / screen_width))/0.1
minimap_pos_y = (screen_height/2 * (minimap_height / screen_height))/0.1

num_islands = 500
num_enemies = 10
enemy_speed = 5
enemy_range = 200

font_size = 20
font = pygame.font.SysFont('Courier New', font_size)
black = (0, 0, 0)
white = (255, 255, 255)
letters = {}
letters_nobg = {}
for i in range(32, 127):
    char = chr(i)
    letters[char] = font.render(char, False, black, white)
    letters_nobg[char] = font.render(char, False, black)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
running = True
dt = 0
bought = False

shift = 1
velocity = [0,0]

all_sprites_list = pygame.sprite.Group()
bulletList = []
moving_objects = []

player = PlayerShip(screen.get_width()/2, screen.get_height()/2)
home = Home()
player.health = 100

all_sprites_list.add(home)
moving_objects.append(home)

for j in range (8):
    for i in range(-100, 100):
        x = 80*i
        w = 80*j
        border1 = Island(pygame.Vector2(x, -6500-w), "black", 0)
        border2 = Island(pygame.Vector2(x, 7000+w), "black", 0)
        all_sprites_list.add(border1)
        moving_objects.append(border1)
        all_sprites_list.add(border2)
        moving_objects.append(border2)

    for i in range(-100, 100):
        y = 80*i
        border1 = Island(pygame.Vector2(-6000-w, y), "black", 0)
        border2 = Island(pygame.Vector2(7500+w, y), "black", 0)
        all_sprites_list.add(border1)
        moving_objects.append(border1)
        all_sprites_list.add(border2)
        moving_objects.append(border2)

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

enemyGroup=pygame.sprite.Group()
for enemy in enemies:
    enemyGroup.add(enemy)
finalboss = FinalBoss(finalbossX, finalbossY, enemy_speed)
all_sprites_list.add(finalboss)
moving_objects.append(finalboss)
enemies.append(finalboss)


ship_types = [Grape, Ship, Rammer, Jugger, FinalBoss]

def writeToScreen(screen, text, font_size, x, y, bg=True):
    for i, char in enumerate(text):
        if bg:
            screen.blit(letters[char], (x + i * font_size / 2, y))
        else:
            screen.blit(letters_nobg[char], (x + i * font_size / 2, y))

def parseOption(option, player):
    if option != 0:
        player.gold -= 1
    if option == 1:
        player.max_health += 1
    elif option == 2:
        player.speed += 1
    elif option == 3:
        player.bullet_speed += 1
    elif option == 4:
        player.rate_of_fire += 1
    elif option == 5:
        player.damage += 1
    elif option == 6:
        player.bullet_range += 1
    

def drawUpgradeMenu(screen, font_size):
    w, h = 600, 600
    sw, sh = screen.get_width(), screen.get_height()
    tlx, tly = (sw - w) / 2, (sh - h) / 2
    bg = pygame.Surface([w, h])
    bg.set_alpha(128)
    bg.fill((255, 255, 255))
    screen.blit(bg, (tlx, tly))

    bhx, bhy, pad, pad2 = 200, 200, 15, 5
    stats = ["Max Health", "Speed", "Bullet Speed", "Rate of Fire", "Damage", "Bullet Range"]
    for dis, stat in enumerate(stats):
        bhtext = "Increase {}".format(stat)
        bhw, bhh = len(bhtext) * font_size / 2, font_size
        bhbut = pygame.Surface([bhw + pad * 2, bhh + pad * 2])
        bhbut.fill((128, 128, 128))
        bhbut.set_alpha(196)
        bhtlx = tlx + bhx
        bhtly = tly + bhy + dis * (font_size + pad * 2 + pad2)
        screen.blit(bhbut, (bhtlx, bhtly))
        writeToScreen(screen, bhtext, font_size, bhtlx + pad, bhtly + pad, False) 

    if pygame.mouse.get_pressed()[0]:
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]
        for i, stat in enumerate(stats):
            bhtext = "Increase {}".format(stat)
            bhw, bhh = len(bhtext) * font_size / 2, font_size
            if tlx + bhx <= mx <= tlx + bhx + bhw + 2 * pad and tly + bhy <= my <= tly + bhy + i * (font_size + pad * 2 + pad2) + bhh + pad * 2:
                return i + 1

    return 0

def truncate(x, d=2):
    y = x * 10**d
    yi = (int)(y)
    y = yi if y - yi < 0.5 else yi + 1
    res = y / 10**d
    resi = (int)(res)
    if (int)(res) == res:
        return resi
    return res

# PLAYER HAS TO BE THE LAST ADDED
all_sprites_list.add(player)

lastFire=-1
def bulletFire():
    global lastFire
    newTime=time.time()
    elapsed=newTime-lastFire
    if elapsed>1:
        lastFire=newTime
        global bulletList
        global moving_objects
        global all_sprites_list
        bullet = Bullet(5, True, 5,0)
        bulletList.append(bullet)
        moving_objects.append(bullet)
        all_sprites_list.add(bullet)
def bulletUpdate():
    global bulletList
    global enemyGroup
    for bullet in bulletList:
        bullet.update()
        count=0
        if bullet.life>100:
            count+=1
            bullet.kill()
            del bullet
        elif bullet.active and bullet.friendly:
            for enemy in pygame.sprite.spritecollide(bullet, enemyGroup, False):
                #enemy.health-=bullet.damage
                print("heya")
                bullet.active=False
                bullet.kill()
                
        elif bullet.active and not bullet.friendly and collide_rect(player, bullet):
            player.health-=bullet.damage
            bullet.active=False
            bullet.kill()
        bulletList=bulletList[count:]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for sprite in moving_objects:
        if type(sprite) == Ship:
            sprite.speed = abs(sprite.speed) 

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

    touchingIsland = False

    at_home = False
    for sprite in moving_objects:
        sprite.shiftPositionX(velocity[0])
        sprite.shiftPositionY(velocity[1])

        if pygame.sprite.collide_rect(player, sprite):
            if type(sprite) in ship_types:
                sprite.shiftPositionX(-velocity[0])
                sprite.shiftPositionY(-velocity[1])
                sprite.speed *= -1
                if player.ramming and not sprite.ramming:
                    sprite.health -= 1
                elif not player.ramming and sprite.ramming:
                    player.health -= 1
            if type(sprite) == Island:
                for sprite in moving_objects:
                    sprite.shiftPositionX(-velocity[0])
                    sprite.shiftPositionY(-velocity[1])
                player.gold += 1
                touchingIsland = True
            if type(sprite) == Home:
                at_home = True

    for enemy in enemies:
        if math.hypot((enemy.xpos-player.xpos), (enemy.ypos-player.ypos)) <= enemy_range:
            #print("Chase")
            enemy.chase(player)
    

    velocity[0] *= 0.9
    velocity[1] *= 0.9

    if not (velocity[0]==0 and velocity[1]==0):
        if (velocity[0]==0):
            if velocity[1]>0:
                angle=90
            else:
                angle=-90
        elif velocity[0]<0:
            angle=np.degrees(np.arctan(-velocity[1]/velocity[0]))
        else:
            angle=np.degrees(np.arctan(-velocity[1]/velocity[0]))+180
        if angle<0:
            angle=(90-(angle*-1))+270
        angle=round(angle/45)%8
        player.updateDir(angle)

    screen.fill("blue")
    minimap.fill((255, 255, 255))

    all_sprites_list.draw(screen)

    #for minimap
    if (not touchingIsland):
        minimap_pos_x -= velocity[0] * (minimap_width / screen_width)
        minimap_pos_y -= velocity[1] * (minimap_width / screen_width)

    pygame.draw.rect(minimap, "black", pygame.Rect(0, 33, 25, 67))  
    pygame.draw.rect(minimap, "green", pygame.Rect(60, 0, 40, 50))
    pygame.draw.rect(minimap, "purple", pygame.Rect(40, 67, 60, 33))
    pygame.draw.rect(minimap, "grey", pygame.Rect(25, 10, 10, 10))

    pygame.draw.circle(minimap, "red", (int(0.1*(minimap_pos_x + (minimap_width / screen_width))), int(0.1*(minimap_pos_y - (minimap_height / screen_height)))), 5)
    screen.blit(minimap, minimap_rect) 
    if at_home:
        player.health = player.max_health
        option = drawUpgradeMenu(screen, font_size)
        if not bought:
            parseOption(option, player)
        
        if option == 0:
            bought = False
        else:
            bought = True
    

    # draw stats
    show_stats = ["gold", "health", "speed", "bullet speed", "rate of fire", "damage", "bullet range"]
    stat_map = {
        "gold":player.gold,
        "speed":player.speed,
        "bullet speed":player.bullet_speed,
        "rate of fire":player.rate_of_fire,
        "damage":player.damage,
        "bullet range":player.bullet_range
    }
    stat_x = screen_width - 250
    pad = 20
    dis = font_size + pad
    for i, stat in enumerate(show_stats):
        if stat == "health":
            writeToScreen(screen, "{}/{}".format(truncate(player.health), player.max_health), font_size, stat_x, dis * i + pad)
        else:
            writeToScreen(screen, "{}: {}".format(stat, stat_map[stat]), font_size, stat_x, dis * i + pad)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()