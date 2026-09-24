VALID_PIECES = {"K", "Q", "B", "R", "P"} #ชื่อหมาก king queen Bishop Rook Pawn

class BoardError(Exception):
    pass

class Board:

    def __init__(self, raw_board):
        if not isinstance(raw_board, str):
            raise BoardError("board must be a string")

        rows = raw_board.split("\n")

        if rows and rows[-1] == "":
            rows.pop()

        if not rows:
            raise BoardError("empty board")

        size = len(rows)
        for row in rows:
            if len(row) != size:
                raise BoardError("board must be a square")

        self.size = size
        self.grid = [list(row) for row in rows]

        king_pos = None
        king_count = 0
        for r in range(size):
            for c in range(size):
                if self.grid[r][c] == "K":
                    king_count += 1
                    king_pos = (r, c)

        if king_count != 1:
            raise BoardError("board must contain exactly one King")

        self.king_pos = king_pos

    def in_bounds(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def piece_at(self, r, c):
        return self.grid[r][c]

    def is_piece(self, ch):
        return ch in VALID_PIECES

    def pieces(self):
        for r in range(self.size):
            for c in range(self.size):
                ch = self.grid[r][c]
                if self.is_piece(ch) and ch != "K":
                    yield r, c, ch