# Day 3: Binary Diagnostic
#
# Results
# Part 1: 3912944
# Part 2: 4996233

def part_one(data_list, width, height):
    ones = [0] * width
    zeros = [0] * width
    bin_list = [''] * width

    for i in range(width):
        for j in range(height):
            if(int(data_list[j][i]) == 1):
                ones[i] += 1
            else:
                zeros[i] += 1
    
    for i in range(width):
        if(ones[i] > zeros[i]):
            bin_list[i] = '1'
        else:
            bin_list[i] = '0'
    
    gamma = int('0b' + ''.join(bin_list), 2)
    epsilon = int('0b' + ''.join('1' if x == '0' else '0' for x in bin_list), 2)

    return gamma * epsilon


def part_two(data_list, height):
    return oxygen_rating(data_list, height) * scrubber_rating(data_list, height)


def oxygen_rating(data_list, height):
    found = False
    pos = 0

    while(not found):
        ones = 0
        zeros = 0
        rating = ''

        for i in range(height):
            if(int(data_list[i][pos]) == 1):
                ones += 1
            else:
                zeros += 1
        
        if(ones >= zeros):
            rating = '1'
        else:
            rating = '0'

        data_list = [val for val in data_list if val[pos] == rating]

        height = len(data_list)

        if(height == 1):
            found = True
        
        pos += 1
    
    return int('0b' + ''.join(data_list), 2)


def scrubber_rating(data_list, height):
    found = False
    pos = 0

    while(not found):
        ones = 0
        zeros = 0
        rating = ''

        for i in range(height):
            if(int(data_list[i][pos]) == 1):
                ones += 1
            else:
                zeros += 1
        
        if(ones < zeros):
            rating = '1'
        else:
            rating = '0'

        data_list = [val for val in data_list if val[pos] == rating]

        height = len(data_list)

        if(height == 1):
            found = True
        
        pos += 1
    
    return int('0b' + ''.join(data_list), 2)


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read().split('\n')

    width = len(data_list[0])
    height = len(data_list)

    # Part 1
    print(f'Part 1: {part_one(data_list, width, height)}')

    # Part 2
    print(f'Part 2: {part_two(data_list, height)}')


if __name__ == '__main__':
    main()
