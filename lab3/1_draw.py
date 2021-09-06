import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (217, 217, 217), (0, 0, 400, 400)) #фон
circle(screen, (255, 255, 0), (200, 200), 100) #голова
circle(screen, (255, 0, 0), (150, 180), 20) #правый глаз
circle(screen, (0, 0, 0), (150, 180), 20, 1) #правый глаз обводка
circle(screen, (0, 0, 0), (150, 180), 8) #правый глаз зрачок
line(screen, (0, 0, 0), (180,175), (100,100), 10) # правая бровь

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
