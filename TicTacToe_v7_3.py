from random import randrange # Element imported here used to create computer's random move choice

# The code from lines 4-25 sets the initial elements required for the game and the following functions
board = []

for i in range(1,8,3):      # Here the board is created and filled with numbers 1-9
    row = [i+j for j in range(3)]
    board.append(row)

board[1][1] = 'X'           # The predetermined opening computer move

squares = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)] # All the squares
winningMoves = [[(0,0),(0,1),(0,2)], 
                [(2,0),(2,1),(2,2)],
                [(0,0),(1,0),(2,0)],
                [(0,2),(1,2),(2,2)],
                [(0,0),(1,1),(2,2)],
                [(0,1),(1,1),(2,1)],
                [(0,2),(1,1),(2,0)],
                [(1,0),(1,1),(1,2)]]

freeSquares = [] 
X = [(1,1)]                 # List of squares filled with X
O = []                      # List of squares filled with O
boardStatus = 'in play'     # Used to control the game execution loop

# Code from lines 29-88 defines the functions used in the game execution

def DisplayBoard():
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
def EnterMove():
    MakeListOfFreeFields()
    while True:
        userMove = int(input("Enter your move: "))
        if userMove not in freeSquares:
            print("Sorry invalid move, please try again.")
        else:
            a = (squares[userMove - 1][0])  # Uses the move to access the index of the squares list ([0]=row [1]=column)
            b = (squares[userMove - 1][1])  # (-1 as the index starts at 0 not 1)
            board[a][b] = 'O'
            O.append(squares[userMove - 1]) # Log the move in the list O
            break    
    DisplayBoard()

def MakeListOfFreeFields():
    del freeSquares[:]
    for row in board:               # Checks the board for X and O's
        for column in row:
            if column == 'X':
                continue
            elif column == 'O':
                continue
            else:
                freeSquares.append(column) # Adds free sqaures to freeSquares list
                
def VictoryFor(sign): # Sign here is used to access the relevant list of moves
    for row in winningMoves:
        winCounter = 0
        for elem in row:
            if elem in sign:
                winCounter += 1
                if winCounter == 3:
                    return 'win'
    else:
        return 'in play'
        
def DrawMove():
    MakeListOfFreeFields()          # Update the list of free squares for computer move
    randomPick = randrange(len(freeSquares))
    compMove = freeSquares[randomPick]
    a = (squares[compMove - 1][0])
    b = (squares[compMove - 1][1])
    board[a][b] = 'X'
    X.append(squares[compMove - 1])
    DisplayBoard()
        
# Game program begins here

DisplayBoard()
while boardStatus == 'in play':
    EnterMove()
    boardStatus = VictoryFor(O)
    if boardStatus == 'win':
        print('You win!')
        break
    DrawMove()
    boardStatus = VictoryFor(X)
    if boardStatus == 'win':
        print('Computer wins!')
        break
    if len(freeSquares) <= 1:
        print('It\'s a tie!')
        break


