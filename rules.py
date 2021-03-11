class Rules:
    def __init__(self):
        pass

    def get_legal_moves(self, board_state, piece_index):
        legal_moves = []
        current_position = board_state.copy()
        piece_color = current_position[piece_index][0]
        piece_type = current_position[piece_index][1]
        if piece_type == 'R':
            row = piece_index // 8
            for squares in range(1, 8):
                if piece_index - squares >= row*8:
                    if current_position[piece_index - squares] == '':
                        legal_moves.append(piece_index - squares)
                        continue
                    elif current_position[piece_index - squares][0] != piece_color:
                        legal_moves.append(piece_index - squares)
                        break
                    elif current_position[piece_index - squares][0] == piece_color:
                        break
        return legal_moves       
        
    def add_position(self, old_index, new_index):
        possible_position = self.current_position.copy()
        possible_position[new_index] = possible_position[old_index]
        possible_position[old_index] = ''
        self.legal_positions.append(possible_position)
        
