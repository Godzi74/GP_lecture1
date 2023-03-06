import time

import pygame
import random
from sys import exit

pygame.init()
font = pygame.font.Font(None, 60)
sound = pygame.mixer.Sound("sound.mp3")
music = pygame.mixer.Sound("beats.mp3")
pygame.display.set_caption("Hello world")
screen = pygame.display.set_mode((1080, 960))
clock = pygame.time.Clock()

points = 0
xpos = random.randrange(0, screen.get_size()[0])
centre_x = list(screen.get_size())[0] / 2
ypos = 0
speed = 1
movingDown = True
cloudSpeed = -150
playerPos = 800
player_surface = pygame.image.load("hello.png").convert_alpha()
player_surface.set_colorkey((255, 255, 255))
player_rectangle = player_surface.get_rect(center = (800, 800))
music.set_volume(1)
sound.set_volume(0.25)
music.play()
bg = pygame.image.load("backgrounds_stars.png").convert_alpha()

w,h = bg.get_size()
y = 0
y1 = -h

def rollingBG():
    global y, y1, h
    screen.blit(bg, (0,y))
    screen.blit(bg, (0, y1))
    y += 1
    y1 += 1
    if y > h:
        y = -h
    if y1 > h:
        y1 = -h


def scorePrinter():
    global points
    points = points + 1

class Rain:


    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = 1
        self.raindropY = 0
        self.hello_surface = pygame.image.load("RedInvader.png").convert_alpha()
        self.rect = pygame.Rect(self.xpos, self.ypos, 25, 20)
        self.active = True


    def Draw(self):
        if self.active == True:
            #pygame.draw.circle(screen, (100, 200, 255), (self.xpos, self.ypos), 10)
            screen.blit(self.hello_surface, self.rect)
       #pygame.draw.rect(screen, (100, 200, 255), pygame.Rect(self.xpos, self.ypos, 10, 10), 10, 10)

    def Move(self):
        self.ypos += self.speed
        self.speed += 1
        self.rect.x = self.xpos
        self.rect.y = self.ypos

        if self.rect.colliderect(player_rectangle):
            # print ("Yo mamma")
            scorePrinter()
            self.active = False
            sound.play()

        pressedKey = pygame.key.get_pressed()
        if pressedKey[pygame.K_d]:
            self.xpos += 1
        if pressedKey[pygame.K_a]:
            self.xpos -= 1
        self.xpos
        if self.ypos > list(screen.get_size())[1]:
            self.ypos = 100
            self.speed = 1
            self.active = True

drop = Rain(100,200)
drops = []


for i in range(20):
    xpos = random.randrange(100, 700)
    ypos = random.randrange(0, screen.get_size()[1])
    drops.append((Rain(xpos, ypos)))

while True:
    screen.fill((110, 110, 110))
    rollingBG()

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

    #if pygame.Rect.collidepoint(player_rectangle.left, player_rectangle.top):
       # print("hi")

    cloud_image = pygame.image.load("cloud.png").convert_alpha()
    screen.blit(cloud_image, (cloudSpeed, -300))
    screen.blit(font.render("Score: {} ".format(points), True, (0, 0, 0,)), (800, 100))
    screen.blit(player_surface, player_rectangle)


    pygame.display.flip()

    clock.tick(60)

    pressedKey = pygame.key.get_pressed()
    if pressedKey[pygame.K_d]:
        xpos += 1
        cloudSpeed += 1
        pygame.display.update()
    if pressedKey[pygame.K_a]:
        cloudSpeed -= 1
        pygame.display.update()

    if pressedKey[pygame.K_RIGHT]:
        player_rectangle.left += 2
        pygame.display.update()
    if pressedKey[pygame.K_LEFT]:
        player_rectangle.left -= 2
        pygame.display.update()
    if player_rectangle.left > 1000:
        player_rectangle.left = 1000
    if player_rectangle.left < 1:
        player_rectangle.left = 1