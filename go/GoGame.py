from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .GoLogic import Board
import numpy as np

class GoGame(Game):
    stones = {
        -1: "X", # black
        +0: "-", # empty
        +1: "O" # white
    }

    @staticmethod
    def getSquarePiece(piece):
        return GoGame.stones[piece]

    @staticmethod
    def display(board):
        n = board.shape[0]
        print("   ", end="")
        for y in range(n):
            print(y, end=" ")
        print("")
        print("-----------------------")
        for y in range(n):
            print(y, "|", end="")    # print the row #
            for x in range(n):
                piece = board[y][x]    # get the piece to print
                print(GoGame.stones[piece], end=" ")
            print("|")

        print("-----------------------")
