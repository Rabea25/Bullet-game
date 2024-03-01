import pygame
from math import *


class Bullet:
    def __init__(self, x, y, angle):
        self.init_x = x
        self.init_y = y
        self.x = 0
        self.y = 0
        self.angle = angle
        self.speed = 25
        self.rect = None

    def update(self):
        self.x += cos(self.angle) * self.speed
        self.y += sin(self.angle) * self.speed
        self.rect = pygame.Rect(self.x + self.init_x, self.y + self.init_y, 10, 10)

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
