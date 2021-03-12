class Rules:
    def __init__(self, castle='', en_passant=''):
        self.castle = castle
        self.en_passant = en_passant

    def get_legal_moves(self, board_state, piece_index):
        legal_moves = []
        current_position = board_state.copy()
        piece_color = current_position[piece_index][0]
        piece_type = current_position[piece_index][1]
        if piece_type == 'R':
            row = piece_index // 8
            for squares_LEFT in range(1, 8):
                squares_LEFT = -squares_LEFT
                if piece_index + squares_LEFT >= row*8:
                    if current_position[piece_index + squares_LEFT] == '':
                        legal_moves.append(piece_index + squares_LEFT)
                        continue
                    elif current_position[piece_index + squares_LEFT][0] != piece_color:
                        legal_moves.append(piece_index + squares_LEFT)
                        break
                    elif current_position[piece_index + squares_LEFT][0] == piece_color:
                        break
            for squares_RIGHT in range(1, 8):
                if piece_index + squares_RIGHT < (row+1)*8:
                    if current_position[piece_index + squares_RIGHT] == '':
                        legal_moves.append(piece_index + squares_RIGHT)
                        continue
                    elif current_position[piece_index + squares_RIGHT][0] != piece_color:
                        legal_moves.append(piece_index + squares_RIGHT)
                        break
                    elif current_position[piece_index + squares_RIGHT][0] == piece_color:
                        break
            for squares_UP in range(1, 8):
                squares_UP = -squares_UP*8
                if piece_index + squares_UP >= 0:
                    if current_position[piece_index + squares_UP] == '':
                        legal_moves.append(piece_index + squares_UP)
                        continue
                    elif current_position[piece_index + squares_UP][0] != piece_color:
                        legal_moves.append(piece_index + squares_UP)
                        break
                    elif current_position[piece_index + squares_UP][0] == piece_color:
                        break
            for squares_DOWN in range(1, 8):
                squares_DOWN = squares_DOWN*8
                if piece_index + squares_DOWN <= 63:
                    if current_position[piece_index + squares_DOWN] == '':
                        legal_moves.append(piece_index + squares_DOWN)
                        continue
                    elif current_position[piece_index + squares_DOWN][0] != piece_color:
                        legal_moves.append(piece_index + squares_DOWN)
                        break
                    elif current_position[piece_index + squares_DOWN][0] == piece_color:
                        break
        elif piece_type == 'B':
            pass
        return legal_moves       
        