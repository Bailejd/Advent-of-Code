# Day 4: Passport Processing

import re

def part_one(data_list):
    numValid = 0

    # Set inital bools
    boolDict = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False, 'cid': False}

    for i in range(len(data_list)):
        # If empty row (end of passport) check for required fields 
        if(data_list[i] == ''):
            valid = True
            for key in boolDict:
                if(boolDict[key] == False and key != 'cid'):
                    valid = False

                # Reset bools
                boolDict[key] = False

            if(valid == True):
                numValid += 1

        else:
            for key in boolDict:
                if(boolDict[key] == False):
                    match = re.search(key, data_list[i])
                    boolDict[key] = bool(match)

    return numValid


def part_two(data_list):
    pass


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        data_list = f.read()
    
    data_list = data_list.split('\n')

    # Part 1
    print(f'Part 1: {part_one(data_list)}')

    # Part 2
    print(f'Part 2: {part_two(data_list)}')
  
    
if __name__ == '__main__':
    main()
