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

gold = 0
font_size = 30
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

for i in range(20):
    x = 80*i
    border1 = Island(pygame.Vector2(x, 0), "black", 0)
    border2 = Island(pygame.Vector2(x, 4000), "black", 0)
    all_sprites_list.add(border1)
    moving_objects.append(border1)
    all_sprites_list.add(border2)
    moving_objects.append(border2)

for i in range(20):
    y = 80*i
    border1 = Island(pygame.Vector2(0, y), "black", 0)
    border2 = Island(pygame.Vector2(4000, y), "black", 0)
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

def drawUpgradeMenu(screen, font_size):
    w, h = 600, 600
    sw, sh = screen.get_width(), screen.get_height()
    tlx, tly = (sw - w) / 2, (sh - h) / 2
    bg = pygame.Surface([w, h])
    bg.set_alpha(128)
    bg.fill((255, 255, 255))

    bhx, bhy = 200, 200
    pad = 15
    buy_health_text = "Increase Max Health"
    bhw, bhh = len(buy_health_text) * font_size / 2, font_size
    buy_health_but = pygame.Surface([bhw + pad * 2, bhh + pad * 2])
    buy_health_but.fill((128, 128, 128))
    buy_health_but.set_alpha(196)

    screen.blit(bg, (tlx, tly))
    screen.blit(buy_health_but, (tlx + bhx - pad, tly + bhy - pad))
    writeToScreen(screen, buy_health_text, font_size, tlx + bhx, tly + bhy, False) 
    if pygame.mouse.get_pressed()[0]:
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]
        if tlx + bhx <= mx <= tlx + bhx + bhw and tly + bhy <= my <= tly + bhy + bhh:
           return 1
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
        bullet = Bullet(0,0, 5, True)
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
                gold += 1
                touchingIsland = True
            if type(sprite) == Home:
                at_home = True

    for enemy in enemies:
        if math.hypot((enemy.xpos-player.xpos), (enemy.ypos-player.ypos)) <= enemy_range:
            #print("Chase")
            enemy.chase(player)
    

    velocity[0] *= 0.9
    velocity[1] *= 0.9

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
    player.health -= 0.001
    if at_home:
        player.health = player.max_health
        option = drawUpgradeMenu(screen, font_size)
        if option == 1 and not bought:
            gold -= 1
            player.max_health += 1
        
        if option == 0:
            bought = False
        else:
            bought = True
    
    writeToScreen(screen, "Gold: {}".format(gold), font_size, screen_width - 250, 20)
    writeToScreen(screen, "{}/{}".format(truncate(player.health), player.max_health), font_size, screen_width - 250, 60)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
