from board_chess import Board, BoardError

BISHOP_DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
ROOK_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
QUEEN_DIRS = BISHOP_DIRS + ROOK_DIRS
PAWN_CAPTURES = [(-1, -1), (-1, 1)]

def _slides_to_king(board, r, c, directions):
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        while board.in_bounds(nr, nc):
            ch = board.piece_at(nr, nc)
            if ch == "K":
                return True
            if board.is_piece(ch):
                break
            nr += dr
            nc += dc
    return False

def _pawn_to_king(board, r, c):
    for dr, dc in PAWN_CAPTURES:
        nr, nc = r + dr, c + dc
        if board.in_bounds(nr, nc) and board.piece_at(nr, nc) == "K":
            return True
    return False

def checkmate(raw_board):
    try:
        board = Board(raw_board)
    except BoardError:
        return
    
    for r, c, piece in board.pieces():
        if piece == "P":
            threatens = _pawn_to_king(board, r, c)
        elif piece == "B":
            threatens = _slides_to_king(board, r, c, BISHOP_DIRS)
        elif piece == "R":
            threatens = _slides_to_king(board, r, c, ROOK_DIRS)
        elif piece == "Q":
            threatens = _slides_to_king(board, r, c, QUEEN_DIRS)
        else:
            threatens = False

        if threatens:
            print("Success")
            return

    print("Fail")