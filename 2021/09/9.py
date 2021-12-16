# Day 9: Smoke Basin
#
# Results
# Part 1: 486
# Part 2: 1059300

import numpy as np
from collections import deque

def check(data_list, x, y):
    check_pos = [[x,y+1],[x+1,y],[x,y-1],[x-1,y]]

    for pos in check_pos:
        if(pos[0] >= data_list.shape[1] or pos[0] < 0):
            continue
        elif(pos[1] >= data_list.shape[0] or pos[1] < 0):
            continue
        if(data_list[pos[1]][pos[0]] <= data_list[y][x]):
            return False
    
    return True


def valid(low_points, x, y):
    if(y < 0 or x < 0 or y >= low_points.shape[0] or x >= low_points.shape[1]):
        return False

    if(low_points[y][x] == 1):
        return False
    
    return True


def bfs(data_list, low_points, coord):
    basin_size = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()

    q.append((coord[1],coord[0]))
    low_points[coord[0]][coord[1]] = 1

    while(len(q) > 0):
        node = q.popleft()
        x = node[0]
        y = node[1]

        for i in range(4):
            adj_x = x + dx[i]
            adj_y = y + dy[i]
            if(valid(low_points, adj_x, adj_y) and data_list[adj_y][adj_x] != 9):
                q.append((adj_x, adj_y))
                low_points[adj_y][adj_x] = 1
                basin_size += 1
    
    return basin_size


def part_one(data_list):
    total = 0
    low_points = np.zeros(data_list.shape, dtype=np.int32)
    for y, line in enumerate(data_list):
        for x, val in enumerate(line):
            if(check(data_list, x, y)):
                total += val + 1
                low_points[y][x] = 1
    
    return total, low_points


def part_two(data_list, low_points):
    basin_sizes = []
    low_coords = np.where(low_points == 1)
    low_coords = np.asarray(low_coords).T
    for coord in low_coords:
        basin_sizes.append(bfs(data_list, low_points, coord))
    
    basin_sizes.sort()

    return (basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = np.array([[int(num) for num in line] for line in f.read().split('\n')])

    low_risk_level, low_points = part_one(data_list)

    # Part 1
    print(f'Part 1: {low_risk_level}')

    # Part 2
    print(f'Part 2: {part_two(data_list, low_points)}')


if __name__ == '__main__':
    main()
