# Day 4: Giant Squid
#
# Results
# Part 1: 39984
# Part 2: 8468

import numpy as np

def check_win(board, row, col):
    if(np.nansum(board[row]) == 0 or np.nansum(board[:, col]) == 0):
        return True


def bingo(draws, boards):
    win_order = []
    win_scores = [0] * boards.shape[0]
    for draw in draws:
        for board_num, board in enumerate(boards):
            found = False
            if(win_scores[board_num] != 0):
                continue
            for row, line in enumerate(board):
                for col, num in enumerate(line):
                    if(num == draw):
                        boards[board_num][row][col] = np.nan
                        found = True
                        if(check_win(board, row, col)):
                            win_order.append(board_num)
                            win_scores[board_num] = int(np.nansum(board) * draw)
                        break
                if(found):
                    break
    
    return win_order, win_scores


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')
    
    draws = [int(draw) for draw in data_list[0].split(',')]

    # Format data for numpy array
    data_list = [line.replace('  ', ' ').lstrip().split() if line != '' else line for line in data_list[2:]]
    data_list = [[int(num) for num in line] for line in data_list if line != '']

    # Find number of boards
    num_boards = int(len(data_list) / 5)

    # Initialize numpy array
    boards = np.zeros((num_boards,5,5))

    # Fill numpy array
    for idx, line in enumerate(data_list):
        boards[idx // 5][idx % 5] = line

    win_order, win_scores = bingo(draws, boards)

    # Part 1
    print(f'Part 1: {win_scores[win_order[0]]}')

    # Part 2
    print(f'Part 2: {win_scores[win_order[-1]]}')


if __name__ == '__main__':
    main()
