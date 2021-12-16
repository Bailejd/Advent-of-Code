# Day 5: Hydrothermal Venture
#
# Results
# Part 1: 7473
# Part 2: 24164

# Consider replacing 1000x1000 sized array with dynamically resizing array
#   based on the largest x and y values in the input

import numpy as np

def part_one(data_list):
    vents = np.zeros((1000,1000), dtype=np.int32)
    for line in data_list:
        left, right = line.split(' -> ')
        x = int(left.split(',')[0]), int(right.split(',')[0])
        y = int(left.split(',')[1]), int(right.split(',')[1])
        
        if(x[0] == x[1] or y[0] == y[1]):
            if(x[0] > x[1] or y[0] > y[1]):
                x = (x[1], x[0])
                y = (y[1], y[0])

            x_diff = x[1] - x[0]
            y_diff = y[1] - y[0]
            new_x = []
            new_y = []

            if(y_diff == 0):
                for i in range(x_diff):
                    new_x.append(x[0] + i)
                new_x.append(x[1])
                new_y = [y[0]] * (x_diff+1)

            if(x_diff == 0):
                for i in range(y_diff):
                    new_y.append(y[0] + i)
                new_y.append(y[1])
                new_x = [x[0]] * (y_diff+1)
            
            points = list(zip(new_x, new_y))
            
            for point in points:
                vents[point[1]][point[0]] += 1
    
    unique, counts = np.unique(vents, return_counts=True)
    return sum(counts[2:])


def part_two(data_list):
    vents = np.zeros((1000,1000), dtype=np.int32)
    for line in data_list:
        left, right = line.split(' -> ')
        x = int(left.split(',')[0]), int(right.split(',')[0])
        y = int(left.split(',')[1]), int(right.split(',')[1])

        x_diff = x[1] - x[0]
        y_diff = y[1] - y[0]

        # Use whichever is not zero for the for loop
        diff = y_diff if x_diff == 0 else x_diff

        new_x = []
        new_y = []

        for i in range(abs(diff)):
            if(x_diff < 0):
                new_x.append(x[0] - i)
            elif(x_diff > 0):
                new_x.append(x[0] + i)
            else:
                new_x.append(x[0])
            if(y_diff < 0):
                new_y.append(y[0] - i)
            elif(y_diff > 0):
                new_y.append(y[0] + i)
            else:
                new_y.append(y[0])
        new_x.append(x[1])
        new_y.append(y[1])
        
        points = list(zip(new_x, new_y))
        
        for point in points:
            vents[point[1]][point[0]] += 1
    
    unique, counts = np.unique(vents, return_counts=True)
    return sum(counts[2:])


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read().split('\n')

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')


if __name__ == '__main__':
    main()
