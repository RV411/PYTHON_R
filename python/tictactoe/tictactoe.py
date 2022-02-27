import random

board = [' ' for x in range(10)]#se inicia el arreglo de 9


def insertLetter(letter,pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        print("Juego Truncado")
        return True


def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))


def playerMove():
    run = True
    while run:
        move = input("Escribe un numero entre 1 y 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Espacio Ocupado')
            else:
                print('Escribe un numero entre 1 y 9')

        except:
            print('Escribe un numero')


def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(lista):
    ln = len(lista)
    r = random.randrange(0,ln)
    return lista[r]


def main():
    print("=======================================")
    print(" ¡Bienvenido(a) al juego del GATO! ")
    print("=======================================")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Perdiste!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('La computadora puso en' , move , ':')
                printBoard(board)
        else:
            print("GANASTE!")
            break




    if isBoardFull(board):
        print("Juego Truncado")

while True:
    x = input("Quieres jugar gato? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
