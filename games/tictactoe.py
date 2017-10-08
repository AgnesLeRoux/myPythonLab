#TIC TAC TOE

import random

def initializeBoard():
    return [[' ' for _ in range(0,3)] for _ in range(0,3)]
    #board1 = [[0]*3]*3

def drawBoard(board):
    print('.-+-+-.')
    print('|'+board[0][0]+'|'+board[0][1]+'|'+board[0][2]+'|')
    print('.-+-+-.')
    print('|'+board[1][0]+'|'+board[1][1]+'|'+board[1][2]+'|')
    print('.-+-+-.')
    print('|'+board[2][0]+'|'+board[2][1]+'|'+board[2][2]+'|')
    print('.-+-+-.')
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

def updateBoard(board,move,tag):
    #print("move ", move)
    coord = int2Coord(move)
    #print("coord " ,coord)
    if board[coord[0]][coord[1]] == ' ':
        board[coord[0]][coord[1]]=tag;
        return False
    else:
        return True

def int2Coord(nb):
    return[nb//3,nb%3]

def aiFindAMove(board,aiTag,playerTag):
    for i in range(0,9):
        board2 = copy(board)
        coord = int2Coord(i)
        if not updateBoard(board2,i,aiTag) and isWinner(board2,aiTag):
            return i
    for i in range(0,9):
        board2 = copy(board)
        if not updateBoard(board2,i,playerTag) and isWinner(board2,playerTag):
            return i   
    found = False
    if board[1][1]==' ':
        return 4
    while not found:
        move = random.randint(0,8)
        coord = int2Coord(move)
        if board[coord[0]][coord[1]]==' ':
            found = True
    return move

def copy(board):
    board2 = []
    for i in range(3):
        board2.append(board[i][:])
    return board2
def newGame():
    print('Hi! Let''s play to TIC-TAC-TOE')
    board = initializeBoard()
    if random.randint(1,2)==1:
        playerTag = 'X'
        aiTag='O'
        currentPlayer = 'player'
        print('You play first')
    else:
        aiTag = 'X'
        playerTag='O'
        currentPlayer='ai'
        print('Computer plays first')
    cpt=0
    while cpt<9:
        if currentPlayer=='player':
            invalidMove = True
            while invalidMove:
                move = int(input('What is your move? (0-8)'))
                invalidMove = updateBoard(board,move,playerTag)
            currentPlayer = 'ai'
        else:
            move = aiFindAMove(board,aiTag,playerTag)
            updateBoard(board,move,aiTag)
            currentPlayer = 'player'
        drawBoard(board)
        #print(board)
        cpt +=1
        if isWinner(board,playerTag):
            print("You win!")
            break
        elif isWinner(board,aiTag):
            print("The computer wins")
            break
    print("End")
    return None

newGame()
    
    
    
