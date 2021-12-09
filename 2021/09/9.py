# Day 9: Smoke Basin
#
# Results
# Part 1: 486
# Part 2:

def format_print(data_list):
    for line in data_list:
        print(line)


def check(data_list, x, y):
    check_pos = [[x,y+1],[x+1,y],[x,y-1],[x-1,y]]

    for pos in check_pos:
        if(pos[0] >= len(data_list[0]) or pos[0] < 0):
            continue
        elif(pos[1] >= len(data_list) or pos[1] < 0):
            continue
        if(data_list[pos[1]][pos[0]] <= data_list[y][x]):
            return False
    
    return True


def part_one(data_list):
    total = 0
    for y, line in enumerate(data_list):
        for x, val in enumerate(line):
            if(check(data_list, x, y)):
                total += val + 1
    
    return total


def part_two(data_list):
    pass


def main():
    # Read input file
    with open("./ex.txt", "r") as f:
        data_list = [[int(num) for num in line] for line in f.read().split('\n')]

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')


if __name__ == '__main__':
    main()
