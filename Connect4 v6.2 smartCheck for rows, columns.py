import time
import tkinter as tk
import graphics as g

board = [ [0,0,0,0,0,0] for i in range(7) ]
turn = [1,"yellow"]
lastFilled = [-1,-1]

def load_board():
    for i in range(7):
        for j in range(6):
            empty = g.Image(g.Point(i*78 + 260,100 + j*78), "emptySquare.gif")
            g.Image.draw(empty,window)

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
        board[a][b] = -1
    if(color == "yellow"):
        yellowCounter = g.Image(g.Point(a*78 + 260, 100 + b*78),  "yellowCounter.gif")
        g.Image.draw(yellowCounter,window)
        board[a][b] = 1
    lastFilled[0] = a
    lastFilled[1] = b

def switch_turn():
    if (turn[0] == 1):
        turn[0] = -1
        turn[1] = "red"
    else:
        turn[0] = 1
        turn[1] = "yellow"


def check_win():
    return( check_win_rows() or check_win_columns() or check_win_diagonals())



#do a clever check using lastFilled
#for now, trivial check (overkill)

def check_win_rows():
    a = lastFilled[0]
    player = turn[0]
    row = board[a]
    for j in range(3):
        if( identical_Four(row[j],row[j+1],row[j+2],row[j+3],player)):
            print("Player ", player, " won!")
            return True

def check_win_columns():
    a = lastFilled[0]
    b = lastFilled[1]
    player = turn[0]
    for j in range (4):
        if( identical_Four(   board[j][b],board[j+1][b],board[j+2][b],board[j+3][b],player ) ):
            print("Player", player, "won!")
            return True
        

def check_win_diagonals():
    return False



def identical_Four(a,b,c,d, player):
    if(a == player and b == a and c == b and d == c):
        return True
    return False


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
        if(check_win()):
            message = g.Text(     g.Point(500,250)    ,"Well done!")
            g.Text.setSize(message,36)
            g.Text.setTextColor(message,"white")
            g.Text.draw(message,window)
            time.sleep(3)
            break
        switch_turn()
window.close()
print("done!")





