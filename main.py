import pygame
from player import *
from bullets import *
from math import *
from enemies import *
import random

# game setup
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Calisto MT', 40, bold=False)
my_font2 = pygame.font.SysFont('Calisto MT', 80, bold=False)
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("first game")
clock = pygame.time.Clock()
running = True
screen.fill((50, 50, 50))

# game variables

x = 1024 / 2
y = 768 / 2
rr = 25
spd = 5
bullets = []
enemybullets = []
enemies = []
player = Player(x, y, spd)
framecount = 0
diff = 5
hiscore = 0
score = 0
extra_spd = 0
prvscore = 0


def update():
    global score, framecount, diff, extra_spd, hiscore, prvscore
    if prvscore < score:
        if score % 50 == 0:
            player.hp = 10
        prvscore = score
    hiscore = max(hiscore, score)
    screen.blit(my_font.render(f'SCORE: {score}', False, (255, 255, 255)), (5, 5))
    screen.blit(my_font.render(f'{player.hp} HP', False, (255, 255, 255)), (930, 5))
    diff = 5 + int(score / 20)
    extra_spd = int(score / 50) * 0.25
    print(player.x, " ", player.y, " ", framecount, '\n', player.hp, '\n', extra_spd)
    x = player.x
    y = player.y
    uinn = pygame.key.get_pressed()
    mpos = pygame.mouse.get_pos()
    angle = atan2(-player.y - - mpos[1], -player.x - - mpos[0])
    player.update(uinn)
    if pygame.mouse.get_pressed()[0]:
        if framecount % 8 == 0:
            bullets.append(Bullet(x=player.x + 25, y=player.y + 25, angle=angle))
    for bullet in bullets:
        bullet.update()
        ##if(bullet.x > 1024 or bullet.x < 0 or bullet.y > 768 or bullet.y < 0):

        for i in range(len(enemies) - 1):
            if i >= len(enemies):
                break
            enemy = enemies[i]
            if bullet.rect.colliderect(enemy.rect):
                enemies.pop(i)
                score += 1

    while len(enemies) < diff:
        enemies.append(Enemy())

    for enemy in enemies:
        enemy.update(x, y, extra_spd)
        if enemy.rect.colliderect(player.rect):
            if not enemy.flag:
                player.hp -= 1
            enemy.flag = True
        else:
            enemy.flag = 0


def render():
    player.render(screen)
    for bullet in bullets:
        bullet.render(screen)
    for enemy in enemies:
        enemy.render(screen)


while running:
    framecount += 1
    screen.fill((50, 50, 50))
    if player.hp > 0:
        render()
        update()
    else:
        txt = my_font2.render(f"GAME OVER!", False, (255, 255, 255))
        txtrect = txt.get_rect(center=(1024/2, 768/2))
        screen.blit(txt, txtrect)
        txt2 = my_font2.render("press R to restart, or Q to quit.", False, (255, 255, 255))
        txtrect2 = txt2.get_rect(center=(1024/2, 768/2 + 100))
        screen.blit(txt2, txtrect2)
        txt3 = my_font.render(f"Your score is {score}, HighScore is {hiscore}", False, (255, 255, 255))
        txtrect3 = txt3.get_rect(center=(1024 / 2, 768 / 2 + 200))
        screen.blit(txt3, txtrect3)


    clock.tick(120)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not player.hp > 0:
                if event.key == pygame.K_r:
                    player.hp = 10
                    score = 0
                    prvscore = 0
                    bullets.clear()
                    enemies.clear()
                    extra_spd = 0
                if event.key == pygame.K_q:
                    running = False
            if event.key == pygame.K_p:
                player.spd += 1
            if event.key == pygame.K_o:
                player.spd = max(spd - 1, 0)
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.display.quit()
pygame.quit()
