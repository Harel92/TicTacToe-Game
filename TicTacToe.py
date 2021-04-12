import random


# Print current board
def display_board(board):
    print('\n' * 20)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


# Let first player choose 'X' or 'O'
def player_input():
    mark = 'PlaceHolder'
    arr = ['X', 'O']

    while mark not in arr:

        mark = input("Please pick a marker 'X' or 'O'").upper()

        if mark not in arr:
            print("Wrong input")

    return mark


# Place the mark on the board
def place_marker(board, marker, position):
    board[position] = marker


# The method checks if one of the players won
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True

    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True

    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True

    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True

    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True

    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True

    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True

    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True


# Define which player goes first randomly
def choose_first():
    arr = random.randint(1, 2)
    if arr == 1:
        return 'Player 1'
    return 'Player 2'


# Validate board position
def space_check(board, position):
    if position <= 0 or position >= 10:
        print("Invalid board position")
        return False

    if board[position] != 'X' and board[position] != 'O':
        return True
    print("Cell already occupied")
    return False


# Check if the board is full
def full_board_check(board):
    start = True
    for i in range(1, 10):
        if board[i] != 'X' and board[i] != 'O':
            start = False
            break
    return start


# Player picks position to place marker
def player_choice(board):
    num = 'PlaceHolder'
    free = False
    arr = range(1, 10)

    while num not in arr or free is False:

        num = input("Please pick a number (1-9): ")
        if num.isdigit():
            num = int(num)
            free = space_check(board, num)
        else:
            print("Invalid input")

    return num


# The method checks if the players want to play again
def replay():
    ret = False
    answer = 'ASK'
    arr = ['Y', 'N']

    while answer not in arr:
        answer = input("Do you want to play again? (Y/N) ").upper()

    if answer == 'Y':
        ret = True
    return ret


# Here the game begins!

print('Welcome to Tic Tac Toe!')

# Initialize game
while True:
    Game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    game_on = True
    first = choose_first()
    if first == 'Player 1':
        second = 'Player 2'
    else:
        second = 'Player 1'

    print(f'{first} goes first')
    first_mark = player_input()

    if first_mark == 'X':
        second_mark = 'O'
    else:
        second_mark = 'X'

    display_board(Game_board)

    # Start playing
    while game_on:
        # Player 1 Turn
        print(f'{first} turn')
        Game_position = player_choice(Game_board)
        place_marker(Game_board, first_mark, Game_position)
        display_board(Game_board)
        won = win_check(Game_board, first_mark)
        if won:
            print(f'{first} won!!!')
            break

        full = full_board_check(Game_board)
        if full:
            print("It's a tie!")
            break

        # Player2's turn.
        print(f'{second} turn')
        Game_position = player_choice(Game_board)
        place_marker(Game_board, second_mark, Game_position)
        display_board(Game_board)
        won = win_check(Game_board, second_mark)
        if won:
            print(f'{second} won!!!')
            break

        full = full_board_check(Game_board)
        if full:
            print("It's a tie!")
            break

    if not replay():
        break
