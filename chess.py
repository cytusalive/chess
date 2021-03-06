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

class Pieces:
    def __init__(self):
        self.dict = {}
    
    def load_pieces(self):
        piece_types = ['R', 'N', 'B', 'Q', 'K', 'P']
        for ptype in piece_types:
            self.dict['w'+ptype] = pygame.image.load('piece_sprites/w'+ptype+'.png')
            self.dict['b'+ptype] = pygame.image.load('piece_sprites/b'+ptype+'.png')



class Chessboard:
    def __init__(self, area, pieces):
        self.area = area
        self.board = ['' for i in range(64)]
        self.pieces = pieces
        self.screen_x, self.screen_y = pygame.display.get_window_size()
        self.square = pygame.Surface((self.screen_x/8, self.screen_y/8)) 

    def load_position(self, position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'):
        board_index = 0
        for fen_index in range(len(position)):
            if position[fen_index].isnumeric():
                for l in range(int(position[fen_index])):
                    self.board[board_index] = ''
                    board_index += 1
            elif position[fen_index] == '/':
                continue
            elif position[fen_index] == ' ':
                break
            else:
                if position[fen_index].islower():
                    self.board[board_index] = 'b' + position[fen_index].upper()
                    board_index += 1
                else:
                    self.board[board_index] = 'w' + position[fen_index]
                    board_index += 1
            
              
    def draw_board(self):
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

    def draw_pieces(self):
        for square_index in range(len(self.board)):
            if self.board[square_index]:
                x, y = index_to_coordinates(square_index)
                self.area.blit(self.pieces.dict[self.board[square_index]], (x*self.screen_x/8, y*self.screen_y/8))

def index_to_coordinates(index):
    y = index // 8 
    x = index % 8 
    return (x, y)


pieces = Pieces()
pieces.load_pieces()
chessgame = Chessboard(screen, pieces)
chessgame.load_position()


while True:
    screen.fill(bgcolor)
    chessgame.draw_board()
    chessgame.draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    msElapsed = clock.tick(30)