import pygame
from player import *
from bullets import *
from math import *
from enemies import *
import random

# game setup
pygame.init()
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
enemies = []
player = Player(x, y, spd)
framecnt = 0


def update():
    print(player.x, " ", player.y)
    uinn = pygame.key.get_pressed()
    mpos = pygame.mouse.get_pos()
    angle = atan2(-player.y - - mpos[1], -player.x - - mpos[0])
    player.update(uinn)
    if pygame.mouse.get_pressed()[0]:
        if framecnt % 8 == 0:
            bullets.append(Bullet(x=player.x+25, y=player.y+25, angle=angle))
    for bullet in bullets:
        bullet.update()
        for i in range(len(enemies) - 1):
            if i>=len(enemies):
                break
            enemy = enemies[i]
            if bullet.rect.colliderect(enemy.rect):
                enemies.pop(i)

    if len(enemies) < 10:
        enemies.append(Enemy())


def render():
    player.render(screen)
    for bullet in bullets:
        bullet.render(screen)
    for enemy in enemies:
        enemy.render(screen)


while running:
    framecnt += 1
    if framecnt == 121:
        framcnt = 1
    screen.fill((50, 50, 50))
    render()
    update()

    clock.tick(120)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.spd += 1
            if event.key == pygame.K_o:
                player.spd = max(spd - 1, 0)
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.display.quit()
pygame.quit()
