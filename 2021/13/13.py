# Day 13: Transparent Origami
#
# Results
# Part 1: 592
# Part 2: JGAJEFKU

import re
import numpy as np

def part_one(data, folds):
    # Find maximum array dimensions
    max_x = 0
    max_y = 0

    # Find the maximum fold values
    # This will be the first x and y folds from the input
    for fold in folds:
        fold_val = int(fold[2:])
        if(fold[0] == 'x' and fold_val > max_x):
            max_x = fold_val*2+1
        if(fold[0] == 'y' and fold_val > max_y):
            max_y = fold_val*2+1
    
    # Create array of zeros of size (max_y, max_x)
    points = np.zeros((max_y, max_x), dtype=np.int32)

    # Plot points
    for coord in data:
        points[coord[1]][coord[0]] = 1

    # Fold array
    for i, fold in enumerate(folds):
        direction, val = fold[0], int(fold[2:])
        # If direction 'y' horizontal fold
        if(direction == 'y'):
            data1 = points[0:val, :]
            data2 = points[val+1:, :]

            # Numpy flip up/down
            data2 = np.flipud(data2)

            # Binary OR each sub-array into main array
            points = data1 | data2
        elif(direction == 'x'):
            data1 = points[:, 0:val]
            data2 = points[:, val+1:]

            # Numpy flip left/right
            data2 = np.fliplr(data2)

            # Binary OR each sub-array into main array
            points = data1 | data2
        
        # Sum after first fold for part 1
        if(i == 0):
            first_fold_sum = points.sum()
    
    # Return first_fold_sum for part 1 and points for part 2
    return first_fold_sum, points


def part_two(points):
    print(f'Part 2: ')

    # Print each line
    for line in points:
        for char in line:
            if(char == 0):
                print(' ', end='')
            elif(char == 1):
                print('█', end='')
        
        print()


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data = f.read().split('\n')

    # folds needs to skip the seperating empty line
    folds = data[data.index('')+1:]
    data = data[:data.index('')]

    # Tuple coordinates for each point
    data = [tuple(int(i) for i in ele.split(',')) for ele in data]

    # Regex to find 'x=###' and 'y=###'
    fold_re = r"[x|y]=\d*"
    folds = [re.search(fold_re, ele).group(0) for ele in folds]

    first_fold_sum, points = part_one(data, folds)

    # Part 1
    print(f'Part 1: {first_fold_sum}')

    # Part 2
    part_two(points)


if __name__ == '__main__':
    main()
