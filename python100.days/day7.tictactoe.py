import os

def print_board(b:'dict'):
    print(b['TL'] + '|' + b['TM'] + '|' + b['TR'])
    print('-+-+-')
    print(b['ML'] + '|' + b['MM'] + '|' + b['MR'])
    print('-+-+-')
    print(b['BL'] + '|' + b['BM'] + '|' + b['BR'])


def run_game():
    game_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    print_board(game_board)
    current_board = game_board.copy()
    run = True
    turn = ''
    place = ''
    counter = 0
    while run:
        if turn == '' or turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        while place not in game_board.keys():
            place = str(input('Now is %s turn, please input the command:' % turn))
        current_board[place] = turn
        print_board(current_board)
        place = ''
        counter += 1
        if counter > 8:
            break


if __name__ == '__main__':
    run_game()
