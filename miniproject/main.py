#!/usr/bin/env python3
from checkmate import checkmate
from sys import argv


def main():
    board = """\
R...
.K..
.P..
....
"""
    try:
        if len(argv) > 1:
            print("usage: python3 main.py")
        else:
            checkmate(board, debug=True)
    except Exception:
        return


if __name__ == "__main__":
    main()