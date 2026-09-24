from checkmate import checkmate
import sys

board = """R...
.K..
P.P.
....
"""
if len(sys.argv) == 1:
        checkmate(board)
else:
    print("There must be only one Argument.")

