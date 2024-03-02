import pygame


class Player:

    def __init__(self, x, y, spd):
        self.x = x
        self.y = y
        self.radius = 25
        self.r = 254
        self.g = 0
        self.b = 0
        self.flag = 1
        self.spd = spd
        self.img = pygame.image.load("pixil-frame-1.png")
        self.rect = None
        self.hp = 10

    def update(self, uin):
        if uin[pygame.K_d]:
            self.x = min(1024 - self.radius, self.x + self.spd)
        if uin[pygame.K_a]:
            self.x = max(self.radius, self.x - self.spd)
        if uin[pygame.K_s]:
            self.y = min(768 - self.radius, self.y + self.spd)
        if uin[pygame.K_w]:
            self.y = max(self.radius, self.y - self.spd)

        if self.flag == 1:
            self.b += 2
            if self.b == 254:
                self.flag = 2
        if self.flag == 2:
            self.r -= 2
            if self.r == 0:
                self.flag = 3
        if self.flag == 3:
            self.g += 2
            if self.g == 254:
                self.flag = 4
        if self.flag == 4:
            self.b -= 2
            if self.b == 0:
                self.flag = 5
        if self.flag == 5:
            self.r += 2
            if self.r == 254:
                self.flag = 6
        if self.flag == 6:
            self.g -= 2
            if self.g == 0:
                self.flag = 1

    def render(self, screen):
        self.rect = screen.blit(self.img, (self.x, self.y))
