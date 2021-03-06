import pygame
import sys
import random
import math
from spritesheet_functions import SpriteSheet

pygame.init()
pygame.display.set_caption("Chess")

screenx = 640
screeny = 640
screen = pygame.display.set_mode((screenx, screeny))
bgcolor = (250, 250, 250)

clock = pygame.time.Clock()

DARK_SQUARE = (100, 40, 20)
LIGHT_SQUARE = (200, 180, 120)

class Chessboard:
    def __init__(self, area, position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'):
        self.area = area
        self.board = ['' for i in range(64)]
        self.screen_x, self.screen_y = pygame.display.get_window_size()
        self.square = pygame.Surface((self.screen_x/8, self.screen_y/8)) 
              
    def draw(self):
        for y in range(8):
            for x in range(8):
                if y % 2:
                    if x % 2:
                        self.square.fill(LIGHT_SQUARE)
                    else:
                        self.square.fill(DARK_SQUARE)
                else:
                    if x % 2:
                        self.square.fill(DARK_SQUARE)
                    else:
                        self.square.fill(LIGHT_SQUARE)

                self.area.blit(self.square, (self.screen_x/8 * x, self.screen_y/8 * y))

board = Chessboard(screen)

while True:
    screen.fill(bgcolor)
    board.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    msElapsed = clock.tick(30)