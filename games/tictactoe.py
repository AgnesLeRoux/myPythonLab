#TIC TAC TOE

import random

def initializeBoard():
    return [[' ' for _ in range(0,3)] for _ in range(0,3)]
    #board1 = [[0]*3]*3

def drawBoard(board):
    print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
    print('-+-+-')
    print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
    print('-+-+-')
    print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
    return None

def isWinner(board,player):
    return ((board[0][0]==player and board[0][1]==player and board[0][2]==player)
    or (board[1][0]==player and board[1][1]==player and board[1][2]==player)
    or (board[2][0]==player and board[2][1]==player and board[2][2]==player)
    or (board[0][0]==player and board[1][0]==player and board[2][0]==player)
    or (board[0][1]==player and board[1][1]==player and board[2][1]==player)
    or (board[0][2]==player and board[1][2]==player and board[2][2]==player)
    or (board[0][0]==player and board[1][1]==player and board[2][2]==player)
    or (board[2][0]==player and board[1][1]==player and board[0][2]==player))

def updateBoard(board,move,p):
    coord = int2Coord(move)
    if board[coord[0]][coord[1]] == '.':
       board[coord[0]][coord[1]]=p;
       return True
    else:
        return False

def int2Coord(nb):
    return[nb//3,nb%3]
       
def newGame():
    print('Hi! Let''s play to TIC-TAC-TOE')
    board = initializeBoard()
    if random.randint(1,2)==1:
        player = 'X'
        ai='O'
        currentPlayer = 'player'
        print('You play first')
    else:
        ai = 'X'
        player='O'
        currentPlayer='ai'
        print('Computer plays first')
    cpt=0
    while cpt<9:
        if currentPlayer=='player':
            invalidMove = True
            while invalidMove:
                move = input('What is your move? (0-8)')
                invalidMove = updateBoard(board,move,player)
        else:
            print('todo')
        cpt +=1
            
    return None

newGame()
    
    
    
