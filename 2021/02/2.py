# Day 2: Dive!
#
# Results
# Part 1: 1499229
# Part 2: 1340836560

def part_one(data_list):
    horizonal = 0
    depth = 0

    for direction in data_list:
        dir, amount = direction.split()

        if(dir == 'forward'):
            horizonal += int(amount)
        elif(dir == 'down'):
            depth += int(amount)
        elif(dir == 'up'):
            depth -= int(amount)

    return horizonal * depth


def part_two(data_list):
    horizonal = 0
    depth = 0
    aim = 0

    for direction in data_list:
        dir, amount = direction.split()
        amount = int(amount)

        if(dir == 'forward'):
            horizonal += amount
            depth += aim * amount
        elif(dir == 'down'):
            aim += amount
        elif(dir == 'up'):
            aim -= amount

    return horizonal * depth


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
