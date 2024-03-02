import pygame
import random

class Enemy:
    def __init__(self):
        self.x = random.randint(26, 1024-26)
        self.y = random.randint(17, 758-17)
        self.img = pygame.image.load("pixil-frame-0.png")
        self.rect = pygame.Rect(self.x, self.y, 51, 33)
        self.spd = 0.5
        self.flag = False

    def render(self, screen):
        self.rect = screen.blit(self.img, (self.x, self.y))

    def update(self, player_x, player_y, spd):
        speed = self.spd + spd
        if player_x > self.x:
            self.x = self.x + speed
        else:
            self.x = self.x - speed
        if player_y > self.y:
            self.y = self.y + speed
        else:
            self.y = self.y - speed

