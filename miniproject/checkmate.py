#!/usr/bin/env python3
"""
checkmate.py

checkmate(board) prints "Success" if the King on `board` is in
check (some other piece can capture it), "Fail" otherwise.

On any undefined behavior (bad board shape, wrong number of Kings,
invalid input...) it prints nothing and simply returns control to
the caller, as required by the subject.
"""

from pprint import pprint

from board_chess import Board, BoardError

BISHOP_DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
ROOK_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
QUEEN_DIRS = BISHOP_DIRS + ROOK_DIRS
# Pawns capture one square diagonally "forward" (towards row - 1).
PAWN_CAPTURES = [(-1, -1), (-1, 1)]


def _slides_to_king(board, r, c, directions):
    """
    From (r, c), look along each direction until the edge of the
    board or a piece is found. A piece can only capture the FIRST
    piece it meets on its path, so as soon as something blocks a
    line we stop looking further along that direction.
    """
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        while board.in_bounds(nr, nc):
            ch = board.piece_at(nr, nc)
            if ch == "K":
                return True
            if board.is_piece(ch):
                # first piece on the path isn't the King: line is blocked
                break
            nr += dr
            nc += dc
    return False


def _pawn_threatens_king(board, r, c):
    for dr, dc in PAWN_CAPTURES:
        nr, nc = r + dr, c + dc
        if board.in_bounds(nr, nc) and board.piece_at(nr, nc) == "K":
            return True
    return False


def _check_range(board):
    """
    Debug helper: returns a copy of the grid where every square a
    piece can threaten is replaced with 'X' (the King's square is
    marked 'X' too if some piece reaches it). Reads exclusively from
    the untouched board.grid so pieces don't interfere with each
    other's line-of-sight calculations.
    """
    result = [row.copy() for row in board.grid]

    def mark(r, c, directions, single_step=False):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while board.in_bounds(nr, nc):
                original = board.piece_at(nr, nc)
                if original == "K":
                    result[nr][nc] = "X"
                    break
                if board.is_piece(original):
                    break
                result[nr][nc] = "X"
                if single_step:
                    break
                nr += dr
                nc += dc

    for r, c, piece in board.pieces():
        if piece == "P":
            mark(r, c, PAWN_CAPTURES, single_step=True)
        elif piece == "B":
            mark(r, c, BISHOP_DIRS)
        elif piece == "R":
            mark(r, c, ROOK_DIRS)
        elif piece == "Q":
            mark(r, c, QUEEN_DIRS)

    return result


def checkmate(raw_board, debug=False):
    try:
        board = Board(raw_board)
    except BoardError:
        # Undefined behavior: print nothing, give back control.
        return

    if debug:
        pprint(board.grid)
        print((board.size, board.size))
        print("Check Range:")
        pprint(_check_range(board))
        print()

    for r, c, piece in board.pieces():
        if piece == "P":
            threatens = _pawn_threatens_king(board, r, c)
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