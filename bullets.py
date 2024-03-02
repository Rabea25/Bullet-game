import pygame
from math import *
import os, sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class Bullet:
    def __init__(self, x, y, angle):
        self.init_x = x
        self.init_y = y
        self.x = 0
        self.y = 0
        self.angle = angle
        self.speed = 25
        self.rect = None
        self.img = pygame.image.load("blt.png")
        self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def update(self):
        self.x += cos(self.angle) * self.speed
        self.y += sin(self.angle) * self.speed

    def render(self, screen):
        self.rect = screen.blit(self.img, (self.x + self.init_x, self.y + self.init_y))
