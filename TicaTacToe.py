#tictactoe game
import os

turn = 0
playing = True
complete = False

#the board
board = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9'
}

#printing the board function
def printBoard(board):
    print(board[1] + ' |' + board[2] + ' |' + board[3])
    print('--+--+--')
    print(board[4] + ' |' + board[5] + ' |' + board[6])
    print('--+--+--')
    print(board[7] + ' |' + board[8] + ' |' + board[9])
printBoard(board)


#check the turn using the modulo
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'
    
#check the winner function  
def checkForWin(board):
    #check for horizontal cases
    if (board[1] == board[2] == board[3]) \
    or (board[4] == board[5] == board[6]) \
    or (board[7] == board[8] == board[9]):
        return True
    #check for vertical cases
    elif (board[1] == board[4] == board[7]) \
    or (board[2] == board[5] == board[8]) \
    or (board[3] == board[6] == board[9]):
        return True
    #check for diagonal cases
    elif (board[1] == board[5] == board[9]) \
    or (board[3] == board[5] == board[7]):
        return True
    else:
        return False
        
#the while loop for playing
while playing:
    #Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    printBoard(board)
    print("Player " + str((turn%2)+1) + "'s turn: Pick your spot or press q to quit")


    # get input player
    choice = input()
    if choice == 'q':
        playing = False
        #check if the player gave a number from 1-9
    elif str.isdigit(choice) and int(choice) in board:
        #check if the spot has already been taken
        if not board[int(choice)] in {"X" , "O"}:
               # valid input, update the board
               turn += 1
               board[int(choice)] = check_turn(turn)
    #check if game has ended ==> if someone won
    if checkForWin(board):
        playing = False
        complete = True
    if turn > 8:
        playing = False

#out of the loop and print the result
#draw the board for the last time
os.system('cls' if os.name == 'nt' else 'clear')
printBoard(board)
if complete:
    print("Player " + str((turn%2)+1) + " wins!")
else:
    print("Draw")
print("thanks for playing!")






    