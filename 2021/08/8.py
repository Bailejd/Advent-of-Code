# Day 8: Seven Segment Search
#
# Results
# Part 1: 519
# Part 2: 1027483

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def find_easy_digits(right, decoded):
    for val in right:
        val_length = len(val)
        # Find 1, Only digit made of 2 segments
        if(val_length == 2):
            decoded[1] = val
        # Find 4, Only digit made of 4 segments
        elif(val_length == 4):
            decoded[4] = val
        # Find 7, Only digit made of 3 segments
        elif(val_length == 3):
            decoded[7] = val
        # Find 8, Only digit made of 7 segments
        elif(val_length == 7):
            decoded [8] = val


def part_one(data_list):
    total = 0
    for line in data_list:
        _, left = line.split(' | ')
        left = left.split(' ')
        for ele in left:
            len_ele = len(ele)
            if(len_ele == 2 or len_ele == 4 or len_ele == 3 or len_ele == 7):
                total += 1
    
    return total


def part_two(data_list):
    total = 0
    for line in data_list:
        decoded = [-1] * 10
        output = [-1] * 4
        right, left = line.split(' | ')
        right, left = right.split(' '), left.split(' ')

        # Create lists based on length of coded number
        len_6 = [num for num in right if len(num) == 6]
        len_5 = [num for num in right if len(num) == 5]

        find_easy_digits(right, decoded)
        
        # Check length 6 first since 5 depends on 6
        for ele in len_6:
            # Find 9, 9 contains all of 4
            if(set(ele).issuperset(set(decoded[4]))):
                decoded[9] = ele
            # Find 0, 0 contains all of 7
            elif(set(ele).issuperset(set(decoded[7]))):
                decoded[0] = ele
            # Find 6, 6 if length is 6 and ele is not 9 or 0
            else:
                decoded[6] = ele
        
        for ele in len_5:
            # Find 3, 3 contains all of 7
            if(set(ele).issuperset(set(decoded[7]))):
                decoded[3] = ele
            # Find 5, 5 contains part of 6
            elif(set(ele).issubset(set(decoded[6]))):
                decoded[5] = ele
            # Find 2, 2 if length is 5 and ele is not 3 or 5
            else:
                decoded[2] = ele

        # Use decoded right side to solve left side
        for i, ele in enumerate(left):
            for j, val in enumerate(decoded):
                if(len(set(ele).difference(set(val))) == 0 and len(ele) == len(val)):
                    output[i] = j
            
        # Convert list to int
        string_list = [str(i) for i in output]
        output = int(''.join(string_list))

        # Add lines output to running total
        total += output
    
    return total


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
