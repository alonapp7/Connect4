import time
import tkinter as tk
import graphics as g

## global variables

board = [ [0,0,0,0,0,0] for i in range(7) ]
board[2][4] = 7

for i in range (6):
    print (i)




def load_board():
    for i in range(7):
        for j in range(6):
            if (board[i][j] == 0):
                empty = g.Image(g.Point(i*78 + 200,50 + j*78), "emptySquare.gif")
                g.Image.draw(empty,window)
            if (board[i][j] == 1):
                yellowCounter = g.Image(g.Point(i*78 + 200,50 + j*78),  "yellowCounter.gif")
                g.Image.draw(yellowCounter,window)
            if (board[i][j] == -1):
                redCounter =g.Image(g.Point(i*78 + 200,50 + j*78),  "redCounter.gif")
                g.Image.draw(redCounter,window)
            
            
    print ("finished displaying board")


######################################
print ("start!")
window = g.GraphWin("Four in a Row", 1000, 600)
g.GraphWin.setBackground(window, "light green")
board [2][3] = 1
board [5][1] = -1
load_board()
for i in range (7):
    print (board[i])




print ("done!")

