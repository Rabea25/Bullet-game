import pygame
import random

class Enemy:
    def __init__(self):
        self.x = random.randint(26, 1024-26)
        self.y = random.randint(17, 758-17)
        self.img = pygame.image.load("pixil-frame-0.png")
        self.rect = pygame.Rect(self.x, self.y, 51, 33)

    def render(self, screen):
        self.rect = screen.blit(self.img, (self.x, self.y))
