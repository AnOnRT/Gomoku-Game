from tkinter import *
import code
from code import Game
import math
import sys
import random

def clear(cnv):
    cnv.delete("circle")
    cnv.delete("dn")
    cnv.delete("line")

pl = Game()

width = 640
height = 640
root = Tk()

root.title("Gomoku")
cnv = Canvas(root, width=width, height=height, bg="brown")
cnv.grid()


for x in range(40, 600, 40):
    for y in range(40, 600, 40):
        cnv.create_rectangle(x, y, x+40, y+40, outline='black', tag = "r")


def restart():
    global root
    root.destroy()
    pl = Game()
    width = 640
    height = 640
    root = Tk()
    root.title("Gomoku")
    cnv = Canvas(root, width=width, height=height, bg="brown")

    cnv.grid()

    for x in range(40, 600, 40):
        for y in range(40, 600, 40):
            cnv.create_rectangle(x, y, x + 40, y + 40, outline='black', tag="r")

    cnv.bind('<Button>', click)
    root.mainloop()

i = 1
def put_circle(x, y):
    global i, pl, n
    a = [None] * 225

    x_r = x % 40
    y_r = y % 40
    x_1 = x // 40
    y_1 = y // 40
    if pl.check_win() == True or pl.check() == True:
        pl = Game()
        cnv.delete(n)
        cnv.delete("dn")
        cnv.delete("line")

    if (x_r > 20 and y_r > 20 and x >= 40 and y >= 40 and x <= 600 and y <= 600 and pl.play(y_1, x_1) == True):
        x1 = (x_1 + 1) * 40 - 15
        y1 = (y_1 + 1) * 40 - 15
        x2 = (x_1 + 1) * 40 + 15
        y2 = (y_1 + 1) * 40 + 15
        if i == 1:
            put_crc(x1, y1, x2, y2, i)
            i = 2
        else:
            put_crc(x1, y1, x2, y2, i)
            i = 1
        print(pl.board)
        if pl.check_win() == True:
            cnv.create_text(320, 20, text=f"Player {pl.winner} wins", tag="dn")
            cnv.create_line((pl.win_y1 + 1) * 40, (pl.win_x1 + 1) * 40, (pl.win_y2 + 1) * 40, (pl.win_x2 + 1) * 40,
                            fill="green", width=5, tag="line")
        if pl.check():
            cnv.create_text(320, 20, text="No move available", tag="dn")


    elif (x_r > 20 and y_r < 20 and x >= 40 and y >= 40 and x <= 600 and y <= 600 and pl.play(y_1 - 1, x_1) == True):
        x1 = (x_1 + 1) * 40 - 15
        y1 = (y_1) * 40 - 15
        x2 = (x_1 + 1) * 40 + 15
        y2 = (y_1) * 40 + 15
        if i == 1:
            put_crc(x1, y1, x2, y2, i)
            i = 2
        else:
            put_crc(x1, y1, x2, y2, i)
            i = 1
        print(pl.board)
        if pl.check_win() == True:
            cnv.create_text(320, 20, text=f"Player {pl.winner} wins", tag="dn")
            cnv.create_line((pl.win_y1 + 1) * 40, (pl.win_x1 + 1) * 40, (pl.win_y2 + 1) * 40,
                            (pl.win_x2 + 1) * 40, fill="green", width=5, tag="line")

        if pl.check():
            cnv.create_text(320, 20, text="No move available", tag="dn")


    elif (x_r < 20 and y_r < 20 and x >= 40 and y >= 40 and x <= 600 and y <= 600 and pl.play(y_1 - 1, x_1 - 1)):
        x1 = (x_1) * 40 - 15
        y1 = (y_1) * 40 - 15
        x2 = (x_1) * 40 + 15
        y2 = (y_1) * 40 + 15
        if i == 1:
            put_crc(x1, y1, x2, y2, i)
            i = 2
        else:
            put_crc(x1, y1, x2, y2, i)
            i = 1
        print(pl.board)
        if pl.check_win() == True:
            cnv.create_text(320, 20, text=f"Player {pl.winner} wins", tag="dn")
            cnv.create_line((pl.win_y1 + 1) * 40, (pl.win_x1 + 1) * 40,
                            (pl.win_y2 + 1) * 40, (pl.win_x2 + 1) * 40, fill="green", width=5, tag="line")
        if pl.check():
            cnv.create_text(320, 20, text="No move available", tag="dn")



    elif (x_r < 20 and y_r > 20 and x >= 40 and y >= 40 and x <= 600 and y <= 600 and pl.play(y_1, x_1 - 1)):
        x1 = (x_1) * 40 - 15
        y1 = (y_1 + 1) * 40 - 15
        x2 = (x_1) * 40 + 15
        y2 = (y_1 + 1) * 40 + 15
        if i == 1:
            put_crc(x1, y1, x2, y2, i)
            i = 2
        else:
            put_crc(x1, y1, x2, y2, i)
            i = 1
        print(pl.board)
        if pl.check_win() == True:
            cnv.create_text(320, 20, text=f"Player {pl.winner} wins", tag="dn")
            cnv.create_line((pl.win_y1 + 1) * 40, (pl.win_x1 + 1) * 40,
                            (pl.win_y2 + 1) * 40, (pl.win_x2 + 1) * 40, fill="green", width=5, tag="line")

        if pl.check():
            cnv.create_text(320, 20, text="No move available", tag="dn")


n = "circle"
def put_crc(x1,y1,x2, y2, i):
    global n
    if i == 1:
        cnv.create_oval(x1, y1, x2, y2, fill = "black", outline = "", tag = n)
    else:
        cnv.create_oval(x1, y1, x2, y2, fill = "white", outline = "", tag = n)

i = 1
def click(event):

    arr = []
    global i, pl
    x, y = event.x, event.y
    x_r = x % 40
    y_r = y % 40
    x_1 = x // 40
    y_1 = y // 40
    put_circle(x, y)




cnv.bind('<Button>', click)
root.mainloop()