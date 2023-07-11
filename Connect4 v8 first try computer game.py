import time
import random
import tkinter as tk
import graphics as g

real_board = [ [0,0,0,0,0,0] for i in range(7) ]
turn = [1,"yellow"] # 1 is user. (user begins)
lastFilled = [-1,-1]
depth = 1

thinking_board = [ [0,0,0,0,0,0] for i in range(7) ]

####################################################################################
def load_board():
    for i in range(7):
        for j in range(6):
            empty = g.Image(g.Point(i*78 + 260,100 + j*78), "emptySquare.gif")
            g.Image.draw(empty,window)

def fill_column(which_board, column):
    if(which_board == "real"):
        board = real_board
    else:
        board = thinking_board
    fullrow = board[column]
    i = 5
    while ( fullrow[i] != 0):
        i = i -1
        if(i ==-1):
            break
    if(i>-1):
        updated_board = fill_square(which_board,column,i,turn[1])
        return updated_board
    return board

def fill_square(board,a,b,color):
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
    return board

def switch_turn():
    if (turn[0] == 1):
        turn[0] = -1
        turn[1] = "red"
    else:
        turn[0] = 1
        turn[1] = "yellow"

def identical_Four(a,b,c,d, player):
    if(a == player and b == a and c == b and d == c):
        return True
    return False

####################################################################################

def check_win(board):
    return( check_win_rows(board) or check_win_columns(board) or check_win_diagonals(board))

def check_win_rows(board):
    a = lastFilled[0]
    player = turn[0]
    row = board[a]
    for j in range(3):
        if( identical_Four(row[j],row[j+1],row[j+2],row[j+3],player)):
            print("Player ", player, " won!")
            return True

def check_win_columns(board):
    a = lastFilled[0]
    b = lastFilled[1]
    player = turn[0]
    for j in range (4):
        if( identical_Four(   board[j][b],board[j+1][b],board[j+2][b],board[j+3][b],player ) ):
            print("Player", player, "won!")
            return True
        
def check_win_diagonals(board):
    a = lastFilled[0]
    b = lastFilled[1]
    player = turn[0]
    s = a + b
    if ( s < 3 or s > 8):
        return False
    if (check_win_upright_diagonal(s,board) or check_win_downright_diagonal(board)):
        print("Player ", player, " won!")
        return True
    return False

def check_win_upright_diagonal(s,board): # can use s because they all have same s
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

def check_win_downright_diagonal(board):
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

####################################################################################

def make_Computer_Move(): #can use deep copy probably
    thinking_board = [ [0,0,0,0,0,0] for i in range(7) ]
    for i in range(7):
        for j in range(6):
            thinking_board[i][j] = real_board[i][j]
    col_and_val = recursive_Computer_Move(depth,thinking_board)
    column = col_and_val[0]
    if(column == -1):
        print("random")
        column = random.randint(0,6)
    fill_column(real_board,column)



def recursive_Computer_Move(curr,board):
    if(curr == 1):
        for i in range (7):
            thinking_board = [ [0,0,0,0,0,0] for i in range(7) ]
            for i in range(7):
                for j in range(6):
                    thinking_board[i][j] = board[i][j]

        if(thinking_board[i][0]!=0):
            updated_board = fill_column(thinking_board,i)
            if(check_win(updated_board)):
                print("found winning")
                return [i,10]
        return [-1,0] #to symbolize that no move was winning


    maxval = 0 # maybe needs to be -inf
    chosen_column = -1 # to symbolize it doesnt matter.. ?
    for i in range (7):

        thinking_board = [ [0,0,0,0,0,0] for i in range(7) ]
        for i in range(7):
            for j in range(6):
                thinking_board[i][j] = board[i][j]

        if(thinking_board[i][0] != 0):   #switch, make this the first thing you check
            updated_board = fill_column(thinking_board,i)
            w = recursive_Computer_Move(curr-1,updated_board)
            if(maxval <w[1]):
                maxval = w[1]
                chosen_column = i
    return [chosen_column,maxval]
            
        
        

    
    
        
print ("start!")
window = g.GraphWin("Four in a Row", 1000, 600)
g.GraphWin.setBackground(window, "light green")
load_board()
while(1):
    if(turn[0]==1):
        mousePosition = window.getMouse()
        column = int((mousePosition.x - 260 + 39)// 78)
        if(column >= 0 and column <= 6):
            updated_real_board = fill_column(real_board,column)
            if(check_win(updated_real_board)):
                message = g.Text(     g.Point(500,250)    ,"Well done!")
                g.Text.setSize(message,36)
                g.Text.setTextColor(message,"white")
                g.Text.draw(message,window)
                time.sleep(3)
                break
    else:
        make_Computer_Move()
        if(check_win(real_board)):
            message = g.Text(     g.Point(500,250)    ,"Well done!")
            g.Text.setSize(message,36)
            g.Text.setTextColor(message,"white")
            g.Text.draw(message,window)
            time.sleep(3)
            break  
    switch_turn()
window.close()
print("done!")





