# Day 13: Shuttle Search

def part_one(data_list):
    pass


def part_two(data_list):
    pass


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.replace('\n', ',').split(',')
    data_list = [i for i in data_list if i != 'x']
    print(data_list)

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')
  
    
if __name__ == '__main__':
    main()