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
    a = lastFilled[0]
    b = lastFilled[1]
    s = a + b
    if ( s < 3 or s > 8):
        return False
    return (check_win_upright_diagonal(s) or check_win_downright_diagonal())



def check_win_upright_diagonal(s): # can use s because they all have same s
    player = turn[0]
    return(
        identical_Four(board[0][3], board[1][2], board[2][1], board[3][0], player) or
        
        identical_Four(board[0][4], board[1][3], board[2][2], board[3][1], player) or
        identical_Four(board[1][3], board[2][2], board[3][1], board[4][0], player) or
        
        identical_Four(board[0][5], board[1][4], board[2][3], board[3][2], player) or
        identical_Four(board[1][4], board[2][3], board[3][2], board[4][1], player) or
        identical_Four(board[2][3], board[3][2], board[4][1], board[5][0], player) or
        
        identical_Four(board[1][5], board[2][4], board[3][3], board[4][2], player) or
        identical_Four(board[2][4], board[3][3], board[4][2], board[5][1], player) or
        identical_Four(board[3][3], board[4][2], board[5][1], board[6][0], player) or
        
        identical_Four(board[2][5], board[3][4], board[4][3], board[5][2], player) or
        identical_Four(board[3][4], board[4][3], board[5][2], board[6][1], player) or
        
        identical_Four(board[3][5], board[4][4], board[5][3], board[6][2], player)
        )


def check_win_downright_diagonal():
    player = turn[0]
    return(
        identical_Four(board[0][2], board[1][3], board[2][4], board[3][5], player) or
        
        identical_Four(board[0][1], board[1][2], board[2][3], board[3][4], player) or
        identical_Four(board[1][2], board[2][3], board[3][4], board[4][5], player) or
        
        identical_Four(board[0][0], board[1][1], board[2][2], board[3][3], player) or
        identical_Four(board[1][1], board[2][2], board[3][3], board[4][4], player) or
        identical_Four(board[2][2], board[3][3], board[4][4], board[5][5], player) or
        
        identical_Four(board[1][0], board[2][1], board[3][2], board[4][3], player) or
        identical_Four(board[2][1], board[3][2], board[4][3], board[5][4], player) or
        identical_Four(board[3][2], board[4][3], board[5][4], board[6][5], player) or
        
        identical_Four(board[2][0], board[3][1], board[4][2], board[5][3], player) or
        identical_Four(board[3][1], board[4][2], board[5][3], board[6][4], player) or
        
        identical_Four(board[3][0], board[4][1], board[5][2], board[6][3], player)
        )









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





