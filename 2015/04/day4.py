# Day 4: The Ideal Stocking Stuffer
#
# Results
# Part 1: 254575
# Part 2: 1038736

import hashlib

def part_one(key):
    counter = 0

    while(True):
        data = key + str(counter)
        hex = hashlib.md5(data.encode()).hexdigest()

        counter += 1

        if(hex.startswith("00000")):
            return data
    

def part_two(key):
    counter = 0

    while(True):
        data = key + str(counter)
        hex = hashlib.md5(data.encode()).hexdigest()

        counter += 1

        if(hex.startswith("000000")):
            return data


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        key = f.readline()

    # Part 1
    print(f'Part 1: {part_one(key)}')

    # Part 2
    print(f'Part 2: {part_two(key)}')
  
    
if __name__ == '__main__':
    main()
