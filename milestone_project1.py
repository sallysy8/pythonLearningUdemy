'''
Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
Keep in mind that this project can take anywhere between several hours to several days.

'''
import random

def frame_board(inputNum):
    #print('\n'*100)
    edge = ('+' + '-'*3)*3 + '+'
    print(edge)
    print('| ' + inputNum[7] + ' | ' + inputNum[8] + ' | ' + inputNum[9] + ' |')
    print(edge)
    print('| ' + inputNum[4] + ' | ' + inputNum[5] + ' | ' + inputNum[6] + ' |')
    print(edge)
    print('| ' + inputNum[1] + ' | ' + inputNum[2] + ' | ' + inputNum[3] + ' |')
    print(edge)

#test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
#frame_board(test_board)
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Please pick a marker 'X' or 'O'! ").upper()
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')
#print(player_input())

def place_marker(inputNum, marker, position):
    inputNum[position] = marker


#place_marker(test_board, '$', 8)
#frame_board(test_board)

def win_check(inputNum, mark):
    return ((inputNum[7] == mark and inputNum[8] == mark and inputNum[9] == mark) or 
    (inputNum[4] == mark and inputNum[5] == mark and inputNum[6] == mark) or
    (inputNum[1] == mark and inputNum[2] == mark and inputNum[3] == mark) or
    (inputNum[1] == mark and inputNum[4] == mark and inputNum[7] == mark) or
    (inputNum[2] == mark and inputNum[5] == mark and inputNum[8] == mark) or
    (inputNum[3] == mark and inputNum[6] == mark and inputNum[9] == mark) or
    (inputNum[1] == mark and inputNum[5] == mark and inputNum[9] == mark) or
    (inputNum[3] == mark and inputNum[5] == mark and inputNum[7] == mark) )


#print(win_check(test_board, 'O'))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#print(choose_first())

def space_check(inputNum, position):
    return inputNum[position] == ' '

#print(space_check(test_board, 1))

def full_board_check(inputNum):
    for i in range(1,10):
        if space_check(inputNum, i) is True:
            return False
    return True

#print(full_board_check(test_board))

def player_choice(inputNum):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(inputNum,position):
        position = int(input('Please choose a number from 1 to 9'))
    
    return position


def replay():

    response = input('Do you want to play again? Y/N ').lower()
    return response[0] == 'y'


print('Welcome to Tic Tac Toe!')

while True:
    # reset the board
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('{} will go first'.format(turn))

    play_game = input('Are you ready to play? Y/N ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            frame_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                frame_board(theBoard)
                print('Player 1: Congratulations! You won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    frame_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # player 2's turn
            frame_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                frame_board(theBoard)
                print('Player 2: Congratulations! You won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    frame_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break





