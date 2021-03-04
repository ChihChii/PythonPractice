import os


def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def check_board(board):
    if ((board['1'] == board['2'] == board['3']) or (board['4'] == board['5'] == board['6']) or (board['7'] == board['8'] == board['9']) or (board['1'] == board['4'] == board['7']) or (board['2'] == board['5'] == board['8']) or (board['3'] == board['6'] == board['9']) or (board['1'] == board['5'] == board['9']) or (board['3'] == board['5'] == board['7'])):
        return 1
    else:
        return 0


def main():
    init_board = {
        '1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9'
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'X'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('輪到%s了, 請輸入位置: ' % turn)
            if curr_board[move] == move:
                counter += 1
                curr_board[move] = turn
            os.system('clear')
            print_board(curr_board)
            if(check_board(curr_board)):
                print('%s win !!!' % turn)
                counter = 10
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        choice = input('再玩一局?(yes|no)')
        begin = (choice == 'yes')


if __name__ == '__main__':
    main()
