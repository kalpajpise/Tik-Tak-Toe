import random


def player_input():
    # Input for the player
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# test cases for the marker generation
# player1_marker,player2_marker=player_input()
# print(player1_marker)
# print(player2_marker)


def choose_first():
    # Who will play 1st
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def display_board(board):
    print("\n" * 80)
    print("   |   |   ")
    print(" " + board[1] + " |" + " " + board[2] + " |" + " " + board[3])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[4] + " |" + " " + board[5] + " |" + " " + board[6])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[7] + " |" + " " + board[8] + " |" + " " + board[9])


# the_board=['0',X','O','X','O','X','O','X','X','X','O']
# display_board(the_board)


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, player):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(f'{player} choose your next position: (1-9) - (From the top left)'))

    return position


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def relpay():
    play = input("Do u want to play again. Yes or NO")
    return play.lower() == 'y'


def main():
    stop = False
    while not stop:
        game_on = True
        the_board = [" "] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()

        while game_on:

            if turn == 'Player 1':
                display_board(the_board)

                position = player_choice(the_board, turn)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print(f"Congratulation {turn} has won the match ")
                    game_on = False
                    stop = True

                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The match is draw")
                        break

                    else:
                        turn = "Player 2"

            else:
                display_board(the_board)
                position = player_choice(the_board,turn)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print(f"Congratulation {turn} has won the match ")
                    game_on = False
                    stop = True


                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The match is draw")
                        break

                    else:
                        turn = "Player 1"


if __name__ == '__main__':
    Flag = True
    print("==== Tik Tak Toe ====")
    play_game = input('Are u ready to play Yes or No')
    if play_game[0].lower() == 'y':
        Flag = True
        main()
    else:
        Flag = False
        print("Thanks for playing  the game")

    while Flag:
        if relpay():
            main()
        else:
            Flag = False
            print("Thanks for playing  the game")
