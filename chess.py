import pygame
import sys
import random
import math
from rules import Rules

pygame.init()
pygame.display.set_caption("Chess")

screenx = 640
screeny = 640
screen = pygame.display.set_mode((screenx, screeny))
bgcolor = (250, 250, 250)

clock = pygame.time.Clock()

DARK_SQUARE = (120, 60, 40)
LIGHT_SQUARE = (200, 180, 120)
HIGHLIGHT_SQUARE = (240, 240, 120, 180)
MOVE_INDICATOR = (100, 200, 150, 100)

pygame.font.init()
font = pygame.font.SysFont("Arial", 20, True)

class Pieces:
    def __init__(self):
        self.types = {}
    
    def load_pieces(self):
        piece_types = ['R', 'N', 'B', 'Q', 'K', 'P']
        for ptype in piece_types:
            self.types['w'+ptype] = pygame.image.load('piece_sprites/w'+ptype+'.png')
            self.types['b'+ptype] = pygame.image.load('piece_sprites/b'+ptype+'.png')

class Chessboard:
    def __init__(self, area, pieces):
        self.area = area
        self.board = ['' for i in range(64)]
        self.pieces = pieces
        self.screen_x, self.screen_y = pygame.display.get_window_size()
        self.square = pygame.Surface((self.screen_x/8, self.screen_y/8))
        self.color_to_move = ''
        self.highlight_squares = []
        self.dotted_squares = []

    def load_position(self, position='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w'): #'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        board_index = 0
        for fen_index in range(len(position)):
            if position[fen_index].isnumeric():
                for l in range(int(position[fen_index])):
                    self.board[board_index] = ''
                    board_index += 1
            elif position[fen_index] == '/':
                continue
            elif position[fen_index] == ' ':
                self.color_to_move = position[fen_index+1]
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

                # showing square index, remove after development
                index = font.render(str(y*8 + x), True, (0, 0, 0))
                self.square.blit(index, (0, 0))

                self.area.blit(self.square, (self.screen_x/8 * x, self.screen_y/8 * y))

                if 8*y+x in self.highlight_squares:
                    transparent_square = pygame.Surface((80,80)).convert_alpha()
                    transparent_square.fill(HIGHLIGHT_SQUARE)
                    self.area.blit(transparent_square, (self.screen_x/8 * x, self.screen_y/8 * y))
                if 8*y+x in self.dotted_squares:
                    transparent_square = pygame.Surface((80,80)).convert_alpha()
                    transparent_square.fill(MOVE_INDICATOR)
                    self.area.blit(transparent_square, (self.screen_x/8 * x, self.screen_y/8 * y))
                
                
        if self.color_to_move == 'w':
            pygame.display.set_caption("Chess - White to Move")
        elif self.color_to_move == 'b':
            pygame.display.set_caption("Chess - Black to Move")

    def draw_pieces(self):
        for square_index in range(len(self.board)):
            if self.board[square_index]:
                x, y = index_to_coordinates(square_index)
                self.area.blit(self.pieces.types[self.board[square_index]], (x*self.screen_x/8, y*self.screen_y/8))

    def switch_turns(self):
        if self.color_to_move == 'w':
            self.color_to_move = 'b'
        elif self.color_to_move == 'b':
            self.color_to_move = 'w'

def index_to_coordinates(index):
    y = index // 8 
    x = index % 8 
    return (x, y)

def coordinates_to_index(x, y):
    index = y * 8 + x
    return index

pieces = Pieces()
pieces.load_pieces()
chessgame = Chessboard(screen, pieces)
chessgame.load_position()

rules = Rules()

dragging = False

while True:
    screen.fill(bgcolor)
    chessgame.draw_board()
    chessgame.draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dragging == False:
                mousex, mousey = pygame.mouse.get_pos()
                old_square_index = coordinates_to_index(mousex//80, mousey//80)
                if chessgame.board[old_square_index]:
                    if chessgame.board[old_square_index][0] == chessgame.color_to_move:
                        legal_moves = rules.get_legal_moves(chessgame.board, old_square_index)
                        print(legal_moves)
                        chessgame.dotted_squares = legal_moves
                        dragging_piece = chessgame.board[old_square_index]
                        chessgame.board[old_square_index] = ''
                        dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            chessgame.dotted_squares = []
            if dragging == True:
                mousex, mousey = pygame.mouse.get_pos()
                new_square_index = coordinates_to_index(mousex//80, mousey//80)
                '''
                validmove = False
                # moving on empty square
                if chessgame.board[new_square_index] == '':
                    if new_square_index == old_square_index:
                        validmove = False
                    else:
                        validmove = True
                # moving on another piece
                if chessgame.board[new_square_index]:
                    if chessgame.board[new_square_index][0] == chessgame.color_to_move:
                        validmove = False
                    elif chessgame.board[new_square_index][0] != chessgame.color_to_move:
                        validmove = True
                '''
                if new_square_index in legal_moves:
                    chessgame.highlight_squares = [old_square_index, new_square_index]
                    chessgame.board[new_square_index] = dragging_piece
                    dragging = False
                    # PAWN PROMOTION
                    for piece_index in range(8):
                        if chessgame.board[piece_index] == 'wP':
                            chessgame.board[piece_index] = 'wQ'
                        if chessgame.board[63 - piece_index] == 'bP':
                            chessgame.board[63 - piece_index] = 'bQ'
                    # PAWN EN PASSANT
                    if dragging_piece == 'wP' and new_square_index == rules.en_passant:
                        chessgame.board[new_square_index + 8] = ''
                    if dragging_piece == 'bP' and new_square_index == rules.en_passant:
                        chessgame.board[new_square_index - 8] = ''
                    rules.en_passant = []
                    if dragging_piece == 'bP' and new_square_index - old_square_index == 16:
                        rules.en_passant = new_square_index - 8
                    if dragging_piece == 'wP' and new_square_index - old_square_index == -16:
                        rules.en_passant = new_square_index + 8

                    chessgame.switch_turns()
                else:
                    chessgame.board[old_square_index] = dragging_piece
                    dragging = False

    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        if dragging == True:
            mousex, mousey = pygame.mouse.get_pos()
            screen.blit(pieces.types[dragging_piece], (mousex-40, mousey-40))


    pygame.display.update()
    msElapsed = clock.tick(30)