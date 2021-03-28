def evaluate(position):
    white_pieces = []
    black_pieces = []
    for square in position:
        if square:
            if square[0] == 'w':
                white_pieces.append(square[1])
            if square[0] == 'b':
                black_pieces.append(square[1])
    white_piece_value = 0
    black_piece_value = 0
    piece_value = {'K': 100000, 'Q': 900, 'R': 500, 'B': 330, 'N': 320, 'P': 100}
    for piece in white_pieces:
        white_piece_value += piece_value[piece]
    for piece in black_pieces:
        black_piece_value += piece_value[piece]
    return (white_piece_value - black_piece_value) * 0.01
