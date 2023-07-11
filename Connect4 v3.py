import time
import tkinter as tk
import graphics as g

board = [ [0,0,0,0,0,0] for i in range(7) ]
turn = [1,"yellow"]

def load_board():
    for i in range(7):
        for j in range(6):
            if (board[i][j] == 0):
                empty = g.Image(g.Point(i*78 + 260,100 + j*78), "emptySquare.gif")
                g.Image.draw(empty,window)
            if (board[i][j] == 1):
                yellowCounter = g.Image(g.Point(i*78 + 260, 100 + j*78),  "yellowCounter.gif")
                g.Image.draw(yellowCounter,window)
            if (board[i][j] == -1):
                redCounter =g.Image(g.Point(i*78 + 260, 100 + j*78),  "redCounter.gif")
                g.Image.draw(redCounter,window)



def fill_column(column):
    fullrow = board[column]
    i = 5
    while ( fullrow[i] != 0):
        i = i -1
        if(i ==-1):
            break
    if(i>-1):
        fill_square(column,i,turn[1])

def fill_square(a,b,color):
    if(color == "red"):
        redCounter =g.Image(g.Point(a*78 + 260, 100 + b*78),  "redCounter.gif")
        g.Image.draw(redCounter,window)
        board[a][b] = 1
    if(color == "yellow"):
        yellowCounter = g.Image(g.Point(a*78 + 260, 100 + b*78),  "yellowCounter.gif")
        g.Image.draw(yellowCounter,window)
        board[a][b] = -1
    
    
def switch_turn():
    if (turn[0] == 1):
        turn[0] = -1
        turn[1] = "red"
    else:
        turn[0] = 1
        turn[1] = "yellow"

######################################
print ("start!")
window = g.GraphWin("Four in a Row", 1000, 600)
g.GraphWin.setBackground(window, "light green")
load_board()
while(1):
    mousePosition = window.getMouse()
    column = int((mousePosition.x - 260 + 39)// 78)
    if(column >= 0 and column <= 6):
        fill_column(column)
        switch_turn()










