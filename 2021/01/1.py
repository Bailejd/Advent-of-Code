# Day 1: Sonar Sweep
#
# Results
# Part 1: 1139
# Part 2: 1103

def part_one(data_list):
    incr = 0

    for prev_, next_ in zip(data_list, data_list[1:]):
        if(prev_ < next_):
            incr += 1
    
    return incr
    

def part_two(data_list):
    incr = 0
    sums = []

    for prev_, curr_, next_ in zip(data_list, data_list[1:], data_list[2:]):
        sums.append(prev_ + curr_ + next_)

    for prev_, next_ in zip(sums, sums[1:]):
        if(prev_ < next_):
            incr += 1
    
    return incr


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = [int(i) for i in f.read().split('\n')]

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')
  
    
if __name__ == '__main__':
    main()
