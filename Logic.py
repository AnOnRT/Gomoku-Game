from tkinter import *
import math
import sys
import random



class Game:
    def __init__(self):

        # self.board is a 15 x 15 array of integers with the contents of
        # each square: 0 = empty, 1 = player 1 stone, 2 = player 2 stone
        self.board = [[0] * 15 for i in range(15)]
        self.turn = 1  # the player whose turn it is to move (1 or 2)
        self.winner = 0  # the player who has won, if any
        self.win_x1 = self.win_y1 = None  # (x, y) pos of one end of winning line
        self.win_x2 = self.win_y2 = None  # (x, y) pos of other end of winning line


    dirs = [(1, -1), (1, 0), (1, 1), (0, 1)]

    # If either player has exactly 5 in a row starting at (x, y) in direction (dx, dy),
    # return that player number (1 or 2); otherwise return 0.
    def five_in_a_row(self, x, y, dx, dy):
        def is_at(x, y, p):
            return 0 <= x < 15 and 0 <= y < 15 and self.board[x][y] == p

        p = self.board[x][y]
        return (p > 0 and
                not is_at(x - dx, y - dy, p) and
                all([is_at(x + i * dx, y + i * dy, p) for i in range(5)]) and
                not is_at(x + 5 * dx, y + 5 * dy, p))

    # Check if either player has won.  If so, set self.winner and self.{x1,y1,x2,y2}.
    def check_win(self):
        for x in range(15):
            for y in range(15):
                for dx, dy in self.dirs:
                    if self.five_in_a_row(x, y, dx, dy):
                        if(self.turn == 1):
                            self.winner = self.turn + 1
                        else:
                            self.winner = self.turn - 1
                        self.win_x1 = x
                        self.win_y1 = y
                        self.win_x2 = x + 4*dx
                        self.win_y2 = y + 4*dy
                        return True
    # If (x, y) is a valid move for the current player, place a stone there and
    # return True.  Otherwise return False.
    def play(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = self.turn
            if (self.turn == 1):
                self.turn = 2
            else:
                self.turn = 1
            return True
        else:
            return False

    def check(self):
        k=True
        for i in range(15):
            for j in range(15):
                if (self.board[i][j] == 0):
                        k = False
        if k == True:
            return True
        return False
