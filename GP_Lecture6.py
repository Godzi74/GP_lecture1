import time

import pygame
import random
from sys import exit


pygame.init()
pygame.display.set_caption("Hello world")
screen = pygame.display.set_mode((1080, 960))
clock = pygame.time.Clock()

xpos = random.randrange(0, screen.get_size()[0])
centre_x = list(screen.get_size())[0] / 2
ypos = 0
speed = 1
movingDown = True

class Rain:


    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = 1
        self.raindropY = 0


    def Draw(self):
        pygame.draw.circle(screen, (100, 200, 255), (self.xpos, self.ypos), 10, )

    def Move(self):
        self.ypos += self.speed
        self.speed += 1
        if self.ypos > list(screen.get_size())[1]:
            self.ypos = 0
            self.speed = 1

drop = Rain(100,200)
drops = []

for i in range(20):
    xpos = random.randrange(0, screen.get_size()[0])
    ypos = random.randrange(0, screen.get_size()[1])
    drops.append((Rain(xpos, ypos)))

while True:
    screen.fill((110, 110, 110))

    for drop in drops:
        drop.Draw()
        drop.Move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            movingDown = True
       # if event.type == pygame.KEYUP and event.key == pygame.K_0:
        #   movingDown = False

    pygame.display.flip()

    clock.tick(60)

    pressedKey = pygame.key.get_pressed()
    if pressedKey[pygame.K_RIGHT]:
        xpos += 1
        pygame.display.update()