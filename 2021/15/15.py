# Day 15: Chiton
#
# Results
# Part 1: 503
# Part 2: 2853

import numpy as np
from queue import PriorityQueue

def valid_pos(coord, shape):
    if(coord[0] < 0 or coord[1] < 0):
        return False

    if(coord[0] >= shape[0] or coord[1] >= shape[1]):
        return False

    return True


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(data_list):
    start = (0,0)
    dest = (len(data_list[0])-1, len(data_list)-1)
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    offsets = ((1,0), (0,1), (-1,0), (0,-1))

    while not frontier.empty():
        pos = frontier.get()[1]

        if(pos == dest):
            break

        for offset in offsets:
            next_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if(valid_pos(next_pos, data_list.shape)):
                new_cost = cost_so_far[pos] + data_list[next_pos[1]][next_pos[0]]
                if(next_pos not in came_from or new_cost < cost_so_far[next_pos]):
                    cost_so_far[next_pos] = new_cost
                    prio = new_cost + manhattan_distance(next_pos, dest)
                    frontier.put((prio, next_pos))
                    came_from[next_pos] = pos
    
    return cost_so_far[pos]


def part_one(data_list):
    return a_star(data_list)


def part_two(data_list):
    for i in range(1,5):
        if(i == 1):
            temp_array = np.array([[ele+i if ele+i < 10 else ((ele+i)%10)+1 for ele in line] for line in data_list])
        else:
            temp_array = np.array(np.hstack((temp_array ,[[ele+i if ele+i < 10 else ((ele+i)%10)+1 for ele in line] for line in data_list])))
    data_list = np.hstack((data_list, temp_array))

    for i in range(5):
        if(i == 0):
            temp_array = np.array(data_list)
        else:
            temp_array = np.array(np.vstack((temp_array, [[ele+i if ele+i < 10 else ((ele+i)%10)+1 for ele in line] for line in data_list])))
    data_list = temp_array

    return a_star(data_list)


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read().split('\n')
    
    data_list = [[int(char) for char in line] for line in data_list]
    data_list = np.array(data_list)
    
    # Part 1
    print(f'Part 1: {part_one(data_list)}')


    # Part 2
    print(f'Part 2: {part_two(data_list)}')


if __name__ == '__main__':
    main()
