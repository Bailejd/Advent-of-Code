# Day 7: The Treachery of Whales
#
# Results
# Part 1: 347449
# Part 2: 98039527

from statistics import median, mean
from math import ceil, floor

def part_one(positions):
    best_pos = int(median(positions))
    total_fuel_used = 0
    for pos in positions:
        total_fuel_used += abs(pos - best_pos)

    return total_fuel_used


def part_two(positions):
    mean_pos = mean(positions)
    
    # Must check the floor and ceil of mean value
    best_pos = (floor(mean_pos), ceil(mean_pos))
    total_fuel_used = [0,0]

    for i, b_pos in enumerate(best_pos):
        fuel_used = 0
        for pos in positions:
            num_moves = abs(pos - b_pos)
            fuel_used += int((pow(num_moves,2) + num_moves) / 2)
        
        total_fuel_used[i] = fuel_used
    
    return(min(total_fuel_used))


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        positions = [int(i) for i in f.read().split(',')]

    # Part 1
    print(f'Part 1: {part_one(positions)}')

    # Part 2
    print(f'Part 2: {part_two(positions)}')


if __name__ == '__main__':
    main()
