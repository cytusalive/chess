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
        if piece_type == 'B':
            for squares_UPLEFT in range(1, 8):
                squares_UPLEFT = -squares_UPLEFT*8 - squares_UPLEFT
                new_index = piece_index + squares_UPLEFT
                if new_index % 8 == 7:
                    break
                if new_index >= 0:
                    if current_position[new_index] == '':
                        if new_index % 8 == 0:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
            for squares_UPRIGHT in range(1, 8):
                squares_UPRIGHT = -squares_UPRIGHT*8 + squares_UPRIGHT
                new_index = piece_index + squares_UPRIGHT
                if new_index % 8 == 0:
                    break
                if new_index >= 0:
                    if current_position[new_index] == '':
                        if new_index % 8 == 7:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
            for squares_DOWNLEFT in range(1, 8):
                squares_DOWNLEFT = squares_DOWNLEFT*8 - squares_DOWNLEFT
                new_index = piece_index + squares_DOWNLEFT
                if new_index % 8 == 7:
                    break
                if new_index < 64:
                    if current_position[new_index] == '':
                        if new_index % 8 == 0:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
            for squares_DOWNRIGHT in range(1, 8):
                squares_DOWNRIGHT = squares_DOWNRIGHT*8 + squares_DOWNRIGHT
                new_index = piece_index + squares_DOWNRIGHT
                if new_index % 8 == 0:
                    break
                if new_index < 64:
                    if current_position[new_index] == '':
                        if new_index % 8 == 7:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
        if piece_type == 'Q':
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
        
            for squares_UPLEFT in range(1, 8):
                squares_UPLEFT = -squares_UPLEFT*8 - squares_UPLEFT
                new_index = piece_index + squares_UPLEFT
                if new_index % 8 == 7:
                    break
                if new_index >= 0:
                    if current_position[new_index] == '':
                        if new_index % 8 == 0:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
            for squares_UPRIGHT in range(1, 8):
                squares_UPRIGHT = -squares_UPRIGHT*8 + squares_UPRIGHT
                new_index = piece_index + squares_UPRIGHT
                if new_index % 8 == 0:
                    break
                if new_index >= 0:
                    if current_position[new_index] == '':
                        if new_index % 8 == 7:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
            for squares_DOWNLEFT in range(1, 8):
                squares_DOWNLEFT = squares_DOWNLEFT*8 - squares_DOWNLEFT
                new_index = piece_index + squares_DOWNLEFT
                if new_index % 8 == 7:
                    break
                if new_index < 64:
                    if current_position[new_index] == '':
                        if new_index % 8 == 0:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
            for squares_DOWNRIGHT in range(1, 8):
                squares_DOWNRIGHT = squares_DOWNRIGHT*8 + squares_DOWNRIGHT
                new_index = piece_index + squares_DOWNRIGHT
                if new_index % 8 == 0:
                    break
                if new_index < 64:
                    if current_position[new_index] == '':
                        if new_index % 8 == 7:
                            legal_moves.append(new_index)
                            break
                        else:
                            legal_moves.append(new_index)
                            continue
                    elif current_position[new_index][0] != piece_color:
                        legal_moves.append(new_index)
                        break
                    elif current_position[new_index][0] == piece_color:
                        break
        if piece_type == 'K':
            directions = [-9, -8, -7, -1, 1, 7, 8, 9]
            for direction in directions:
                new_index = piece_index + direction
                if new_index < 64 and new_index >= 0:
                    legal_moves.append(new_index)
        return legal_moves       
        