import pygame
import sys
import random
import math
from spritesheet_functions import SpriteSheet

pygame.init()
pygame.display.set_caption("Chess")

screenx = 600
screeny = 600
screen = pygame.display.set_mode((screenx, screeny))
bgcolor = (250, 250, 250)

clock = pygame.time.Clock()

while True:
    screen.fill(bgcolor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    msElapsed = clock.tick(30)